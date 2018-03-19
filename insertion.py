import time
from randomList import randomList;


def insertionSort(my_list):
    start = int(round(time.time() * 1000))
    for i in range(len(my_list)):

        for j in range(i):
            if my_list[i] < my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]

    end = int(round(time.time() * 1000))
    print 'Original Insertion Sort: ',end - start
    return my_list



# create random list of (size, lower limit, upper limit)
ran_list = randomList(5000, 0, 100)
#print ran_list

insertionSort(ran_list)
