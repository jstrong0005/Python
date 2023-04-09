# Write your dog_years function here:
def dog_years(name, age):
    i = age * 7
    print('{}. you are {} years old in dog years'.format(name, i))

dog_years("Shane", 42)

print(dog_years("Brian Urlacher", 16))
# should print "Brian Urlacher, you are 112 years old in dog years"
print(dog_years("Walter Payton", 0))
# should print "Walkter Payton, you are 0 years old in dog years"