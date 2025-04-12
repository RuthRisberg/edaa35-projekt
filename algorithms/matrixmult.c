#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <assert.h>

#define SIZE 100

int main(int argc, char **argv)
{
    int matrix_a[SIZE][SIZE];
    int matrix_b[SIZE][SIZE];
    int result[SIZE][SIZE];
    struct timespec starttime, endtime;
    int i, j, k, iter;
    FILE *input_file, *answer_file, *time_file;

    time_file = fopen(argv[3], "w");

    fprintf(time_file, "index,time\n");

    for (iter = 0; iter < 1000; iter++)
    {
        input_file = fopen(argv[1], "r");
        for (i = 0; i < SIZE; i++)
            for (j = 0; j < SIZE; j++)
                fscanf(input_file, "%d", &matrix_a[i][j]);
        for (i = 0; i < SIZE; i++)
            for (j = 0; j < SIZE; j++)
                fscanf(input_file, "%d", &matrix_b[i][j]);
        fclose(input_file);

        timespec_get(&starttime, TIME_UTC);

        for (i = 0; i < SIZE; i++)
        {
            for (j = 0; j < SIZE; j++)
            {
                result[i][j] = 0;
                for (k = 0; k < SIZE; k++)
                {
                    result[i][j] += matrix_a[i][k] * matrix_b[k][j];
                }
            }
        }

        timespec_get(&endtime, TIME_UTC);
        fprintf(time_file, "%d,%ld\n", iter, ((int)1e9) * (endtime.tv_sec - starttime.tv_sec) + endtime.tv_nsec - starttime.tv_nsec);

        answer_file = fopen(argv[2], "w");
        for (i = 0; i < SIZE; i++)
        {
            for (int j = 0; j < SIZE; j++)
                fprintf(answer_file, "%d ", result[i][j]);
            fprintf(answer_file, "\n");
        }
        fclose(answer_file);
    }
    fclose(time_file);
}
