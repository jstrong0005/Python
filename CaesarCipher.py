#! python3

#######################################################################################
# File Name: CaesarCypher.py
# Written by: Shane Stron
# Hopefully this program will be able to perform the required tasks
#
########################################################################################
# Import the string library so we can play with strings
import string
# Declare some variables so we can make choices and manipulate string
plainText = ""
cipherText = ""
shiftSize = ""
SYMBOLS = string.ascii_letters + string.digits + string.punctuation + " "
print(SYMBOLS)
print(len(SYMBOLS))
print(SYMBOLS[-1:])
print(SYMBOLS[-2:])
print(SYMBOLS[:1])
counter = 0
for counter in SYMBOLS:
    #bob = int(counter)
    print(counter)
    print(ord(counter))


bob = int(5)
sue = bob - 1
print(SYMBOLS[sue:bob])

cryptSelect = ["encrypt", "decrypt"]
# Ask the user to make a choice by typing what they want
choice = input("Would you like to encrypt or decrypt? ")
#number = int(len(SYMBOLS))




if choice == cryptSelect[0]:
    print("Let's shake 'em up")
    plainText = input("Enter a plain text message: ")
    shiftSize = int(input("Enter the distance value: "))
    cipherText = ""
    for ch in plainText:
        ordValue = ord(ch)
        cipherValue = ordValue + shiftSize
        if cipherValue > ord(SYMBOLS[-1:]):
            cipherValue = ord(SYMBOLS[:1]) + ord(shiftSize) - ((ord(SYMBOLS[-1:])) - ordValue + 1)
        cipherText += chr(cipherValue)
    print(cipherText)
elif choice == cryptSelect[1]:
    print("Let's get 'em straight")
    cipherText = input("Enter the coded text: ")
    shiftSize = int(input("Enter the distance value: "))
    plainText = ""
    for ch in cipherText:
        ordValue = ord(ch)
        cipherValue = ordValue - shiftSize
        if cipherValue < ord('a'):
           cipherValue = ord('~') - (shiftSize - (ord('a')) - ordValue - 1)
        plainText += chr(cipherValue)
        print(plainText)
        print(ord(cipherValue))
    print(plainText)
else:
    print("You'll have to spell it out for me...")


#print(choice)
#print(cryptSelect[0])
#plainText = input("Please enter plain text string to be encrypted: ")
#shiftSize = input("Enter the key size as an integer: ")

