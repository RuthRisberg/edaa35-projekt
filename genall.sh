
mkdir results
mkdir alg_answers

python3 genlist.py > inp_quicksort.txt
python3 genlist.py > inp_mergesort.txt
python3 genmatrices.py > inp_matrixmult.txt
# 
for alg in mergesort quicksort matrixmult
do
    python3 algorithms/$alg.py inp_$alg.txt alg_answers/py_$alg.txt results/py_$alg.csv

    gcc algorithms/$alg.c -O3 -march=native -o algorithms/$alg
    algorithms/$alg inp_$alg.txt alg_answers/c_$alg.txt results/c_$alg.csv
    rm algorithms/$alg

    cd algorithms
    javac $alg.java
    java $alg ../inp_$alg.txt ../alg_answers/java_$alg.txt ../results/java_$alg.csv
    rm $alg.class
    cd ..
done
