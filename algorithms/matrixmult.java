import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class matrixmult {

    public static void main(String[] args) throws IOException {

        final int SIZE = 100;

        File time_file = new File(args[2]);
        FileWriter timeWriter = new FileWriter(time_file);

        timeWriter.write("index,time\n");

        for (int iter = 0; iter < 1000; iter++) {
            List<List<Integer>> matrix_a = new ArrayList<>();
            List<List<Integer>> matrix_b = new ArrayList<>();
            File infile = new File(args[0]);
            Scanner fileReader = new Scanner(infile);
            for (int i = 0; i < SIZE; i++) {
                List<Integer> line = new ArrayList<>();
                for (int j = 0; j < SIZE; j++) {
                    line.add(fileReader.nextInt());
                }
                matrix_a.add(line);
            }
            for (int i = 0; i < SIZE; i++) {
                List<Integer> line = new ArrayList<>();
                for (int j = 0; j < SIZE; j++) {
                    line.add(fileReader.nextInt());
                }
                matrix_b.add(line);
            }
            fileReader.close();

            List<List<Integer>> result = new ArrayList<>();

            long starttime = System.nanoTime();

            for (int i = 0; i < SIZE; i++) {
                List<Integer> line = new ArrayList<>();
                for (int j = 0; j < SIZE; j++) {
                    int element = 0;
                    for (int k = 0; k < SIZE; k++) {
                        element += matrix_a.get(i).get(k) * matrix_b.get(k).get(j);
                    }
                    line.add(element);
                }
                result.add(line);
            }

            long endtime = System.nanoTime();

            timeWriter.write(Integer.toString(iter) + "," + Long.toString(endtime - starttime) + "\n");

            File answerFile = new File(args[1]);
            FileWriter ansWriter = new FileWriter(answerFile);
            for (List<Integer> line : result) {
                for (int element : line) {
                    ansWriter.write(Integer.toString(element) + " ");
                }
                ansWriter.write("\n");
            }
            ansWriter.close();
        }

        timeWriter.close();
    }
}
