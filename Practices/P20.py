import random


def binary_search(l, num):
    tmp = sorted(l)
    f = 0
    h = int(len(tmp))
    while f <= h:
        m = int(f + (h - f) / 2)
        if tmp[m] == num:
            return True
        elif tmp[m] < num:
            f = m + 1
        elif tmp[m] > num:
            h = m - 1
    return False


if __name__ == "__main__":

    nlist = random.sample(range(200), random.randint(1, 50))
    print(nlist)

    if binary_search(list(nlist), int(input("Enter a number: "))):
        print("Found")
    else:
        print("Not Found")
