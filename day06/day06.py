from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day06/input.txt"
SAMPLE_DATA = "day06/sample.txt"


def day6() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    return res


if __name__ == '__main__':
    result = day6()
    print(f'Day 6 Part 1: {result.p1}')
    print(f'Day 6 Part 2: {result.p2}')