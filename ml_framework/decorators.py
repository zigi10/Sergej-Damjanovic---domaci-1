import time
from functools import wraps


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = round(end - start, 4)

        if isinstance(result, dict):
            result["execution_time"] = elapsed
        else:
            result = {"result": result, "execution_time": elapsed}

        return result

    return wrapper


class TimeDecorator:
    def __init__(self, experiment):
        self._experiment = experiment
        self._execution_time = 0.0

    @property
    def execution_time(self):
        return self._execution_time

    def run(self, X, y, **kwargs):
        start = time.perf_counter()
        result = self._experiment.run(X, y, **kwargs)
        end = time.perf_counter()
        self._execution_time = round(end - start, 4)

        if isinstance(result, dict):
            result["execution_time"] = self._execution_time
        else:
            result = {"result": result, "execution_time": self._execution_time}

        return result

    def __getattr__(self, name):
        return getattr(self._experiment, name)