f = open("input.txt", "r")
calories = []
i = 0
for x in f:
    if x == "\n":
        calories.append(i)
        i = 0
    else:
        if x.strip():
            n = int(x)
            i = i + int(n)
calories.sort(reverse=True)
print(calories[0] + calories[1] + calories[2])