#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

#Start de program
#Get name
name = input("Whats your name? ")
#Get age
age = int(input("How old are you? "))

year = str((2020 - age) + 100)

#Print name
print(name + " will turn 100 years old in the year " + year)