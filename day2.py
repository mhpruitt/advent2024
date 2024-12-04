"""
--- Day 2: Red-Nosed Reports ---

https://adventofcode.com/2024/day/2
"""

def extract_readings():
    with open('inputs/day2.txt', 'r') as f:
        while readings := f.readline().strip().split():
            yield readings

def is_safe_increasing(r1: str, r2: str) -> bool:
    return 3 >= int(r2) - int(r1) >= 1

def is_safe_decreasing(r1: str, r2: str) -> bool:
    return 3 >= int(r1) - int(r2) >= 1


# Part 1
def check_if_safe(readings: list, predicate) -> bool:
    return all(predicate(readings[i], readings[i+1]) for i in range(len(readings)-1))

def check_if_all_safe(readings: list) -> bool:
    return check_if_safe(readings, is_safe_increasing) or check_if_safe(readings, is_safe_decreasing)


# Part 2
def check_if_safe_with_damper(readings: list, predicate, has_been_damped=False) -> bool:
    for idx in range(len(readings) - 1):
        if not predicate(readings[idx], readings[idx + 1]):
            return not has_been_damped and any(
                check_if_safe_with_damper(readings[:idx+o] + readings[idx+1+o:], predicate, True)
                for o in (0, 1)
            )

    return True


def check_if_all_safe_with_damper(readings: list) -> bool:
    return check_if_safe_with_damper(readings, is_safe_increasing) or check_if_safe_with_damper(readings, is_safe_decreasing)



def main():
    print(f'Part 1: {sum(check_if_all_safe(r) for r in extract_readings())}')
    print(f'Part 2: {sum(check_if_all_safe_with_damper(r) for r in extract_readings())}')

