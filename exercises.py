# # Question 1
# # Write a program that prints the first n numbers of the Fibonacci sequence. The Fibonacci sequence is defined as :
# # Fn=(Fn−1)+(Fn−2)
# # F0=0,F1=1
# #
# # That is, the next number in the sequence is the sum of the previous two numbers and the first two numbers in the sequence are 0 and 1.
#
# # First we define our variables
# nterms = int(input("Please enter a number term to find the Fibonacci Number:  "))
# n1 = 0
# n2 = 1
# counter = 0
#
# # Next we create the while loop
# print("Here is your Fibonacci sequence:")
# print()
# while counter < nterms:
#     print(n1)
#     nth = n1 + n2
#     # Next we have to update the values
#     n1 = n2
#     n2 = nth
#     counter += 1

# Question 2
# Write a program that prints a sequence such as the one shown below. The number of stars in the widest part should be equal to the number a user inputs:

# First we assign a user input number and initialise our counter

user_input = int(input("Please enter your number: "))
counter = 0

# Next we write our while loop
while counter < user_input:
    print(counter*"*")
    counter += 1

while counter > 1:
    print(counter*"*")
    counter -= 1

# Question 3
#  Write a program that converts a 4 bit binary number into its decimal equivalent.