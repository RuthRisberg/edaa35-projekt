import sys
import time

LIST_LEN = 3000

time_file = open(sys.argv[3], "w")
time_file.write("index,time\n")

for iter in range(1000):
    original_list = []
    with open(sys.argv[1]) as input_file:
        for i in range(LIST_LEN):
            original_list.append(int(input_file.readline()))
    list_to_sort = original_list.copy()

    starttime = time.time_ns()

    buf_list = [None] * len(list_to_sort)

    sectionlen = 1
    while sectionlen < len(list_to_sort):
        for sectionstart in range(0, len(list_to_sort), 2 * sectionlen):
            index1 = sectionstart
            index2 = sectionstart + sectionlen
            for i in range(sectionstart, min(sectionstart + 2 * sectionlen, len(list_to_sort))):
                if index2 >= min(sectionstart + 2 * sectionlen, len(list_to_sort)):
                    buf_list[i] = list_to_sort[index1]
                    index1 += 1
                elif index1 >= sectionstart + sectionlen:
                    buf_list[i] = list_to_sort[index2]
                    index2 += 1
                elif list_to_sort[index1] < list_to_sort[index2]:
                    buf_list[i] = list_to_sort[index1]
                    index1 += 1
                else:
                    buf_list[i] = list_to_sort[index2]
                    index2 += 1

        sectionlen *= 2
        buf_list, list_to_sort = list_to_sort, buf_list

    endtime = time.time_ns()
    time_file.write(str(iter) + "," + str(endtime - starttime) + "\n")

    with open(sys.argv[2], "w") as answer_file:
        for element in list_to_sort:
            answer_file.write(str(element) + " ")
        answer_file.write("\n")
time_file.close()
