from random import randint

DESCRIPTION = "Find the greatest common divisor of given numbers."

MIN_NUMBER = 1
MAX_NUMBER = 100


def _gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def make_round() -> tuple[str, str]:
    first = randint(MIN_NUMBER, MAX_NUMBER)
    second = randint(MIN_NUMBER, MAX_NUMBER)
    question = f"{first} {second}"
    answer = _gcd(first, second)
    return question, str(answer)
