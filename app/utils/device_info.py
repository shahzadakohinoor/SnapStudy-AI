"""Hardware capability diagnostics."""

import os
import platform
import psutil


def get_device_info() -> dict:
    cpu_count = os.cpu_count() or 1
    ram_gb = round(psutil.virtual_memory().total / (1024**3), 2)
    os_name = f"{platform.system()} {platform.release()}"

    gpu_available = False
    gpu_name = "None"
    try:
        import torch

        if torch.cuda.is_available():
            gpu_available = True
            gpu_name = torch.cuda.get_device_name(0)
    except ImportError:
        pass

    return {
        "os": os_name,
        "cpu_threads": cpu_count,
        "ram_gb": ram_gb,
        "gpu_available": gpu_available,
        "gpu_name": gpu_name,
    }