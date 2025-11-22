from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_NUMBER = 2
MAX_NUMBER = 100


def is_prime(n: int) -> bool:
    return (
        n == 2 or
        (
            n > 2
            and n & 1
            and all(n % d for d in range(3, int(n ** 0.5) + 1, 2))
        )
    )


def make_round() -> tuple[str, str]:
    number = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = "yes" if is_prime(number) else "no"
    return str(number), correct_answer
