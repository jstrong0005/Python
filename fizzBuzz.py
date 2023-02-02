#! Python3
#############################################
# Program Name:         FizzBuzz
# Brought to you by:    Shane Strong
#############################################

"""
Loop and Selection Coding Challenge
Objective:
Write a basic loop that is composed of multiple selections.
Challenge:
Write a program that performs the following tasks:
1.  Asks the user for two numbers (lower and upper).  These two numbers will create a
range for our project.
2. The first number will be the lower limit of the range while the second number will
be the upper limit of the range.
3. Loop through the range of numbers (omitting zero if chosen as lower limit) and do
the following:
•If the number is evenly divisible by 30, print “Foo”
•If the number is evenly divisible by 5, print “Bar”
•If the number is evenly divisible by 3, print “Fizz”
•If the number is evenly divisible by 2, print “Buzz”
•If the number is evenly divisible by 3 and 2, print “FizzBuzz”
•If the number does not meet any of the criteria above, print “Bazz”
4. Finally print the following statements:
•“The total numbers evaluated was _________.”
•“There were ________ numbers that are divisible by 30.”
•“There were ________ numbers that are divisible by 5.”
•“There were ________ numbers that are divisible by 3.”
•“There were ________ numbers that are divisible by 2.”
•“There were ________ numbers that are divisible by both 3 and 2.”
•“There were ________ numbers that didn’t meet any of the requirements
above.”
"""
placeholder = "Not Yet"
lower = float(input("Enter a number for the low end of the range: "))
while lower == 0:
    print("You cannot choose 0 as your lower number...")
    lower = float(input("Enter a number for the low end of the range: "))
upper = float(input("Enter a number for the high end of the range: "))

evalNumber = lower
fooCount = 0
barCount = 0
fizzCount = 0
buzzCount = 0
noMatch = 0
fizzBuzzCount = 0
totalEval = 0
for counter in range(int(lower), int(upper)):
    totalEval += 1
    if (evalNumber % 3) and (evalNumber % 2) == 0:
        print("FizzBuzz")
        evalNumber += 1
        fizzBuzzCount += 1
        #fizzCount += 1
        #buzzCount += 1
    elif evalNumber % 3 == 0:
        print("Fizz")
        evalNumber += 1
        fizzCount += 1
    elif evalNumber % 2 == 0:
        print("Buzz")
        evalNumber += 1
        buzzCount += 1
    elif evalNumber % 30 == 0:
        print("Foo")
        evalNumber += 1
        fooCount += 1
    elif evalNumber % 5 == 0:
        print("Bar")
        evalNumber += 1
        barCount += 1
    else:
        print("Bazz")
        evalNumber += 1
        noMatch += 1


print("The total numbers evaluated was ", totalEval, ".")
print("There were ", fooCount, " numbers that are divisible by 30.")
print("There were ", barCount, " numbers that are divisible by 5.")
print("There were ", fizzCount, " numbers that are divisible by 3.")
print("There were ", buzzCount, " numbers that are divisible by 2")
print("There were ", fizzBuzzCount, " numbers that are divisible by both 3 and 2.")
print("There were ", noMatch, " numbers that didn't meet any of the requirements above.")
