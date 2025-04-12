#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <assert.h>

#define LIST_LEN 3000

void quicksort(int *arr, int lo, int hi)
{
    int pivot;
    int loindex = lo + 1;
    int hiindex = hi;
    int temp;

    if (lo >= hi)
        return;

    pivot = arr[lo];

    while (loindex <= hiindex)
    {
        if (arr[loindex] > pivot)
        {
            temp = arr[loindex];
            arr[loindex] = arr[hiindex];
            arr[hiindex] = temp;
            hiindex--;
        }
        else
            loindex++;
    }

    temp = arr[lo];
    arr[lo] = arr[hiindex];
    arr[hiindex] = temp;

    quicksort(arr, lo, hiindex - 1);
    quicksort(arr, loindex, hi);
}

int main(int argc, char **argv)
{
    int original_list[LIST_LEN];
    int list_to_sort[LIST_LEN];
    struct timespec starttime, endtime;
    int i, iter;
    FILE *input_file, *answer_file, *time_file;

    time_file = fopen(argv[3], "w");

    fprintf(time_file, "index,time\n");

    for (iter = 0; iter < 1000; iter++)
    {
        input_file = fopen(argv[1], "r");
        for (i = 0; i < LIST_LEN; i++)
        {
            fscanf(input_file, "%d", &original_list[i]);
        }
        fclose(input_file);

        memcpy(list_to_sort, original_list, LIST_LEN * sizeof(int));

        timespec_get(&starttime, TIME_UTC);

        quicksort(list_to_sort, 0, LIST_LEN - 1);

        timespec_get(&endtime, TIME_UTC);
        fprintf(time_file, "%d,%ld\n", iter, ((int)1e9) * (endtime.tv_sec - starttime.tv_sec) + endtime.tv_nsec - starttime.tv_nsec);

        answer_file = fopen(argv[2], "w");
        for (i = 0; i < LIST_LEN; i++)
        {
            fprintf(answer_file, "%d ", list_to_sort[i]);
        }
        fprintf(answer_file, "\n");
        fclose(answer_file);
    }
    fclose(time_file);
}
