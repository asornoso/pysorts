from random import randint

def randomList(size, lower, upper):
    a_list = []
    for i in range(size):
        a_list.append(randint(lower,upper))

    return a_list
