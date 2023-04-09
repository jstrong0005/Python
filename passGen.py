'''
#incomplete password generator
import random
import string



def generate_password():
    # define all the possible characters that can be used in the password
    pwLength = input("Plese enter the length needed for password: ")
    chScheme = input("Enter 1 for lowercase and uppercase letters."
                      "\nEnter 2 for letters and numbers."
                      "\nEnter 3 for letters numbers and special characters: ")
    if chScheme == '1':
        characters = string.ascii_letters
    elif chScheme == '2':
        characters = string.ascii_letters + string.digits
    elif chScheme == '3':
        characters = string.ascii_letters + string.digits + string.punctuation
#    characters = string.ascii_letters + string.digits + string.punctuation

    # randomly select characters from the pool until the desired length is reached
    password = ''.join(random.choice(characters) for i in range(int(pwLength)))

    return password

# example usage: generate a password with 12 characters
password = generate_password()
print(password)
'''

'''
passwordgen.py
Author: Shane Strong
This program prompts the user for a password length as well aas if they want upper, lower, numbers, and or punctuation in their password.
'''

import random # Import random to generate random password by using random.choice
import string # Import string to generate our custom char set

upper = string.ascii_uppercase      # Stores all uppercase letters A-Z
lower = string.ascii_lowercase      # Stores all lowercase letters a-z
number = string.digits 		        # Stores all digits 0-9
punctuation = string.punctuation    # Stores all punctuation chars

password = ''  # Used to store the password
charset = ''   # Used to store charset based on the user input

# Check for password length from user. If not int, print error and ask for password length again.

while True:
    try:
        password_length = int(input("Enter the length ot the requested password: "))
        break
    except ValueError as error:
        print(error)
        print("Password length must be an integer, please try again.")

# Ask the user if they would like uppercase chars in their password

use_upper = input("Would you like uppercase characters in your password? [Y or N]: ")

# Ask the user if they would like lowercase chars in their password

use_lower = input("Would you like lowercase characters in your password? [Y or N]: ")

# Ask the user if they would like to use digits in their password

use_numbers = input("Would you like numbers in your password? [Y or N]: ")

# Ask the user if they would like punctuation in their password

use_punctuation = input("Would you like punctuation in your password? [Y or N]: ")

if use_upper in ('Y', 'y'):
    charset += upper

if use_lower in ('Y', 'y'):
    charset += lower

if use_numbers in ('Y', 'y'):
    charset += number

if use_punctuation in ('Y', 'y'):
    charset += punctuation


if len(charset) == 0:
    print("Selections are empty, you must choose at least one upper, lower, number, or punctuation. Please try again.")

else:
    for x in range(password_length):
        password += random.choice(charset)

print("Here is your secure password: "+ password)
