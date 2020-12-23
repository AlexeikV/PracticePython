import sys

user1 = input("Whats your name u1?\n")
user2 = input("Whats your name u2?\n")
u1_answer = input("%s, do yo want to choose rock, paper or scissors?\n" % user1)
u2_answer = input("%s, do you want to choose rock, paper or scissors?\n" % user2)

def check(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(check(u1_answer.lower(), u2_answer.lower()))