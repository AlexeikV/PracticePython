import random
import string

def GeneratorPwd(size, type):
    charP=string.ascii_uppercase+string.ascii_lowercase
    if type=='strong':
        password=''.join(random.choice(charP) for _ in range(size-2))+random.choice(string.punctuation)+random.choice(string.digits)
    elif type=='weak':
        password=''.join(random.choice(charP) for _ in range(size))
    else:
        print("I don't recognize the type!")
        password=''
    return password

if __name__ == '__main__':
    user_pass=input("Tell me strong or weak password?")
    size_pass=int(input("Tell me the password lenght you need?"))
    password = GeneratorPwd(size_pass,user_pass)
    print("Your password is '%s'" %password)