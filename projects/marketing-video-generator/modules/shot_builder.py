import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter


try:
    from modules.utils import load_styles
except ModuleNotFoundError:
    from utils import load_styles


RESAMPLE = Image.Resampling.LANCZOS


def hex_to_rgb(hex_color):
    hex_color = hex_color.replace("#", "")
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def get_font(size=60, bold=False):
    font_paths = [
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
    ]

    for path in font_paths:
        if Path(path).exists():
            return ImageFont.truetype(path, size)

    return ImageFont.load_default()


def wrap_text(draw, text, font, max_width):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + " " + word if current_line else word
        bbox = draw.textbbox((0, 0), test_line, font=font)
        line_width = bbox[2] - bbox[0]

        if line_width <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return lines


def draw_center_text(image, text, y, font_size, color, max_width=900, bold=True):
    draw = ImageDraw.Draw(image)
    font = get_font(font_size, bold=bold)
    lines = wrap_text(draw, text, font, max_width)

    line_height = font_size + 12
    total_height = len(lines) * line_height
    start_y = y - total_height // 2

    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        x = (image.width - text_width) // 2
        draw.text((x, start_y), line, font=font, fill=color)
        start_y += line_height


def draw_left_text(image, text, x, y, font_size, color, max_width=430, bold=True):
    draw = ImageDraw.Draw(image)
    font = get_font(font_size, bold=bold)
    lines = wrap_text(draw, text, font, max_width)

    line_height = font_size + 12

    for line in lines:
        draw.text((x, y), line, font=font, fill=color)
        y += line_height


def create_background(size, style_config):
    width, height = size
    colors = style_config["colors"]

    base = hex_to_rgb(colors[0])
    accent = hex_to_rgb(colors[1])

    background = Image.new("RGB", size, base)
    draw = ImageDraw.Draw(background)

    for y in range(height):
        ratio = y / height
        r = int(base[0] * (1 - ratio) + accent[0] * ratio * 0.35)
        g = int(base[1] * (1 - ratio) + accent[1] * ratio * 0.35)
        b = int(base[2] * (1 - ratio) + accent[2] * ratio * 0.35)
        draw.line((0, y, width, y), fill=(r, g, b))

    glow = Image.new("RGBA", size, (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)

    glow_draw.ellipse(
        (width // 2 - 420, height // 2 - 420, width // 2 + 420, height // 2 + 420),
        fill=(accent[0], accent[1], accent[2], 80)
    )

    glow = glow.filter(ImageFilter.GaussianBlur(120))

    background = background.convert("RGBA")
    background.alpha_composite(glow)

    return background


def add_light_sweep(image, accent_color):
    accent = hex_to_rgb(accent_color)
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    draw.polygon(
        [
            (image.width * 0.15, 0),
            (image.width * 0.32, 0),
            (image.width * 0.82, image.height),
            (image.width * 0.65, image.height)
        ],
        fill=(accent[0], accent[1], accent[2], 45)
    )

    overlay = overlay.filter(ImageFilter.GaussianBlur(25))
    image.alpha_composite(overlay)

    return image


def resize_product(product, max_height):
    product = product.copy()
    scale = max_height / product.height
    new_width = int(product.width * scale)
    new_height = int(product.height * scale)
    return product.resize((new_width, new_height), RESAMPLE)


def paste_product(image, product, center_x, center_y, shadow=True):
    product = product.convert("RGBA")

    x = int(center_x - product.width // 2)
    y = int(center_y - product.height // 2)

    if shadow:
        alpha = product.getchannel("A")
        shadow_img = Image.new("RGBA", product.size, (0, 0, 0, 120))
        shadow_img.putalpha(alpha.filter(ImageFilter.GaussianBlur(18)))

        image.alpha_composite(shadow_img, (x + 25, y + 35))

    image.alpha_composite(product, (x, y))

    return image


def create_scene(scene, scene_index, product_image, style_config, output_dir, canvas_size=(1080, 1920)):
    scene_type = scene.get("type", "hero")
    text = scene.get("text", "")
    motion = scene.get("motion", "slow_zoom_in")
    duration = scene.get("duration", 2)

    text_color = style_config.get("text_color", "#FFFFFF")
    accent_color = style_config.get("accent_color", "#D4AF37")

    image = create_background(canvas_size, style_config)

    if scene_type == "hero":
        product = resize_product(product_image, max_height=1050)
        image = paste_product(image, product, canvas_size[0] // 2, 1080)
        draw_center_text(image, text, y=260, font_size=70, color=text_color, bold=True)

    elif scene_type == "detail":
        product = resize_product(product_image, max_height=1250)
        image = paste_product(image, product, int(canvas_size[0] * 0.67), 1050)
        image = add_light_sweep(image, accent_color)
        draw_left_text(image, text, x=80, y=360, font_size=58, color=text_color, bold=True)

    elif scene_type == "cta":
        product = resize_product(product_image, max_height=900)
        image = paste_product(image, product, canvas_size[0] // 2, 850)
        draw_center_text(image, text, y=1510, font_size=72, color=text_color, bold=True)

        draw = ImageDraw.Draw(image)
        button_w, button_h = 620, 95
        button_x = (canvas_size[0] - button_w) // 2
        button_y = 1630

        draw.rounded_rectangle(
            (button_x, button_y, button_x + button_w, button_y + button_h),
            radius=35,
            outline=accent_color,
            width=4
        )

        draw_center_text(image, "SHOP NOW", y=button_y + 48, font_size=42, color=accent_color, bold=True)

    else:
        product = resize_product(product_image, max_height=1000)
        image = paste_product(image, product, canvas_size[0] // 2, 1000)
        draw_center_text(image, text, y=280, font_size=64, color=text_color, bold=True)

    output_path = output_dir / f"scene_{scene_index:02d}_{scene_type}.png"
    image.save(output_path)

    return {
        "scene_number": scene_index,
        "type": scene_type,
        "duration": duration,
        "motion": motion,
        "text": text,
        "image_path": str(output_path)
    }


def build_shots(plan, style_name="luxury", product_image_path="output/preprocessed/product_transparent.png"):
    output_dir = Path("output/shots")
    output_dir.mkdir(parents=True, exist_ok=True)

    styles = load_styles()
    style_config = styles.get(style_name, styles["luxury"])

    product_image = Image.open(product_image_path).convert("RGBA")

    scenes = plan.get("scenes", [])

    shot_manifest = []

    for index, scene in enumerate(scenes, start=1):
        shot = create_scene(
            scene=scene,
            scene_index=index,
            product_image=product_image,
            style_config=style_config,
            output_dir=output_dir
        )

        shot_manifest.append(shot)

    manifest_path = output_dir / "shot_manifest.json"

    with open(manifest_path, "w", encoding="utf-8") as file:
        json.dump(shot_manifest, file, indent=2)

    return shot_manifest


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
                "duration": 2,
                "motion": "slow_zoom_in",
                "text": "Luxury in every drop"
            },
            {
                "type": "detail",
                "duration": 2,
                "motion": "light_sweep",
                "text": "Crafted for radiant confidence"
            },
            {
                "type": "cta",
                "duration": 2,
                "motion": "zoom_out_with_glow",
                "text": "Own the moment"
            }
        ]
    }

    shots = build_shots(
        plan=sample_plan,
        style_name="luxury",
        product_image_path="output/preprocessed/product_transparent.png"
    )

    print("Shot images created successfully.")
    print(json.dumps(shots, indent=2))