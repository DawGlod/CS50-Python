import random
import sys

def game():
    try:
        level = int(input("Level: "))
        if level < 1:
            raise ValueError
        correct = random.randrange(1, level)
        while True:
            guess = int(input("Guess: "))
            if guess == correct:
                print("Just right!")
                sys.exit()
            elif guess > correct:
                print("Too large!")
            elif guess < correct:
                print("Too small!")
    except ValueError:
        game()


def main():
    game()


if __name__ == "__main__":
    main()
