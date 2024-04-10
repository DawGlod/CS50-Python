import random


def get_level():
    try:
        level = int(input("Level: "))
        possible_levels = [1, 2, 3]
        if level not in possible_levels:
            get_level()
        return level
    except ValueError:
        get_level()


def generate_integer(level):
    score = 0
    for _ in range(10):
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        elif level == 3:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
        for i in range(4):
            if i == 3:
                print(f"{x} + {y} = {x + y}")
                break
            print(f"{x} + {y} = ", end="")
            answer = int(input())
            if answer != x + y:
                print("EEE")
                continue
            else:
                score += 1
                break
    return score


def main():
    level = get_level()
    score = generate_integer(level)
    print(f"Score: {score}")


if __name__ == "__main__":
    main()
