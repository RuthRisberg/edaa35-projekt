from collections import defaultdict
algs = ["matrixmult", "mergesort", "quicksort"]
langs = ["py", "java", "c"]

stats = {}
allkeys = set()
for alg in algs:
    stats[alg] = {}
    for lang in langs:
        stat = defaultdict(lambda:0)
        with open("algorithms/"+alg+"."+lang) as f:
            contents = f.read()
            for char in contents:
                if char in "1234567890":
                    stat["digit"] += 1
                elif char in "qwertyuiopasdfghjklzxcvbnm":
                    stat["letter"] += 1
                elif char in "QWERTYUIOPASDFGHJKLZXCVBNM":
                    stat["LETTER"] += 1
                elif char == "\n":
                    stat["newline"] += 1
                elif char == " ":
                    stat["space"] += 1
                elif char == "\t":
                    stat["tab"] += 1
                elif char in "()[]{}":
                    stat["()[]{}"] += 1
                elif char in "?%#&":
                    stat["?%#&"] += 1
                elif char in "><=":
                    stat["<>="] += 1
                else:
                    stat[char] += 1
        stats[alg][lang] = stat
        allkeys.update(stat.keys())

allkeys = list(allkeys)
print("\t\t" + "\t\t".join(algs))
print("\tpython\tjava\tc\t"*3)
for key in allkeys:
    print(key, end="\t")
    for alg in algs:
        for lang in ["py", "java", "c"]:
            print(stats[alg][lang][key], end='\t')
        print("", end="\t")
    print()
