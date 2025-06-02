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
            stat["total"] = len(contents)
            for char in contents:
                if char in "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM":
                    stat["alphnumeric"] += 1
                elif char in " \n":
                    stat["whitespace"] += 1
                else:
                    stat["special"] += 1
                    if char in "()[]{}":
                        stat["()[]{}"] += 1
                    elif char in "?%#&":
                        stat["?%#&"] += 1
                    elif char in "><=":
                        stat["<>="] += 1
                    else:
                        stat[char] += 1
        stats[alg][lang] = stat
        allkeys.update(stat.keys())

allkeys = list(sorted(allkeys - {"total"}))
# print("\t" + "\t\t\t".join(algs))
print("\tpython\tjava\tc\t")


## Prints the data formatted for a Typst table

print("    [total],", end="")
for lang in ["py", "java", "c"]:
    print(" [" + str(sum([stats[alg][lang]["total"] for alg in algs])) + "],", end='')
# print("", end="\t")
print()

for key in allkeys:
    print("    ["+key+"],", end="")
    for lang in ["py", "java", "c"]:
        count = sum([stats[alg][lang][key] for alg in algs])
        total = sum([stats[alg][lang]["total"] for alg in algs])
        print(f" [{count} \\ ({(100 * count / total):.1f}%)],", end='')
    # print("", end="\t")
    print()
