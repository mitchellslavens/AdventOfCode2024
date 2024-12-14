from shared.types import Result
from shared.input import get_input
import re

INPUT_DATA = "day03/input.txt"
SAMPLE_DATA = "day03/sample.txt"

def day3() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    score = 0
    score2 = 0
    score += sum(num1 * num2 for num1, num2 in find_matches(''.join(input))) 
    score2 += sum(num1 * num2 for num1, num2 in find_matches(trim_string_between_ops(''.join(input))))
    res.p1 = score
    res.p2 = score2
    return res    

# Just remove portions of the string that exist between a "don't" and the next "do".
def trim_string_between_ops(mem_string: str) -> str:
    i = 0
    op_toggle = True
    res = []
    while i < len(mem_string):
        if mem_string[i:i+4] == "do()":
            res.append(mem_string[i:i+4])
            i += 4
            op_toggle = True
        elif mem_string[i:i+7] == "don't()":
           res.append(mem_string[i:i+7])
           i += 7
           op_toggle = False 
        else:
            if op_toggle:
                res.append(mem_string[i])
            i += 1
    return ''.join(res)

def find_matches(mem_string: str) -> list[tuple[int, int]]:
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, mem_string)
    return [(int(num1), int(num2)) for num1, num2 in matches]

if __name__ == '__main__':
    result = day3()
    print(f'Day 3 Part 1: {result.p1}')
    print(f'Day 3 Part 2: {result.p2}')