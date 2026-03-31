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

password = ""
for _ in range(length):
    password += random.choice(characters)

print("Generated Password:", password)