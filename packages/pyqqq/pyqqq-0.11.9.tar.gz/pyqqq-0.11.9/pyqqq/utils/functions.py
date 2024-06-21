import time
import threading


def throttle(func, wait):
    """
    주어진 함수를 쓰로틀 처리하여 일정 시간(`wait` 초) 동안 한 번만 함수를
    실행하도록 합니다.

    Args:
        func (callable): 쓰로틀 처리할 함수.
        wait (float): 실행 주기 시간(초).

    Returns:
        callable: 쓰로틀 처리된 함수.

    Examples:
        >>> def print_message():
        ...     print("함수가 실행되었습니다.")
        >>> throttled_function = throttle(print_message, 2)
        >>> throttled_function()  # 즉시 실행됨.
        >>> time.sleep(1)
        >>> throttled_function()  # 2초가 경과하지 않았으므로 무시됨.
        >>> time.sleep(2)
        >>> throttled_function()  # 2초가 경과했으므로 실행됨.
    """

    def throttled(*args, **kwargs):
        now = time.time()
        if not hasattr(throttled, "last_call") or now - throttled.last_call >= wait:
            throttled.last_call = now
            func(*args, **kwargs)

    return throttled


def debounce(func, wait):
    """
    주어진 함수를 디바운스 처리하여 마지막 호출 후 특정 시간(`wait` 초)이
    경과된 이후에 함수를 실행합니다.

    Args:
        func (callable): 디바운스 처리할 함수.
        wait (float): 지연 시간(초).

    Returns:
        callable: 디바운스 처리된 함수.

    Examples:
        >>> def print_message():
        ...     print("함수가 실행되었습니다.")
        >>> debounced_function = debounce(print_message, 2)
        >>> debounced_function()  # 2초 후에 실행되며, 그 기간 내에 다시 호출되지 않으면 실행됨.
    """

    def debounced(*args, **kwargs):
        def call_it():
            debounced.last_call = time.time()
            func(*args, **kwargs)

        if hasattr(debounced, "timer"):
            debounced.timer.cancel()

        debounced.timer = threading.Timer(wait, call_it)
        debounced.timer.start()

    return debounced
