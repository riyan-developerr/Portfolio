import json

import gradio as gr

from modules.pipeline import run_full_pipeline
from modules.utils import load_styles
from modules.scorer import update_score, ensure_runs_csv


def run_pipeline(
    image_path,
    product_name,
    product_type,
    product_description,
    style_name,
    target_audience,
    duration,
    output_format
):
    if not image_path:
        return None, None, "Please upload a product image.", "", "", ""

    if not product_name.strip():
        return None, None, "Please enter a product name.", "", "", ""

    if not product_description.strip():
        return None, None, "Please enter a product description.", "", "", ""

    result = run_full_pipeline(
        image_path=image_path,
        product_name=product_name,
        product_type=product_type,
        product_description=product_description,
        style_name=style_name,
        target_audience=target_audience,
        duration=duration,
        output_format=output_format,
        backend_name="template",
        prepare_ai_prompts=True
    )

    if not result["success"]:
        return (
            None,
            None,
            result["message"],
            "",
            result["run_id"],
            result["run_id"]
        )

    status = (
        f"{result['message']}\n"
        f"Run ID: {result['run_id']}\n"
        f"Preview video: {result['preview_video']}\n"
        f"Download file: {result['download_file']}\n"
        f"AI prompt jobs: {result['ai_jobs_path']}"
    )

    return (
        result["preview_video"],
        result["download_file"],
        status,
        json.dumps(result["plan"], indent=2),
        result["run_id"],
        result["run_id"]
    )


def save_score(
    run_id,
    product_visibility,
    text_readability,
    motion_smoothness,
    style_match,
    premium_look,
    overall_quality,
    notes
):
    if not run_id:
        return "No run ID found. Generate a video first."

    scores = {
        "product_visibility": product_visibility,
        "text_readability": text_readability,
        "motion_smoothness": motion_smoothness,
        "style_match": style_match,
        "premium_look": premium_look,
        "overall_quality": overall_quality
    }

    success, message = update_score(
        run_id=run_id,
        scores=scores,
        notes=notes
    )

    return message


styles = list(load_styles().keys())

with gr.Blocks(title="Marketing Video Generator V1") as demo:
    run_id_state = gr.State("")

    gr.Markdown("# Marketing Video Generator V1")
    gr.Markdown(
        "Upload a product image, generate a short marketing video, "
        "download the output, view the scene plan, and score the result."
    )

    with gr.Row():
        with gr.Column():
            image_input = gr.Image(
                type="filepath",
                label="Upload Product Image"
            )

            product_name_input = gr.Textbox(
                label="Product Name",
                placeholder="e.g. Luna Perfume"
            )

            product_type_input = gr.Textbox(
                label="Product Type",
                value="perfume",
                placeholder="e.g. perfume, skincare, tech gadget, fashion item"
            )

            product_description_input = gr.Textbox(
                label="Product Description",
                lines=5,
                placeholder="Describe the product, benefits, and overall feel..."
            )

            style_input = gr.Dropdown(
                choices=styles,
                value="luxury",
                label="Style"
            )

            target_audience_input = gr.Textbox(
                label="Target Audience",
                value="young professional women"
            )

            duration_input = gr.Slider(
                minimum=6,
                maximum=15,
                step=1,
                value=12,
                label="Duration (seconds)"
            )

            output_format_input = gr.Dropdown(
                choices=["MP4", "GIF"],
                value="MP4",
                label="Output Format"
            )

            generate_button = gr.Button("Generate Video")

        with gr.Column():
            video_output = gr.Video(label="Preview Video")
            download_output = gr.File(label="Download Output File")
            status_output = gr.Textbox(label="Status")
            run_id_output = gr.Textbox(label="Run ID")
            plan_output = gr.Code(
                label="Generated Scene Plan JSON",
                language="json"
            )

    gr.Markdown("## Score This Output")
    gr.Markdown("After watching the video, rate it from 1 to 5.")

    with gr.Row():
        product_visibility_score = gr.Slider(
            1, 5, step=1, value=3, label="Product Visibility"
        )
        text_readability_score = gr.Slider(
            1, 5, step=1, value=3, label="Text Readability"
        )
        motion_smoothness_score = gr.Slider(
            1, 5, step=1, value=3, label="Motion Smoothness"
        )

    with gr.Row():
        style_match_score = gr.Slider(
            1, 5, step=1, value=3, label="Style Match"
        )
        premium_look_score = gr.Slider(
            1, 5, step=1, value=3, label="Premium Look"
        )
        overall_quality_score = gr.Slider(
            1, 5, step=1, value=3, label="Overall Quality"
        )

    notes_input = gr.Textbox(
        label="Notes",
        lines=3,
        placeholder="What looked good? What should improve?"
    )

    save_score_button = gr.Button("Save Score")
    score_status_output = gr.Textbox(label="Score Save Status")

    generate_button.click(
        fn=run_pipeline,
        inputs=[
            image_input,
            product_name_input,
            product_type_input,
            product_description_input,
            style_input,
            target_audience_input,
            duration_input,
            output_format_input
        ],
        outputs=[
            video_output,
            download_output,
            status_output,
            plan_output,
            run_id_output,
            run_id_state
        ]
    )

    save_score_button.click(
        fn=save_score,
        inputs=[
            run_id_state,
            product_visibility_score,
            text_readability_score,
            motion_smoothness_score,
            style_match_score,
            premium_look_score,
            overall_quality_score,
            notes_input
        ],
        outputs=[
            score_status_output
        ]
    )


if __name__ == "__main__":
    ensure_runs_csv()
    demo.launch()