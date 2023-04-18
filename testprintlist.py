# Put your code here
def printAll(seq):
    if seq:
        print(seq, "->", seq[0])
        printAll(seq[1:])

printAll(list(range(10)))
