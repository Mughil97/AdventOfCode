left = []
right = []

with open("2024/1-a/input.txt") as f:
    for line in f.readlines():
        numbers = line.split()
        left.append(int(numbers[0].strip()))
        right.append(int(numbers[1].strip()))

left.sort()
right.sort()

diff = []

for i in range(0, 1000):
    diff.append(abs(left[i] - right[i]))


print(sum(diff))
