import json
from pathlib import Path
from datetime import datetime

from modules.planner import generate_video_plan
from modules.preprocess import process_product_image
from modules.shot_builder import build_shots
from modules.video_generator import generate_final_video
from modules.prompt_builder import build_video_prompt_jobs
from modules.scorer import log_generation


OUTPUT_DIR = Path("output")
MUSIC_PATH = "assets/music/background.mp3"

# Must match CROSSFADE_DURATION in modules/composer.py
CROSSFADE_DURATION = 0.35


def fix_scene_durations_for_crossfade(plan, selected_duration):
    """
    Keeps smooth crossfade transitions while making final video
    close to the user's selected duration.
    """
    scenes = plan.get("scenes", [])

    if not scenes:
        return plan

    total_duration = float(selected_duration)
    scene_count = len(scenes)

    total_overlap = CROSSFADE_DURATION * (scene_count - 1)
    adjusted_total_duration = total_duration + total_overlap

    scene_duration = adjusted_total_duration / scene_count

    for scene in scenes:
        scene["duration"] = round(scene_duration, 2)

    return plan


def run_full_pipeline(
    image_path,
    product_name,
    product_type,
    product_description,
    style_name,
    target_audience,
    duration,
    output_format="MP4",
    backend_name="template",
    prepare_ai_prompts=True
):
    """
    Full project pipeline order:

    1. Get user input
    2. Run planner
    3. Preprocess image
    4. Generate scene plan
    5. Create base scenes with template engine
    6. Prepare optional AI video prompt jobs
    7. Compose scenes
    8. Add captions/music/SFX through composer/audio system
    9. Export MP4/GIF
    10. Save metadata to CSV
    """

    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    plan_path = OUTPUT_DIR / f"plan_{run_id}.json"
    final_video_path = OUTPUT_DIR / f"final_video_{run_id}.mp4"

    try:
        # 1. Run planner
        plan = generate_video_plan(
            product_name=product_name,
            product_description=product_description,
            style=style_name,
            target_audience=target_audience,
            duration=int(duration)
        )

        # 2. Fix scene durations
        plan = fix_scene_durations_for_crossfade(plan, duration)

        # 3. Save scene plan JSON
        with open(plan_path, "w", encoding="utf-8") as file:
            json.dump(plan, file, indent=2)

        # 4. Preprocess product image
        preprocess_outputs = process_product_image(image_path)

        # 5. Create base scenes with template engine
        build_shots(
            plan=plan,
            style_name=style_name,
            product_image_path=preprocess_outputs["transparent_product"]
        )

        # 6. Optional future AI-video prompt jobs
        ai_jobs_path = ""

        if prepare_ai_prompts:
            build_video_prompt_jobs(
                plan=plan,
                product_name=product_name,
                product_description=product_description,
                style_name=style_name,
                target_audience=target_audience,
                input_image_path=preprocess_outputs["transparent_product"],
                output_dir="output/ai_clip_jobs"
            )

            ai_jobs_path = "output/ai_clip_jobs/video_prompt_jobs.json"

        # 7. Export MP4 and optional GIF
        export_gif = output_format == "GIF"

        generate_final_video(
            backend_name=backend_name,
            manifest_path="output/shots/shot_manifest.json",
            music_path=str(MUSIC_PATH),
            output_path=str(final_video_path),
            style_name=style_name,
            export_gif=export_gif
        )

        # 8. Select downloadable output
        download_path = final_video_path

        if export_gif:
            gif_path = final_video_path.with_suffix(".gif")
            if gif_path.exists():
                download_path = gif_path

        # 9. Save metadata to CSV
        log_generation(
            run_id=run_id,
            product_name=product_name,
            product_type=product_type,
            prompt=product_description,
            style=style_name,
            backend_used=backend_name,
            duration=duration,
            output_file=str(download_path),
            plan_json_path=str(plan_path),
            status="success",
            notes=f"output_format={output_format}; ai_jobs_path={ai_jobs_path}"
        )

        return {
            "success": True,
            "run_id": run_id,
            "plan": plan,
            "plan_path": str(plan_path),
            "preview_video": str(final_video_path),
            "download_file": str(download_path),
            "ai_jobs_path": ai_jobs_path,
            "message": "Pipeline completed successfully."
        }

    except Exception as error:
        log_generation(
            run_id=run_id,
            product_name=product_name,
            product_type=product_type,
            prompt=product_description,
            style=style_name,
            backend_used=backend_name,
            duration=duration,
            output_file="",
            plan_json_path=str(plan_path) if plan_path.exists() else "",
            status="failed",
            error_message=str(error),
            notes=f"output_format={output_format}"
        )

        return {
            "success": False,
            "run_id": run_id,
            "plan": {},
            "plan_path": "",
            "preview_video": None,
            "download_file": None,
            "ai_jobs_path": "",
            "message": f"Error: {str(error)}"
        }