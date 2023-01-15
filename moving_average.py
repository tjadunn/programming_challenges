import math
from collections import deque

class MovingAverage:
    """
    Represent a moving average defined by a window of size `size`

    Example:
        ma = MovingAverage(3) -> Define window of size 3

        ma.next(1) -> 1 / 1
        ma.next(2) -> 2 + 1 / 3
        ma.next(3) -> 2 + 1 + 3 / 3
    """
    def __init__(self, size: int) -> None:
        self.size = size
        self.average_window = deque()
        self.current_index = 0

    def next(self, val: int) -> float:
        # outline
        # maintain average window in a deque
        # while its less than size calculate the average / counter
        # when greater than size calculate average / size
        # move the window righwards each time we call next

        if self.current_index == 0:
            # initialise the window
            self.average_window.append(val)
            self.current_index += 1
            return float(val)

        elif self.current_index < self.size:
            self.average_window.append(val)
            self.current_index += 1
            return sum(self.average_window) / (self.current_index)

        else:

            self.average_window.popleft()
            self.average_window.append(val)
            self.current_index += 1
            return sum(self.average_window) / self.size


def test_moving_average_next() -> None:
    moving_average = MovingAverage(3)

    result = moving_average.next(1)
    result_two = moving_average.next(10)

    assert math.isclose(result, 1.0) # be careful comparing floats here
    assert math.isclose(result_two, 5.5) # be careful comparing floats here
    assert math.isclose(moving_average.next(3), 4.666666666666667) # be careful comparing floats here
    assert math.isclose(moving_average.next(5), 6.0) # be careful comparing floats here


if __name__ == "__main__":
    test_moving_average_next()
