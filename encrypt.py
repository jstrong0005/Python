#! python3
###########################################################
# Filename: encrypt.py
# Program Name: Caesar Cipher
# Brought to you by: Shane Strong
#
###########################################################

##-----------------------------------------------------------------------##
"""
Encrypts an input string of lowercase letters and prints
the result. The other input is the distance value
"""


plainText = input("Enter a one-word, lowercase message: ")
distance = int(input("Enter the distance value: "))
code = ""
for ch in plainText:
    ordValue = ord(ch)
    cipherValue = ordValue + distance
    if cipherValue > ord('z'):
        cipherValue = ord('a') + distance - (ord('z') - ordValue + 1)
    code += chr(cipherValue)
print(code)

