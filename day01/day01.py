from shared.types import Result
from shared.input import get_input
from collections import Counter

INPUT_DATA = "day01/input.txt"
SAMPLE_DATA = "day01/sample.txt"

def parse_input(lines: list[str]) -> tuple[list, list]:
    first, second = [], []
    for line in lines:
        vals = line.split('  ')
        first.append(int(vals[0]))
        second.append(int(vals[1]))
    return first, second
    
def get_distance_sum(first: list[int], second: list[int]) -> int:
    first = sorted(first)
    second = sorted(second)

    dist = 0
    for i in range(len(first)):
        print(first[i], ':', second[i])
        dist += abs(first[i] - second[i])
    return dist

def get_similarity_score(first: list[int], second: list[int]) -> int:
    counts = Counter(second)
    score = 0
    for n in first:
        score += n * counts[n]
    return score


def day1() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    first, second = parse_input(input)
    res.p1 = get_distance_sum(first, second)
    res.p2 = get_similarity_score(first, second)
    return res

if __name__ == '__main__':
    result = day1()
    print(f'Day 1 Part 1: {result.p1}')
    print(f'Day 1 Part 2: {result.p2}')