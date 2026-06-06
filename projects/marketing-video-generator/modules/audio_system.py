import math
from pathlib import Path

try:
    from moviepy import AudioFileClip, CompositeAudioClip, concatenate_audioclips
except ImportError:
    from moviepy.editor import AudioFileClip, CompositeAudioClip, concatenate_audioclips


def trim_audio(audio, duration):
    if hasattr(audio, "subclipped"):
        return audio.subclipped(0, duration)
    return audio.subclip(0, duration)


def set_audio_start(audio, start_time):
    if hasattr(audio, "with_start"):
        return audio.with_start(start_time)
    return audio.set_start(start_time)


def scale_audio(audio, volume):
    if hasattr(audio, "with_volume_scaled"):
        return audio.with_volume_scaled(volume)
    return audio.volumex(volume)


def fade_audio(audio, fade_in=0.8, fade_out=1.0):
    """
    Adds fade-in and fade-out if MoviePy supports it.
    If not supported, safely returns original audio.
    """
    try:
        from moviepy.audio.fx.AudioFadeIn import AudioFadeIn
        from moviepy.audio.fx.AudioFadeOut import AudioFadeOut
        return audio.with_effects([AudioFadeIn(fade_in), AudioFadeOut(fade_out)])
    except Exception:
        pass

    try:
        import moviepy.audio.fx.all as afx
        audio = audio.fx(afx.audio_fadein, fade_in)
        audio = audio.fx(afx.audio_fadeout, fade_out)
        return audio
    except Exception:
        return audio


def normalize_audio(audio, target_peak=0.35, max_boost=2.0):
    """
    Basic volume normalization.
    Prevents very loud music and slightly boosts very quiet music.
    """
    try:
        peak = audio.max_volume()

        if hasattr(peak, "__iter__"):
            peak = max(peak)

        peak = float(peak)

        if peak <= 0:
            return audio

        factor = target_peak / peak
        factor = min(factor, max_boost)

        return scale_audio(audio, factor)

    except Exception:
        return audio


def loop_audio_to_duration(audio, duration):
    """
    If the music is shorter than the video, loop it.
    """
    if audio.duration >= duration:
        return trim_audio(audio, duration)

    repeat_count = math.ceil(duration / audio.duration)
    repeated_audio = concatenate_audioclips([audio] * repeat_count)

    return trim_audio(repeated_audio, duration)


def load_background_music(music_path, duration, volume=0.25):
    music_path = Path(music_path)

    if not music_path.exists():
        print("No background music found.")
        return None

    music = AudioFileClip(str(music_path))
    music = loop_audio_to_duration(music, duration)
    music = normalize_audio(music)
    music = scale_audio(music, volume)
    music = fade_audio(music, fade_in=1.0, fade_out=1.2)

    return music


def load_sfx(sfx_path, start_time, volume=0.35):
    sfx_path = Path(sfx_path)

    if not sfx_path.exists():
        return None

    sfx = AudioFileClip(str(sfx_path))
    sfx = scale_audio(sfx, volume)
    sfx = set_audio_start(sfx, start_time)

    return sfx


def build_audio_mix(
    video_duration,
    music_path="assets/music/background.mp3",
    sfx_dir="assets/sfx",
    transition_times=None
):
    """
    Creates final audio mix:
    background music + optional whoosh/shimmer SFX.
    """
    audio_layers = []

    music = load_background_music(music_path, video_duration)

    if music is not None:
        audio_layers.append(music)

    sfx_dir = Path(sfx_dir)
    transition_times = transition_times or []

    whoosh_path = sfx_dir / "whoosh.mp3"
    shimmer_path = sfx_dir / "shimmer.mp3"

    for index, time_point in enumerate(transition_times):
        sfx_path = whoosh_path if index % 2 == 0 else shimmer_path
        sfx = load_sfx(sfx_path, start_time=time_point, volume=0.30)

        if sfx is not None:
            audio_layers.append(sfx)

    if not audio_layers:
        return None

    final_audio = CompositeAudioClip(audio_layers)
    final_audio = trim_audio(final_audio, video_duration)

    return final_audio