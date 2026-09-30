"""Execution timers and telemetry helpers."""

import time
from functools import wraps


def timed_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"[{func.__name__}] completed in {duration:.4f}s")
        return result

    return wrapper