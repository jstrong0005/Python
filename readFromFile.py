f = open(f, 'r')
textFromFile = ""
while True:
    print("hey")
    line = f.readline()
    if line == "":
        break
    print(line)
    textFromFile = str(textFromFile) + str(line)


print(textFromFile)
nf = open(nf, 'w')
nf.write(textFromFile)
nf.close()
"""
exercise 4.8

# Put your code here
copyFrom = input("Enter the input filt name: ")
copyTo = input("Enter the output file name: ")
textFromFile = ""

f = open(copyFrom, "r")
nf = open(copyTo, 'w')
textFromFile = f.read()
nf.write(textFromFile)
nf.close()
"""