# Task3 PASSWORD GENERATOR
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("WELCOME :) \nTHIS IS YOUR PASSWORD GENERATOR")

    try:
        length = int(input("Enter the length of password required: "))
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    password = generate_password(length)

    print(f"\n\nGenerated Password: {password}")

if __name__ == "__main__":
    main()