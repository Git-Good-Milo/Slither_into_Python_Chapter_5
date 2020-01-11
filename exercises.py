# Question 1
# Write a program that prints the first n numbers of the Fibonacci sequence. The Fibonacci sequence is defined as :
# Fn=(Fn−1)+(Fn−2)
# F0=0,F1=1
#
# That is, the next number in the sequence is the sum of the previous two numbers and the first two numbers in the sequence are 0 and 1.

# First we define our variables
nterms = int(input("Please enter a number term to find the Fibonacci Number:  "))
n1 = 0
n2 = 1
counter = 0

# Next we create the while loop
print("Here is your Fibonacci sequence:")
print()
while counter < nterms:
    print(n1)
    nth = n1 + n2
    # Next we have to update the values
    n1 = n2
    n2 = nth
    counter += 1


