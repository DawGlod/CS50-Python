def is_valid(s):
    #First condition
    for sign in s[0:2]:
        if not sign.isalpha():
            return False
    #Second condition
    sum = 0
    for sign in s:
        sum += 1
    if not 4 <= sum <= 6:
        return False
    #Third condition
    for character in s[2:]:
        if character.isdigit():
            if character == "0":
                return False
            for a in s[s.index(character):]:
                if not a.isdigit():
                    return False
            break
    #Fourth condition
    for character in s:
        if not character.isalnum():
            return False
    return True




def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()


