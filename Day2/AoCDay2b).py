f = open("input.txt","r")
score = 0
for x in f:
    actions = x.split()
    match actions[0]:
        case "A":
            match actions[1]:
                case "X":
                    score += 3 + 0
                case "Y":
                    score += 1 + 3
                case "Z":
                    score += 2 + 6
        case "B":
            match actions[1]:
                case "X":
                    score += 1 + 0
                case "Y":
                    score += 2 + 3
                case "Z":
                    score += 3 + 6
        case "C":
            match actions[1]:
                case "X":
                    score += 2 + 0
                case "Y":
                    score += 3 + 3
                case "Z":
                    score += 1 + 6
print(score)