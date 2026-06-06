import json
import re
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


MODEL_NAME = "Qwen/Qwen3-0.6B"

tokenizer = None
model = None


def load_model():
    global tokenizer, model

    if tokenizer is not None and model is not None:
        return tokenizer, model

    print("Loading local Qwen model...")

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME,
        local_files_only=True
    )

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        dtype=torch.float32,
        local_files_only=True
    )

    model.to("cpu")
    model.eval()

    return tokenizer, model


def extract_json(text):
    """
    Extract JSON object from model output.
    This helps if the model adds extra text before/after JSON.
    """
    text = text.strip()

    # Remove markdown code fences if model uses them
    text = text.replace("```json", "").replace("```", "").strip()

    match = re.search(r"\{[\s\S]*\}", text)

    if not match:
        raise ValueError("No JSON object found in model output.")

    json_text = match.group(0)
    return json.loads(json_text)


def create_fallback_plan(product_name, product_description, style, target_audience, duration):
    """
    Backup plan if model output is not valid JSON.
    """
    scene_duration = max(1, duration // 3)

    return {
        "hook": f"Discover {product_name}",
        "headline": f"{product_name} — Made for {target_audience}",
        "tone": style,
        "background_style": "clean modern background with soft lighting",
        "music_mood": "upbeat modern",
        "scenes": [
            {
                "type": "hero",
                "duration": scene_duration,
                "motion": "slow zoom in",
                "text": f"Discover {product_name}"
            },
            {
                "type": "detail",
                "duration": scene_duration,
                "motion": "slight right pan",
                "text": "Designed to stand out"
            },
            {
                "type": "cta",
                "duration": scene_duration,
                "motion": "zoom out",
                "text": "Get yours today"
            }
        ]
    }


def generate_video_plan(
    product_name,
    product_description,
    style="premium",
    target_audience="young adults",
    duration=10
):
    tokenizer, model = load_model()

    prompt = f"""
You are a marketing video planner.

Create a short marketing video plan.

Product name: {product_name}
Product description: {product_description}
Style: {style}
Target audience: {target_audience}
Duration: {duration} seconds

Return ONLY valid JSON.
Do not explain anything.
Do not use markdown.
Do not add extra text.

The JSON must follow this exact structure:

{{
  "hook": "short powerful hook",
  "headline": "short headline",
  "tone": "video tone",
  "background_style": "visual background style",
  "music_mood": "music mood",
  "scenes": [
    {{
      "type": "hero",
      "duration": 2,
      "motion": "slow zoom in",
      "text": "text overlay"
    }},
    {{
      "type": "detail",
      "duration": 2,
      "motion": "slight right pan",
      "text": "text overlay"
    }},
    {{
      "type": "cta",
      "duration": 2,
      "motion": "zoom out with glow",
      "text": "text overlay"
    }}
  ]
}}
"""

    messages = [
        {"role": "user", "content": prompt}
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=False
    )

    inputs = tokenizer(text, return_tensors="pt").to("cpu")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=350,
            do_sample=True,
            temperature=0.4,
            pad_token_id=tokenizer.eos_token_id
        )

    response = tokenizer.decode(
        outputs[0][inputs["input_ids"].shape[-1]:],
        skip_special_tokens=True
    )

    try:
        plan = extract_json(response)
        return plan

    except Exception as error:
        print("Model did not return perfect JSON. Using fallback plan.")
        print("Error:", error)
        print("Raw model output:")
        print(response)

        return create_fallback_plan(
            product_name,
            product_description,
            style,
            target_audience,
            duration
        )


if __name__ == "__main__":
    plan = generate_video_plan(
        product_name="Luna Perfume",
        product_description="A luxury perfume with floral and woody notes for confident women.",
        style="premium elegant",
        target_audience="young professional women",
        duration=10
    )

    print(json.dumps(plan, indent=2))