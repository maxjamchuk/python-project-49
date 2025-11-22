from random import choice, randint

DESCRIPTION = "What is the result of the expression?"

MIN_NUMBER = 0
MAX_NUMBER = 20
OPERATIONS = ("+", "-", "*")


def _calculate(a: int, b: int, op: str) -> int:
    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case _:
            raise ValueError(f"Unsupported operation: {op}")


def make_round() -> tuple[str, str]:
    a = randint(MIN_NUMBER, MAX_NUMBER)
    b = randint(MIN_NUMBER, MAX_NUMBER)
    op = choice(OPERATIONS)

    question = f"{a} {op} {b}"
    result = _calculate(a, b, op)

    return question, str(result)
