import random

random.seed(1)
size = 100

for i in range(size):
    print(*[random.randint(0, 999) for j in range(size)])

print()

for i in range(size):
    print(*[random.randint(0, 999) for j in range(size)])
