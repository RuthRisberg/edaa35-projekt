import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class mergesort {
    public static void main(String[] args) throws IOException {

        final int LIST_LEN = 3000;

        File time_file = new File(args[2]);
        FileWriter timeWriter = new FileWriter(time_file);

        timeWriter.write("index,time\n");

        for (int iter = 0; iter < 1000; iter++) {
            List<Integer> original_list = new ArrayList<>();
            File infile = new File(args[0]);
            Scanner fileReader = new Scanner(infile);
            while (fileReader.hasNext()) {
                original_list.add(fileReader.nextInt());
            }
            fileReader.close();

            List<Integer> list_to_sort = new ArrayList<>(original_list);

            long starttime = System.nanoTime();

            List<Integer> buf_list = new ArrayList<>(original_list);

            int sectionlen = 1;
            while (sectionlen < LIST_LEN) {
                for (int sectionstart = 0; sectionstart < LIST_LEN; sectionstart += 2 * sectionlen) {
                    int index1 = sectionstart;
                    int index2 = sectionstart + sectionlen;
                    for (int i = sectionstart; i < Math.min(sectionstart + 2 * sectionlen, LIST_LEN); i++) {
                        if (index2 >= Math.min(sectionstart + 2 * sectionlen, LIST_LEN)) {
                            buf_list.set(i, list_to_sort.get(index1));
                            index1++;
                        } else if (index1 >= sectionstart + sectionlen) {
                            buf_list.set(i, list_to_sort.get(index2));
                            index2++;
                        } else if (list_to_sort.get(index1) < list_to_sort.get(index2)) {
                            buf_list.set(i, list_to_sort.get(index1));
                            index1++;
                        } else {
                            buf_list.set(i, list_to_sort.get(index2));
                            index2++;
                        }

                    }
                }
                sectionlen *= 2;
                List<Integer> temp = buf_list;
                buf_list = list_to_sort;
                list_to_sort = temp;
            }

            long endtime = System.nanoTime();

            timeWriter.write(Integer.toString(iter) + "," + Long.toString(endtime - starttime) + "\n");

            File answerFile = new File(args[1]);
            FileWriter ansWriter = new FileWriter(answerFile);
            for (int element : list_to_sort) {
                ansWriter.write(Integer.toString(element) + " ");
            }
            ansWriter.write("\n");
            ansWriter.close();
        }

        timeWriter.close();
    }
}
