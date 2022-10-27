import random


def guessing_game():
    rand = random.randint(1, 100)
    trial = 3
    while True and trial != 0:
        number = input("Guess a number between 1 and 100 (inclusive): ")
        number = int(number)
        if number > rand:
            print("Too High")
            print(f"You guessed: {number}")
            trial = trial - 1
            print(f'You have only {trial} left. 👎')
        elif number < rand:
            print("Too Low")
            print(f"You guessed: {number}")
            trial = trial - 1
            print(f'You have only {trial} left. 👎')
        else:
            print("Just Right 🎉")
            break


guessing_game()
