"""Project root runner."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.utils.device_info import get_device_info
from app.main import main

if __name__ == "__main__":
    device = get_device_info()
    print(f"[*] System: {device['os']} | CPU Cores: {device['cpu_threads']}")
    main()