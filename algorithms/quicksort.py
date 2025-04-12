import sys
import time

LIST_LEN = 3000


def quicksort(arr, lo, hi):
    if lo >= hi:
        return

    pivot = arr[lo]
    loindex = lo + 1
    hiindex = hi
    while loindex <= hiindex:
        if arr[loindex] > pivot:
            arr[loindex], arr[hiindex] = arr[hiindex], arr[loindex]
            hiindex -= 1
        else:
            loindex += 1

    arr[lo], arr[hiindex] = arr[hiindex], arr[lo]

    quicksort(arr, lo, hiindex - 1)
    quicksort(arr, loindex, hi)


time_file = open(sys.argv[3], "w")
time_file.write("index,time\n")

for iter in range(1000):
    original_list = []
    with open(sys.argv[1]) as input_file:
        for i in range(LIST_LEN):
            original_list.append(int(input_file.readline()))
    list_to_sort = original_list.copy()

    starttime = time.time_ns()

    quicksort(list_to_sort, 0, len(list_to_sort) - 1)

    endtime = time.time_ns()
    time_file.write(str(iter) + "," + str(endtime - starttime) + "\n")

    with open(sys.argv[2], "w") as answer_file:
        for element in list_to_sort:
            answer_file.write(str(element) + " ")
        answer_file.write("\n")
time_file.close()
