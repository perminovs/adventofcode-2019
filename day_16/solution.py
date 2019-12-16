from itertools import chain, cycle
from typing import Iterator

from day_16.data import RAW

BASE_PATTERN = [0, 1, 0, -1]
REPEATS = 100


def get_pattern_for_round(iteration: int) -> Iterator[int]:
    for _ in range(iteration - 1):
        yield BASE_PATTERN[0]

    for num in chain(BASE_PATTERN[1:], cycle(BASE_PATTERN)):
        for _ in range(iteration):
            yield num


def phase(digits: str, repeat: int) -> str:
    for _ in range(repeat):
        digits = _phase(digits)
    return digits


def _phase(digits: str) -> str:
    def digit_generator():
        return (int(i) for i in str(digits))

    new_digits = []
    for idx, digit in enumerate(digit_generator(), start=1):
        row_sum = []
        for p, d in zip(digit_generator(), get_pattern_for_round(idx)):
            row_sum.append(p * d)
        new_digits.append(str(sum(row_sum))[-1])
    return ''.join(new_digits)


def main_p1():
    result = phase(RAW, REPEATS)
    print(result[:8])


if __name__ == '__main__':
    main_p1()
