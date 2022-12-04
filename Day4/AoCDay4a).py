def isCovered(a,b,c,d):
    first  = (a <= c) and (d <= b)
    second = (c <= a) and (b <= d)
    return first or second

f = open("input.txt", "r")
sum = 0
for x in f:
    numbers = x.split(",")
    first = numbers[0].split("-")
    second = numbers[1].split("-")
    if isCovered(int(first[0]),int(first[1]),int(second[0]),int(second[1])):
        sum += 1
print(sum)