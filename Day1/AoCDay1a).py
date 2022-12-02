f = open("input.txt", "r")
max = 0
i = 0
for x in f:
    if x == "\n":
        if i > max:
            max = i
        i = 0
    else:
        if x.strip():
            n = int(x)
            i = i + int(n)
print (max)