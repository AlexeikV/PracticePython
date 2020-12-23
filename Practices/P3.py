#List to get in the practice
list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#Array to create in the insert the result
listN = []

# Temporal data
number = int(input("Enter a number\n"))
for i in list:
        if(i < number):
            listN.append(i)
        else:
            break

# Print the result
print("List containing numbers less than", number, listN)