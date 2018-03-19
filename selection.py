import time
from randomList import randomList;


def selectionSort(my_list):
    #start = int(round(time.time() * 1000))
    for i in range(len(my_list)):
        min = i

        for j in range(len(my_list) - i):
            if my_list[j+i] < my_list[min]:
                min = j+i
        my_list[i], my_list[min] = my_list[min], my_list[i]
        print my_list

    #end = int(round(time.time() * 1000))
    #print 'Original Insertion Sort: ',end - start
    return my_list



# create random list of (size, lower limit, upper limit)
ran_list = randomList(10, 0, 100)
#print ran_list

selectionSort(ran_list)
