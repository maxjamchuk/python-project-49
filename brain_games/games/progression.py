from random import randint

DESCRIPTION = "What number is missing in the progression?"

PROGRESSION_LENGTH = 10
MIN_START = 1
MAX_START = 20
MIN_STEP = 1
MAX_STEP = 10


def _build_progression(start: int, step: int, length: int) -> list[int]:
    return [start + index * step for index in range(length)]


def make_round() -> tuple[str, str]:
    """Генерирует один раунд игры «Арифметическая прогрессия».

    Возвращает:
        question (str): прогрессия с ".." вместо одного числа
        correct_answer (str): спрятанное число
    """
    start = randint(MIN_START, MAX_START)
    step = randint(MIN_STEP, MAX_STEP)
    progression = _build_progression(start, step, PROGRESSION_LENGTH)

    hidden_index = randint(0, PROGRESSION_LENGTH - 1)
    correct_value = progression[hidden_index]
    progression[hidden_index] = ".."

    question = " ".join(str(item) for item in progression)
    return question, str(correct_value)
