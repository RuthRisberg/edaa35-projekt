import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class quicksort {

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

            sort(list_to_sort, 0, LIST_LEN - 1);

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

    private static void sort(List<Integer> arr, int lo, int hi) {
        int pivot = arr.get(lo);
        int loindex = lo + 1;
        int hiindex = hi;
        int temp;

        if (hi <= lo)
            return;

        while (loindex <= hiindex) {
            if (arr.get(loindex) > pivot) {
                temp = arr.get(loindex);
                arr.set(loindex, arr.get(hiindex));
                arr.set(hiindex, temp);
                hiindex--;
            } else
                loindex++;
        }

        temp = arr.get(lo);
        arr.set(lo, arr.get(hiindex));
        arr.set(hiindex, temp);

        sort(arr, lo, hiindex - 1);
        sort(arr, loindex, hi);
    }
}
