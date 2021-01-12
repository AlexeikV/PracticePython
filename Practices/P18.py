from random import *

def cowsnbulls():
    number = [str(randint(0,9)) for x in range(4)]
    print(number)
    guess = []
    n = 0
    while guess != number:
        cs = 0
        bs = 0
        guess = list(input("Guess a 4 digit number: "))
        guessed = []
        for i in range(4):
            if guess[i] == number[i]:
                cs += 1
                guessed.append(guess[i])
            elif guess[i] in number and guessed.count(guess[i]) < number.count(guess[i]):
                bs += 1
                guessed.append(guess[i])
        if cs > 1:
            cow = "cows"
        else:
            cow = "cow"
        if bs > 1:
            bull = "bulls"
        else:
            bull = "bull"
        print("%d %s and %d %s" %(cs, cow, bs, bull))
        cs = 0
        bs = 0
        n += 1
    print("That's correct, and it only took %d guesses!" %(n))


if __name__ == "__main__":
    cowsnbulls()