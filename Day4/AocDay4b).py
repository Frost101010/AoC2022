def isCovered(a,b):
    return not set(a).intersection(b)

f = open("input.txt", "r")
sum = 0
for x in f:
    numbers = x.split(",")
    first = numbers[0].split("-")
    second = numbers[1].split("-")
    a = list(range(int(first[0]),int(first[1])))
    if not isCovered(list(range(int(first[0]),(int(first[1]) + 1))), list(range(int(second[0]),(int(second[1]) + 1)))):
        sum += 1
print(sum)