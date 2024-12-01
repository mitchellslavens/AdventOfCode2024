from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day09/input.txt"
SAMPLE_DATA = "day09/sample.txt"


def day9() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    return res


if __name__ == '__main__':
    result = day9()
    print(f'Day 9 Part 1: {result.p1}')
    print(f'Day 9 Part 2: {result.p2}')