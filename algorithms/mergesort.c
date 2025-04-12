#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <assert.h>

#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define LIST_LEN 3000

int main(int argc, char **argv)
{
    int original_list[LIST_LEN];
    int *list_to_sort;
    int *buf_list;
    int *temp;
    struct timespec starttime, endtime;
    int sectionlen, i, iter, sectionstart, index1, index2;
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

        list_to_sort = calloc(LIST_LEN, sizeof(int));
        memcpy(list_to_sort, original_list, LIST_LEN * sizeof(int));

        timespec_get(&starttime, TIME_UTC);

        buf_list = calloc(LIST_LEN, sizeof(int));

        sectionlen = 1;
        while (sectionlen < LIST_LEN)
        {
            for (sectionstart = 0; sectionstart < LIST_LEN; sectionstart += 2 * sectionlen)
            {
                index1 = sectionstart;
                index2 = sectionstart + sectionlen;

                for (i = sectionstart; i < MIN(sectionstart + 2 * sectionlen, LIST_LEN); i++)
                {
                    if (index2 >= MIN(sectionstart + 2 * sectionlen, LIST_LEN))
                    {
                        buf_list[i] = list_to_sort[index1];
                        index1++;
                    }
                    else if (index1 >= sectionstart + sectionlen)
                    {
                        buf_list[i] = list_to_sort[index2];
                        index2++;
                    }
                    else if (list_to_sort[index1] < list_to_sort[index2])
                    {
                        buf_list[i] = list_to_sort[index1];
                        index1++;
                    }
                    else
                    {
                        buf_list[i] = list_to_sort[index2];
                        index2++;
                    }
                }
            }

            sectionlen *= 2;
            temp = buf_list;
            buf_list = list_to_sort;
            list_to_sort = temp;
        }

        free(buf_list);

        timespec_get(&endtime, TIME_UTC);
        fprintf(time_file, "%d,%ld\n", iter, ((int)1e9) * (endtime.tv_sec - starttime.tv_sec) + endtime.tv_nsec - starttime.tv_nsec);

        answer_file = fopen(argv[2], "w");
        for (i = 0; i < LIST_LEN; i++)
        {
            fprintf(answer_file, "%d ", list_to_sort[i]);
        }
        fprintf(answer_file, "\n");
        fclose(answer_file);

        free(list_to_sort);
    }
    fclose(time_file);
}
