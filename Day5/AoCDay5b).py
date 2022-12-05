stacks = []
stacks.append(["Z", "P", "M", "H", "R"])
stacks.append(["P", "C", "J", "B"])
stacks.append(["S", "N", "H", "G", "L", "C", "D"])
stacks.append(["F", "T", "M", "D", "Q", "S", "R", "L"])
stacks.append(["F", "S", "P", "Q", "B", "T", "Z", "M"])
stacks.append(["T", "F", "S", "Z", "B", "G"])
stacks.append(["N", "R", "V"])
stacks.append(["P", "G", "L", "T", "D", "V", "C", "M"])
stacks.append(["W", "Q", "N", "J", "F", "M", "L"])

f = open("input.txt", "r")

def move(number, a, b):
    c = []
    for _ in range(number):
        c.append(stacks[a].pop())
    for _ in range(number):
        stacks[b].append(c.pop())

for x in f:
    line = x.split()
    move(int(line[1]),int(line[3]) - 1,int(line[5]) - 1)

for x in stacks:
    print(x.pop())