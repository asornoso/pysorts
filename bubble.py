import time
from randomList import randomList;


def bubbleSort(my_list):
    start = int(round(time.time() * 1000))
    for i in range(len(my_list)):

        for j in range(len(my_list)-1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

    end = int(round(time.time() * 1000))
    print 'Original Bubble Sort: ',end - start
    return my_list


def bubbleSortStepper(my_list):
    start = int(round(time.time() * 1000))
    for i in range(len(my_list)):

        for j in range(len(my_list)-1 -i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

    end = int(round(time.time() * 1000))
    print 'Improved Bubble Sort: ', end - start
    return my_list

# create random list of (size, lower limit, upper limit)
ran_list = randomList(5000, 0, 100)

bubbleSort(ran_list)
bubbleSortStepper(ran_list)
