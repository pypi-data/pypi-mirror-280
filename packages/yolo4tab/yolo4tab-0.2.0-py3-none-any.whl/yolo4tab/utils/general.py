from pathlib import Path
from typing import Union

import gdown
import torch
from ultralytics import YOLO

from ..const import MODEL_URLS, Task


def verify_device(device: Union[str, int]) -> torch.device:
    """Verify if the device is available.

    Args:
        device (Union[str, int]): "cpu" or cuda device id (int) or cuda device name (str). If not available, use "cpu".

    Returns:
        torch.device: device
    """
    if device != "cpu" and torch.cuda.is_available():
        all_device_ids = [i for i in range(torch.cuda.device_count())]

        if isinstance(device, str):
            device = int(device)

        if device not in all_device_ids:
            print(
                f"Device {device} is not available. Available devices are {all_device_ids}. Using CPU instead."
            )
            return torch.device("cpu")
        else:
            return torch.device(f"cuda:{device}")
    return torch.device("cpu")


def verify_weight(weight_path: str, task: Task, version: str) -> str:
    """Verify the weight path. If not exists, download the default weight. If failed to load, use the default weight instead.

    Args:
        weight_path (str): Path to the weight file.
        task (Task): Task to verify the weight.
        version (str): Version of the weight.

    Returns:
        str: Verified weight path.
    """
    ## Define default weight path
    default_weight_dir = Path("~/.yolo4tab/").expanduser()
    if not default_weight_dir.exists():
        default_weight_dir.mkdir(parents=True, exist_ok=True)
    default_weight_path = default_weight_dir.joinpath(MODEL_URLS[task][version]['file'])

    ## Download the default weight if not exists
    if not default_weight_path.exists():
        print(f"Downloading the weight for task '{task}'...")
        weight_url = MODEL_URLS[task][version]['url']
        gdown.download(weight_url, str(default_weight_path), quiet=False)
        print(
            f"Downloaded the weight for task '{task}' version '{version}' at '{default_weight_path}'."
        )

    ## Verify the weight path
    if weight_path is None:
        weight_path = default_weight_path
    else:
        try:
            _ = YOLO(weight_path)
        except Exception as e:
            print(
                f"Failed to load the weight at '{weight_path}'. Error: {e}. Using default weight instead."
            )
            weight_path = default_weight_path
    return weight_path
