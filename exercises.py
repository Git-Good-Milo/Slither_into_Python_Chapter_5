# # Question 1
# # Write a program that prints the first n numbers of the Fibonacci sequence. The Fibonacci sequence is defined as :
# # Fn=(Fn−1)+(Fn−2)
# # F0=0,F1=1
# #
# # # Next we create the while loop
# # print("Here is your Fibonacci sequence:")
# # print()
# # while counter < nterms:
# #     print(n1)
# #     nth = n1 + n2
# #     # Next we have to update the values
# #     n1 = n2
# #     n2 = nth
# #     counter += 1
#
# # Question 2
# # Write a program that prints a sequence such as the one shown below. The number of stars in the widest part should be equal to the number a user inputs:
#
# # First we assign a user input number and initialise our counter
#
# user_input = int(input("Please enter your number: "))
# counter = 0
#
# # Next we write our while loop
# while counter < user_input:
#     print(counter*"*")
#     counter += 1
#
# while counter > 1:
#     print(counter*"*")
#     counter -= 1

# Question 3
#  Write a program that converts a 4 bit binary number into its decimal equivalent.

# Get a user input for a binary number. Save it as a string.
# Initialise an index to 0
user_input = input("Enter a binary number, no more than 4 bit: ")


# Construct a while loop
if len(user_input) > 4:
    print("Please enter a 4 bit binary number")
elif len(user_input) == 4:
    index = 0
    print("lol")
    while index < 4:
        print("lol")
        if user_input[index] == 1:
            print("2")
            index += 1
        elif user_input[index] == 0:
            print("3")
            index += 1

