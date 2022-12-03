def getRucksackValue(a,b,c):
    intersection = set(a).intersection(b).intersection(c)
    value = 0
    for x in intersection:
        if x.islower():
            value += ord(x) - 96
        else:
            value += ord(x) - 38
    return value

f = open("input.txt", "r")
index = 0
sum = 0
a = ""
b = ""
c = ""
for x in f:
    if index == 0:
        a = x.strip()
        index += 1
    elif index == 1:
        b = x.strip()
        index += 1
    else:
        c = x.strip()
        index = 0
        sum += getRucksackValue(a,b,c)
print (sum)