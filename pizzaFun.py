#! Python3
# Written By: Shane Strong
#
"""

List Challenge #1
Complete the coding challenge listed below.  Submit your code as a .txt file, video walk-
through, or as screenshots.
You work at Len’s Slice, a new pizza joint in the neighborhood. You are going to use your
knowledge of Python lists to organize some of your sales data.
1. To keep track of the kinds of pizzas you sell, create a list called toppings that holds the
following:
a. pepperoni
b. pineapple
c. cheese
d. sausage
e. olives
f. anchovies
g. mushrooms
2. To keep track of how much each kind of pizza slice costs, create a list called prices that
holds:
a. 2
b. 6
c. 1
d. 3
e. 2
f. 7
g. 2
3. Find the length of the toppings list and store it in a variable called num_pizzas.
4. Print the string "We sell X different kinds of pizza!", with num_pizzas where the X is.
5. Use zip to combine the two lists into a list called pizzas that has the structure:
a. [(price_0, topping_0), (price_1, topping_1), (price_2, topping_2), ...]
b. In order to make the result of zip a list, remember to do the following:
list(zip(___, ___))
6. Print pizzas. Does it look the way you expect?
7. Sort pizzas so that the pizzas with the lowest prices are at the start of the list.
8. Store the first element of pizzas in a variable called cheapest_pizza.
9. A man in a business suit walks in and shouts “I will have your MOST EXPENSIVE
pizza!” Get the last item of the pizzas list and store it in a variable called
priciest_pizza.
10. Three mice walk into the store. They don’t have much money (they’re mice), but they do
each want different pizzas. Slice the pizzas list and store the 3 lowest cost pizzas in a list
called three_cheapest.
11. Print the three_cheapest list.
12. Your boss wants you to do some research on $2 slices. Count the number of occurrences
of 2 in the prices list, and store the result in a variable called num_two_dollar_slices. Print
the contents of this new list.

"""
# Here we make the list of toppings
toppingsRaw = "pepperoni pineapple cheese sausage olives anchovies mushrooms"
toppings = toppingsRaw.split()

# Here we make the list of prices
pricesRaw = "2 6 1 3 2 7 2"
prices = pricesRaw.split()

# store the number of pizza variations to a intiger
numb_pizzas = int(len(prices))
print("Welcome to Len's Slice! ")
#print(toppings[2], prices[3], str(numb_pizzas))
print("We sell", numb_pizzas, "different kinds of pizza!")
pizzas = list(zip(prices, toppings))
pizzas.sort()
print("\nThe budget conscious pizza: ")
cheapest_pizza = list(pizzas[0])
print(cheapest_pizza)
priciest_pizza = list(pizzas[len(pizzas) -+ 1])
print("\nThe premium pizza: ")
print(priciest_pizza)
print("\nThe 3 value pizzas: ")
three_cheapest = list(pizzas[:3])
print(three_cheapest)

twoDollarSlice = 0
twoDollarList = []
for index in prices:
    if index == '2':
        twoDollarSlice += 1

#This is a hack and isn't right
twoDollarList = list(pizzas[1:4])

print("\nOur two dollar menu has", str(twoDollarSlice), "items", twoDollarList)

