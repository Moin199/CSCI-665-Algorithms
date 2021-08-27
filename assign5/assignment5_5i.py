import math

def extraSpace(S, M, i, j):
    extraSpaces = M - j + i
    for x in range(i, j + 1):
        extraSpaces -= len(S[x])
    return extraSpaces


def badnessLine(S, M, i, j):
    es = extraSpace(S, M, i, j)
    if es < 0:
        return math.inf
    return es
def minBadDynamicChoice(S, M):
    cost = [math.inf for i in range(len(S))]

    choice = [[] for i in range(len(S))]

    for i in range(0, len(S)):
        if badnessLine(S, M, 0, i) != math.inf:
            cost[i] = badnessLine(S, M, 0, i)
            choice[i] = [(0, i)]
            if i == len(S) - 1:
                return 0, [(0, i)]
        else:
            min = math.inf
            choiceCanidate = []
            for k in range(0, i):
                before = cost[k]
                after = badnessLine(S, M, k + 1, i)
                if i == len(S) - 1 and badnessLine(S, M, k + 1, i) != math.inf:
                    after = 0  # Last line
                max = before if before > after else after
                if min > max:
                    choiceCanidate = choice[k] + [(k + 1, i)]
                    min = max
            choice[i] = choiceCanidate
            cost[i] = min
    return cost[len(S) - 1], choice[len(S) - 1]


def printParagraph(S, M):
    cost, choice = minBadDynamicChoice(S, M)
    for i in range(0, len(choice)):
        for x in range(choice[i][0], choice[i][1] + 1):
            print(str(S[x]), end=" ")
        print()


print(minBadDynamicChoice(["aaa", "aaa"], 6))
printParagraph(["jjjjjj", "aaa", "bb", "cc", "ff", "mm", "ddddd", "ddddd"], 6)

printParagraph(["jjjjjj"], 6)