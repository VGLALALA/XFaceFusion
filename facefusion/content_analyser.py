from functools import lru_cache

from facefusion.typing import DownloadScope, Fps, InferencePool, ModelOptions, ModelSet, VisionFrame

# Stub implementation with NSFW functionality removed.

@lru_cache(maxsize=None)
def create_static_model_set(download_scope: DownloadScope) -> ModelSet:
    return {}

def get_inference_pool() -> InferencePool:
    return {}

def clear_inference_pool() -> None:
    pass

def get_model_options() -> ModelOptions:
    return {}

def pre_check() -> bool:
    return True

def analyse_stream(vision_frame: VisionFrame, video_fps: Fps) -> bool:
    return False

def analyse_frame(vision_frame: VisionFrame) -> bool:
    return False

def forward(vision_frame: VisionFrame) -> float:
    return 0.0

def prepare_frame(vision_frame: VisionFrame) -> VisionFrame:
    return vision_frame

@lru_cache(maxsize=None)
def analyse_image(image_path: str) -> bool:
    return False

@lru_cache(maxsize=None)
def analyse_video(video_path: str, trim_frame_start: int, trim_frame_end: int) -> bool:
    return False
