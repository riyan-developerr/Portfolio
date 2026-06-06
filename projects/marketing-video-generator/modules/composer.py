import json
import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

try:
    from moviepy import VideoClip, concatenate_videoclips
except ImportError:
    from moviepy.editor import VideoClip, concatenate_videoclips

try:
    from modules.utils import load_styles
except ModuleNotFoundError:
    from utils import load_styles

try:
    from modules.audio_system import build_audio_mix
except ModuleNotFoundError:
    from audio_system import build_audio_mix


FPS = 30
VIDEO_SIZE = (1080, 1920)
CROSSFADE_DURATION = 0.35


def set_clip_fps(clip, fps):
    if hasattr(clip, "with_fps"):
        return clip.with_fps(fps)
    return clip.set_fps(fps)


def set_clip_audio(clip, audio):
    if hasattr(clip, "with_audio"):
        return clip.with_audio(audio)
    return clip.set_audio(audio)


def hex_to_rgb(hex_color):
    hex_color = hex_color.replace("#", "")
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def load_shot_manifest(manifest_path="output/shots/shot_manifest.json"):
    with open(manifest_path, "r", encoding="utf-8") as file:
        return json.load(file)


def create_vignette_mask(size, strength=0.28):
    width, height = size

    x = np.linspace(-1, 1, width)
    y = np.linspace(-1, 1, height)
    xx, yy = np.meshgrid(x, y)

    dist = np.sqrt(xx**2 + yy**2)
    mask = np.clip((dist - 0.35) / 0.80, 0, 1)
    mask = (mask ** 1.8) * strength

    return mask[..., None]


VIGNETTE_MASK = create_vignette_mask(VIDEO_SIZE)


def apply_vignette(frame_np):
    frame = frame_np.astype(np.float32)
    frame *= (1.0 - VIGNETTE_MASK)
    return np.clip(frame, 0, 255).astype(np.uint8)


def create_particles(count=18, seed=42):
    rng = np.random.default_rng(seed)
    particles = []

    for _ in range(count):
        particles.append({
            "x": float(rng.uniform(0.08, 0.92)),
            "y": float(rng.uniform(0.15, 0.95)),
            "radius": int(rng.integers(2, 6)),
            "alpha": int(rng.integers(18, 50)),
            "speed": float(rng.uniform(0.05, 0.18)),
            "drift": float(rng.uniform(12, 40)),
            "phase": float(rng.uniform(0, math.pi * 2))
        })

    return particles


def apply_motion(image, progress, motion, scene_type):
    base_w, base_h = VIDEO_SIZE

    if "zoom_out" in motion:
        zoom = 1.08 - (0.08 * progress)
    else:
        zoom = 1.00 + (0.08 * progress)

    new_w = int(base_w * zoom)
    new_h = int(base_h * zoom)

    resized = image.resize((new_w, new_h), Image.Resampling.LANCZOS)

    left = (new_w - base_w) // 2
    top = (new_h - base_h) // 2

    drift_x = int(18 * math.sin(progress * math.pi))
    drift_y = int(10 * math.sin(progress * math.pi * 0.8))

    if scene_type == "detail":
        drift_x += int(15 * progress)

    if "right" in motion or "pan" in motion:
        drift_x += int(24 * progress)

    if "left" in motion:
        drift_x -= int(24 * progress)

    left += drift_x
    top += drift_y

    left = max(0, min(left, new_w - base_w))
    top = max(0, min(top, new_h - base_h))

    return resized.crop((left, top, left + base_w, top + base_h)).convert("RGBA")


def apply_glow(frame, progress, accent_color, scene_type):
    accent = hex_to_rgb(accent_color)

    overlay = Image.new("RGBA", frame.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    if scene_type == "detail":
        center_x, center_y = int(frame.width * 0.68), 1060
        radius = 320
    elif scene_type == "cta":
        center_x, center_y = frame.width // 2, 860
        radius = 280
    else:
        center_x, center_y = frame.width // 2, 1080
        radius = 360

    pulse = 0.5 + 0.5 * math.sin(progress * math.pi * 2)
    alpha = int(26 + pulse * 28)

    draw.ellipse(
        (
            center_x - radius,
            center_y - radius,
            center_x + radius,
            center_y + radius
        ),
        fill=(accent[0], accent[1], accent[2], alpha)
    )

    overlay = overlay.filter(ImageFilter.GaussianBlur(90))
    frame.alpha_composite(overlay)

    return frame


def apply_light_sweep(frame, progress, accent_color):
    accent = hex_to_rgb(accent_color)

    overlay = Image.new("RGBA", frame.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    x_pos = int((-0.35 + progress * 1.6) * frame.width)

    draw.polygon(
        [
            (x_pos, 0),
            (x_pos + 140, 0),
            (x_pos + 520, frame.height),
            (x_pos + 380, frame.height)
        ],
        fill=(accent[0], accent[1], accent[2], 34)
    )

    overlay = overlay.filter(ImageFilter.GaussianBlur(18))
    frame.alpha_composite(overlay)

    return frame


def apply_particles(frame, progress, particles):
    overlay = Image.new("RGBA", frame.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    for p in particles:
        x = int(
            p["x"] * frame.width
            + math.sin(progress * math.pi * 2 + p["phase"]) * p["drift"]
        )

        y = int(((p["y"] - progress * p["speed"]) % 1.0) * frame.height)

        r = p["radius"]

        draw.ellipse(
            (x - r, y - r, x + r, y + r),
            fill=(255, 255, 255, p["alpha"])
        )

    overlay = overlay.filter(ImageFilter.GaussianBlur(1.8))
    frame.alpha_composite(overlay)

    return frame


def apply_fade(frame, t, duration, fade_duration=0.35):
    if t < fade_duration:
        alpha = t / fade_duration
    elif t > duration - fade_duration:
        alpha = (duration - t) / fade_duration
    else:
        alpha = 1.0

    alpha = max(0, min(1, alpha))

    black = Image.new("RGB", frame.size, (0, 0, 0))
    return Image.blend(black, frame.convert("RGB"), alpha)


def create_animated_clip(image_path, duration, motion, scene_type, style_config):
    image = Image.open(image_path).convert("RGB")
    image = image.resize(VIDEO_SIZE, Image.Resampling.LANCZOS)

    accent_color = style_config.get("accent_color", "#D4AF37")
    particles = create_particles(count=18, seed=42)

    def make_frame(t):
        progress = t / duration if duration > 0 else 0

        frame = apply_motion(image, progress, motion, scene_type)
        frame = apply_glow(frame, progress, accent_color, scene_type)
        frame = apply_particles(frame, progress, particles)

        if "sweep" in motion or scene_type == "detail":
            frame = apply_light_sweep(frame, progress, accent_color)

        frame = apply_fade(frame, t, duration)

        frame_np = np.array(frame)
        frame_np = apply_vignette(frame_np)

        return frame_np

    try:
        clip = VideoClip(make_frame, duration=duration)
    except TypeError:
        clip = VideoClip(frame_function=make_frame, duration=duration)

    return set_clip_fps(clip, FPS)


def calculate_transition_times(shots):
    transition_times = []
    current_time = 0

    for shot in shots[:-1]:
        current_time += shot.get("duration", 2) - CROSSFADE_DURATION
        transition_times.append(max(0, current_time))

    return transition_times


def compose_video(
    manifest_path="output/shots/shot_manifest.json",
    music_path="assets/music/background.mp3",
    output_path="output/final_video.mp4",
    export_gif=False,
    style_name="luxury"
):
    shots = load_shot_manifest(manifest_path)

    styles = load_styles()
    style_config = styles.get(style_name, styles["luxury"])

    clips = []

    for shot in shots:
        image_path = shot["image_path"]
        duration = shot.get("duration", 2)
        motion = shot.get("motion", "slow_zoom_in")
        scene_type = shot.get("type", "hero")

        clip = create_animated_clip(
            image_path=image_path,
            duration=duration,
            motion=motion,
            scene_type=scene_type,
            style_config=style_config
        )

        clips.append(clip)

    final_video = concatenate_videoclips(
        clips,
        method="compose",
        padding=-CROSSFADE_DURATION
    )

    transition_times = calculate_transition_times(shots)

    audio = build_audio_mix(
        video_duration=final_video.duration,
        music_path=music_path,
        sfx_dir="assets/sfx",
        transition_times=transition_times
    )

    if audio is not None:
        final_video = set_clip_audio(final_video, audio)
    else:
        print("No audio found. Exporting silent video.")

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    final_video.write_videofile(
        str(output_path),
        fps=FPS,
        codec="libx264",
        audio_codec="aac"
    )

    if export_gif:
        gif_path = output_path.with_suffix(".gif")
        final_video.write_gif(str(gif_path), fps=12)
        print(f"GIF exported: {gif_path}")

    print(f"MP4 exported: {output_path}")

    return str(output_path)


if __name__ == "__main__":
    compose_video(
        manifest_path="output/shots/shot_manifest.json",
        music_path="assets/music/background.mp3",
        output_path="output/final_video.mp4",
        export_gif=False,
        style_name="luxury"
    )