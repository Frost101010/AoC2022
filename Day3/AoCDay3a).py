def getRucksackValue(a):
    intersection = set(a[:len(a)//2]).intersection(a[len(a)//2:])
    value = 0
    for x in intersection:
        if x.islower():
            value += ord(x) - 96
        else:
            value += ord(x) - 38
    return value

f = open("input.txt", "r")
sum = 0
for x in f:
    sum += getRucksackValue(x)
print (sum)