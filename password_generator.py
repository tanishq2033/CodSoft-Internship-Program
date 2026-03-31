import random
import string

print("PASSWORD GENERATOR")

length = int(input("Enter password length: "))
use_digits = input("Include numbers? (yes/no): ").lower()
use_symbols = input("Include symbols? (yes/no): ").lower()

characters = string.ascii_letters

if use_digits == "yes":
    characters += string.digits

if use_symbols == "yes":
    characters += string.punctuation

if length <= 0:
    print("Please enter a valid positive length")
else:
    password = ""
    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)