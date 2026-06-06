from abc import ABC, abstractmethod
import requests

try:
    from modules.composer import compose_video
except ModuleNotFoundError:
    from composer import compose_video


COMFYUI_URL = "http://127.0.0.1:8188"


class VideoGenerator(ABC):
    name = "base"

    def is_available(self):
        return True

    @abstractmethod
    def generate_video(
        self,
        manifest_path,
        music_path,
        output_path,
        style_name="luxury",
        export_gif=False
    ):
        pass


class TemplateMotionGenerator(VideoGenerator):
    name = "template"

    def generate_video(
        self,
        manifest_path,
        music_path,
        output_path,
        style_name="luxury",
        export_gif=False
    ):
        return compose_video(
            manifest_path=manifest_path,
            music_path=music_path,
            output_path=output_path,
            export_gif=export_gif,
            style_name=style_name
        )


class ComfyUIGenerator(VideoGenerator):
    name = "comfyui"

    def is_available(self):
        try:
            response = requests.get(f"{COMFYUI_URL}/system_stats", timeout=3)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False

    def generate_video(
        self,
        manifest_path,
        music_path,
        output_path,
        style_name="luxury",
        export_gif=False
    ):
        raise NotImplementedError(
            "ComfyUI backend is prepared but not fully connected yet. "
            "Use template backend for now."
        )


class DiffusersGenerator(VideoGenerator):
    name = "diffusers"

    def is_available(self):
        return False

    def generate_video(
        self,
        manifest_path,
        music_path,
        output_path,
        style_name="luxury",
        export_gif=False
    ):
        raise NotImplementedError(
            "Diffusers video backend is not enabled yet."
        )


def get_video_generator(backend_name="template"):
    backends = {
        "template": TemplateMotionGenerator,
        "comfyui": ComfyUIGenerator,
        "diffusers": DiffusersGenerator
    }

    backend_class = backends.get(backend_name, TemplateMotionGenerator)
    return backend_class()


def generate_final_video(
    backend_name="template",
    manifest_path="output/shots/shot_manifest.json",
    music_path="assets/music/background.mp3",
    output_path="output/final_video.mp4",
    style_name="luxury",
    export_gif=False
):
    generator = get_video_generator(backend_name)

    if not generator.is_available():
        print(f"{backend_name} backend is not available. Falling back to template backend.")
        generator = TemplateMotionGenerator()

    return generator.generate_video(
        manifest_path=manifest_path,
        music_path=music_path,
        output_path=output_path,
        style_name=style_name,
        export_gif=export_gif
    )


if __name__ == "__main__":
    print("Testing video generator backends...")

    template = get_video_generator("template")
    comfyui = get_video_generator("comfyui")
    diffusers = get_video_generator("diffusers")

    print("Template available:", template.is_available())
    print("ComfyUI available:", comfyui.is_available())
    print("Diffusers available:", diffusers.is_available())