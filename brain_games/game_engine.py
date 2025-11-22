import prompt

ROUNDS_COUNT = 3


def run_game(get_round, description: str) -> None:

    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(description)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = get_round()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ").lower()

        if answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
