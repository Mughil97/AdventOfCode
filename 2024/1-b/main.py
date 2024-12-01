from collections import Counter

left = []
right = []

with open("2024/1-a/input.txt") as f:
    for line in f.readlines():
        numbers = line.split()
        left.append(int(numbers[0].strip()))
        right.append(int(numbers[1].strip()))

right_counter = Counter(right)

result = []

for i in left:
    result.append(i * right_counter.get(i, 0))


print(sum(result))
