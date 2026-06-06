import json
from pathlib import Path

try:
    from modules.utils import load_styles
except ModuleNotFoundError:
    from utils import load_styles


def clean_text(text):
    if not text:
        return ""
    return str(text).replace("\n", " ").strip()


def build_scene_prompt(
    scene,
    product_name,
    product_description,
    style_name,
    style_config,
    target_audience
):
    scene_type = scene.get("type", "hero")
    motion = scene.get("motion", "slow zoom in")
    overlay_text = scene.get("text", "")

    bg_type = style_config.get("bg_type", "clean premium background")
    colors = style_config.get("colors", [])
    music_mood = style_config.get("music_mood", "premium cinematic")
    font_style = style_config.get("font_style", "clean modern")

    color_description = ", ".join(colors)

    base_prompt = (
        f"Premium commercial product video of {product_name}. "
        f"Product description: {product_description}. "
        f"Target audience: {target_audience}. "
        f"Style: {style_name}. "
        f"Background style: {bg_type}. "
        f"Color palette: {color_description}. "
        f"Lighting: cinematic studio lighting, soft reflections, polished highlights. "
        f"Camera motion: {motion}. "
        f"Mood: {music_mood}, high-end, clean, professional. "
        f"Product should remain centered, sharp, and consistent. "
    )

    if scene_type == "hero":
        scene_prompt = (
            base_prompt +
            "Hero shot, product is the main focus, elegant reveal, slow premium zoom, "
            "minimal background motion, luxury advertisement look."
        )

    elif scene_type == "detail":
        scene_prompt = (
            base_prompt +
            "Detail feature shot, highlight product texture and quality, subtle light sweep, "
            "gentle side camera movement, refined premium look."
        )

    elif scene_type == "cta":
        scene_prompt = (
            base_prompt +
            "Final call-to-action shot, product centered, strong clean ending, "
            "premium brand finish, smooth fade-out feeling."
        )

    else:
        scene_prompt = (
            base_prompt +
            "Clean product advertising shot, smooth motion, professional commercial finish."
        )

    if overlay_text:
        scene_prompt += f" Intended text overlay meaning: {overlay_text}. Text should be clean and readable if used."

    return clean_text(scene_prompt)


def build_negative_prompt():
    return (
        "low quality, blurry, distorted product, changing product shape, warped logo, "
        "bad text, unreadable text, messy background, extra objects, flickering, "
        "unstable motion, shaky camera, deformed packaging, unrealistic reflections, "
        "poor lighting, noisy video, low resolution"
    )


def build_video_prompt_jobs(
    plan,
    product_name,
    product_description,
    style_name="luxury",
    target_audience="general audience",
    input_image_path="output/preprocessed/product_transparent.png",
    output_dir="output/ai_clip_jobs"
):
    styles = load_styles()
    style_config = styles.get(style_name, styles["luxury"])

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    scenes = plan.get("scenes", [])
    jobs = []

    for index, scene in enumerate(scenes, start=1):
        scene_type = scene.get("type", f"scene_{index}")
        duration = scene.get("duration", 2)

        positive_prompt = build_scene_prompt(
            scene=scene,
            product_name=product_name,
            product_description=product_description,
            style_name=style_name,
            style_config=style_config,
            target_audience=target_audience
        )

        job = {
            "scene_number": index,
            "scene_type": scene_type,
            "duration": duration,
            "motion": scene.get("motion", "slow zoom in"),
            "input_image": input_image_path,
            "output_clip": str(output_dir / f"scene_{index:02d}_{scene_type}.mp4"),
            "positive_prompt": positive_prompt,
            "negative_prompt": build_negative_prompt(),
            "notes": "Future AI video job. This can be sent to ComfyUI or Diffusers later."
        }

        jobs.append(job)

    jobs_path = output_dir / "video_prompt_jobs.json"

    with open(jobs_path, "w", encoding="utf-8") as file:
        json.dump(jobs, file, indent=2)

    return jobs


if __name__ == "__main__":
    sample_plan = {
        "hook": "Luxury in every drop",
        "headline": "Refined. Bold. Unforgettable.",
        "tone": "premium",
        "background_style": "dark black with gold glow",
        "music_mood": "cinematic elegant",
        "scenes": [
            {
                "type": "hero",
                "duration": 4,
                "motion": "slow zoom in",
                "text": "Luxury in every drop"
            },
            {
                "type": "detail",
                "duration": 4,
                "motion": "slight right pan with light sweep",
                "text": "Crafted for confidence"
            },
            {
                "type": "cta",
                "duration": 4,
                "motion": "zoom out with glow",
                "text": "Own the moment"
            }
        ]
    }

    jobs = build_video_prompt_jobs(
        plan=sample_plan,
        product_name="Luna Perfume",
        product_description="A luxury perfume with floral and woody notes for confident women.",
        style_name="luxury",
        target_audience="young professional women",
        input_image_path="output/preprocessed/product_transparent.png"
    )

    print(json.dumps(jobs, indent=2))