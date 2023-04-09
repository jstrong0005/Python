seriesOfBits = input("Enter a string of bits: ")

moddedBob = seriesOfBits[-1:] + seriesOfBits[:-1]
print(moddedBob)