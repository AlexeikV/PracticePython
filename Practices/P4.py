# Declare the num
num = 0

# Get a data
num = int(input("Choose a number to divide:\n"))

# Generate a range base in the num
rangeN = list(range(1, num+1))

# Build array
divisor = []

for number in rangeN:
    if num % number == 0:
        divisor.append(number)

print(divisor)