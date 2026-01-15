
import random
import string


def welcome_message():
    print("============================================")
    print("         PYTHON PASSWORD GENERATOR           ")
    print("============================================")
    print("This program generates a secure password")
    print("based on your selected criteria.\n")


def get_password_length():
    while True:
        try:
            length = int(input("Enter password length (minimum 6): "))
            if length < 6:
                print("Password length should be at least 6.\n")
            else:
                return length
        except ValueError:
            print("Please enter a valid number.\n")


def get_user_choice(message):
    while True:
        choice = input(message + " (yes/no): ").lower()
        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print(" Please enter yes or no.\n")


def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""

    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if characters == "":
        return None

    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    welcome_message()

    while True:
        length = get_password_length()

        use_letters = get_user_choice("Include letters?")
        use_numbers = get_user_choice("Include numbers?")
        use_symbols = get_user_choice("Include symbols?")

        password = generate_password(length, use_letters, use_numbers, use_symbols)

        if password is None:
            print("\n You must select at least one character type.\n")
        else:
            print("\n GENERATED PASSWORD")
            print("--------------------------------------------")
            print(password)
            print("--------------------------------------------")

        again = input("\nDo you want to generate another password? (yes/no): ").lower()
        if again != "yes":
            break

main()
