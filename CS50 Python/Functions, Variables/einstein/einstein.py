def energy(mass):
    c = 300000000
    return mass * c**2


def main():
    m = int(input("Mass: "))
    print(energy(m))


if __name__ == "__main__":
    main()
