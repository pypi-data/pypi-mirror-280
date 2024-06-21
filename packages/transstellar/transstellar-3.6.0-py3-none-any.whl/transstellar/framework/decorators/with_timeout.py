import datetime
from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T")


def with_timeout(timeout: int = 10):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if "timeout" in kwargs:
                remaining_timeout = kwargs["timeout"]
            else:
                remaining_timeout = timeout

            start_time = datetime.datetime.now()

            try:
                return func(self, *args, **kwargs)
            except Exception as e:
                end_time = datetime.datetime.now()
                time_difference = (end_time - start_time).total_seconds()
                new_remaining_timeout = remaining_timeout - time_difference

                if new_remaining_timeout > 0:
                    kwargs["timeout"] = new_remaining_timeout
                    return wrapper(self, *args, **kwargs)
                else:
                    raise e

        return wrapper

    return decorator
