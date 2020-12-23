#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

#Start the program
#Get number
number = input("Enter a number: ")

mod = number % 2
#Validate the type of number if is odd and even
if mod > 0:
    print("You insert an odd number")
else:
    print("You insert an even number")
