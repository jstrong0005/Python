
"""
Given the list of hexadcimal digits in varible "x" below, return a string that is made from their ASCII characters.  Example: ['41', '4f'] > "AR".

x = ['74', '68', '61', '74', '73', '20', '6e', '6f', '20', '6f', '72', '64', '69', '6e', '61', '72', '79', '20', '72', '61', '62', '62', '69', '74']

Imagine this is a network packet with hexadecimal characters in it. Covert the list of hex bytes to a string!  Remember that the int() function can be used to convert a string to an integer by passing a base as the second parameter like this: int("FF", 16) will return 255.  So you can convert the character at posistion 0 and then the character in position 1 like this:

#>>> chr(int(x[0], 16))

't'

#>>> chr(int(x[1], 16))

'h'

Now its your turn.  Write a function that steps through each character in the list and converts them into strings.

Submit your function with the correct answer.  This can be a screenshot or .txt document, as long as your function and answer are visible.

Good luck!"""


x = ['74', '68', '61', '74', '73', '20', '6e', '6f', '20', '6f', '72', '64', '69', '6e', '61', '72', '79', '20', '72', '61', '62', '62', '69', '74']

z = []

#print(chr(int(x[0], 16)))

for index in x:
    z.append(chr(int(index, 16)))

print(*z, sep=" ")