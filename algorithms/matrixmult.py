import sys
import time

SIZE = 100

time_file = open(sys.argv[3], "w")
time_file.write("index,time\n")

for iter in range(1000):
    matrix_a = []
    matrix_b = []
    with open(sys.argv[1]) as input_file:
        for i in range(SIZE):
            matrix_a.append(list(map(int, input_file.readline().split())))
        input_file.readline()
        for i in range(SIZE):
            matrix_b.append(list(map(int, input_file.readline().split())))

    result = []

    starttime = time.time_ns()

    for i in range(SIZE):
        result.append([])
        for j in range(SIZE):
            result[-1].append(0)
            for k in range(SIZE):
                result[-1][-1] += matrix_a[i][k] * matrix_b[k][j]

    endtime = time.time_ns()
    time_file.write(str(iter) + "," + str(endtime - starttime) + "\n")

    with open(sys.argv[2], "w") as answer_file:
        for line in result:
            for element in line:
                answer_file.write(str(element) + " ")
            answer_file.write("\n")
time_file.close()
