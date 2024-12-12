from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day02/input.txt"
SAMPLE_DATA = "day02/sample.txt"


def day2() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    score = 0
    score2 = 0
    for report in input:
        score += 1 if report_is_safe(list(map(int, report.split(' ')))) else 0
        score2 += 1 if safe_with_one_error(list(map(int, report.split(' ')))) else 0
    res.p1 = score
    res.p2 = score2
    return res

# Since the lists are so short, just try removing each element
def safe_with_one_error(report: list[int]) -> bool:
    for i in range(len(report)):
        if report_is_safe(report[:i] + report[i + 1:]):
            return True
    return False

def report_is_safe(report: list[int]) -> bool:
    if len(report) < 2:
        return True
    first, second = 0, 1
    increasing = report[first] < report[second]
    while second < len(report):
        if increasing and report[first] >= report[second]:
            return False
        elif not increasing and report[second] >= report[first]:
            return False
        if abs(report[first] - report[second]) > 3:
            return False
        first += 1
        second += 1
    return True


if __name__ == '__main__':
    result = day2()
    print(f'Day 2 Part 1: {result.p1}')
    print(f'Day 2 Part 2: {result.p2}')