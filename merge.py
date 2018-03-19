import time
from randomList import randomList;


def recursiveMerge(my_list):
    #start = int(round(time.time() * 1000))

    merge(my_list, 0, len(my_list))


    #end = int(round(time.time() * 1000))
    #print 'Original Insertion Sort: ',end - start
    return my_list


def merge(my_list, start, end):
    #print start, length
    if end - start == 1:
        #done....
        print my_list[start]
        #print start

    else:
        #break down some more...
        print my_list[start: end]
        middle = (start + end) / 2
        merge(my_list, start, middle)
        merge(my_list, middle, end)
        merge2(my_list, start, middle, end)



def merge2(list, start, middle, end):

    print "MERGING: ",list[start:end]


# create random list of (size, lower limit, upper limit)
ran_list = randomList(8, 0, 100)
#print ran_list

1 , 2 ,3 ,4 , 5, 6, 7, 8


recursiveMerge(ran_list)
