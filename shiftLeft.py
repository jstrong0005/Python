
import string

seriesOfBits = input("Enter a string of bits: ")

print(seriesOfBits)
moddedBob = seriesOfBits[1:] + seriesOfBits[0:1]
print(moddedBob)

"""
print("last character")
print(seriesOfBits[:-1])
print("first character")
print(seriesOfBits[0:1])
print("first 2 character")
print(seriesOfBits[:2])
print("the entire string")
print(seriesOfBits[:len(seriesOfBits)])
print("last three characters")
print(seriesOfBits[-3:])
print("Drill to extract file")
print(seriesOfBits[2:6])
print("last character")
print(seriesOfBits[-1:])
"""