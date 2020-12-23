import random

# Generate random data
list_1 = random.sample(range(20), 13)
list_2 = random.sample(range(20), 13)

ran = []

print("Random List 1:", list_1)
print("Random List 2:",list_2, "\n")

for number in list_1:
    for numbers in list_2:
        if (number == numbers):
            ran.append(number)

print("The commmon values: ", ran)