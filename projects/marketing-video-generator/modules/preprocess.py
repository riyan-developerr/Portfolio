import os
from pathlib import Path
from PIL import Image, ImageFilter
from rembg import remove


# Store rembg AI model on D drive, not C drive
os.environ.setdefault("U2NET_HOME", r"D:\ai_models\rembg")


def load_image(image_path):
    image = Image.open(image_path).convert("RGBA")
    return image


def remove_background(image):
    """
    Removes image background and returns transparent PNG image.
    """
    clean_image = remove(image)
    return clean_image.convert("RGBA")


def crop_transparent_edges(image):
    """
    Crops empty transparent space around the product.
    """
    alpha = image.getchannel("A")
    bbox = alpha.getbbox()

    if bbox:
        return image.crop(bbox)

    return image


def upscale_if_small(image, min_size=900):
    """
    Upscales product if it is too small.
    """
    width, height = image.size
    largest_side = max(width, height)

    if largest_side >= min_size:
        return image

    scale = min_size / largest_side
    new_size = (int(width * scale), int(height * scale))

    return image.resize(new_size, Image.LANCZOS)


def sharpen_image(image):
    """
    Slightly sharpens product image.
    """
    return image.filter(
        ImageFilter.UnsharpMask(radius=1.5, percent=120, threshold=3)
    )


def place_on_canvas(image, canvas_size, padding=80):
    """
    Places product in the center of a transparent canvas.
    """
    canvas_width, canvas_height = canvas_size

    max_width = canvas_width - padding * 2
    max_height = canvas_height - padding * 2

    image_copy = image.copy()
    image_copy.thumbnail((max_width, max_height), Image.LANCZOS)

    canvas = Image.new("RGBA", canvas_size, (0, 0, 0, 0))

    x = (canvas_width - image_copy.width) // 2
    y = (canvas_height - image_copy.height) // 2

    canvas.paste(image_copy, (x, y), image_copy)

    return canvas


def process_product_image(input_path, output_dir="output/preprocessed"):
    """
    Main function:
    input product image -> clean transparent images for video generation
    """
    input_path = Path(input_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    image = load_image(input_path)

    transparent = remove_background(image)
    transparent = crop_transparent_edges(transparent)
    transparent = upscale_if_small(transparent)
    transparent = sharpen_image(transparent)

    transparent_path = output_dir / "product_transparent.png"
    hero_path = output_dir / "product_hero.png"
    thumbnail_path = output_dir / "product_thumbnail.png"
    background_ready_path = output_dir / "product_background_ready.png"

    # 1. Clean transparent product
    transparent.save(transparent_path)

    # 2. Hero image - square for main product scenes
    hero = place_on_canvas(transparent, (1080, 1080), padding=120)
    hero.save(hero_path)

    # 3. Thumbnail image - small preview
    thumbnail = place_on_canvas(transparent, (512, 512), padding=60)
    thumbnail.save(thumbnail_path)

    # 4. Background-ready image - 16:9 video canvas
    background_ready = place_on_canvas(transparent, (1920, 1080), padding=160)
    background_ready.save(background_ready_path)

    return {
        "transparent_product": str(transparent_path),
        "hero_image": str(hero_path),
        "thumbnail": str(thumbnail_path),
        "background_ready": str(background_ready_path),
    }


if __name__ == "__main__":
    test_image = "input/product.jpg"

    outputs = process_product_image(test_image)

    print("Image preprocessing completed.")
    print(outputs)