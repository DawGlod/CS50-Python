from validator_collection import validators

def response(email_address):
    try:
        if validators.email(email_address):
            return("Valid")
    except Exception:
        return "Invalid"

def main():
    email_address = input("Email: ")
    print(response(email_address))

if __name__ == "__main__":
    main()
