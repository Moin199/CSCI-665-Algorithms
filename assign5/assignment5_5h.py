import math

def len_i_j(S):
    l = 0
    for s in S:
        l += len(s)
    return l


def extraSpace(S, M, i, j):
    extra_spaces = M - j + i - len_i_j(S[i:j + 1])
    return extra_spaces

def badnessLine(s,m,i,j):
    badness=extraSpace(s,m,i,j)
    if badness<0:
        return -1
    return badness

def minBadDynamic(S,M):
    cost = [math.inf for i in range(len(S))]

    for i in range(0, len(S)):
        if badnessLine(S, M, 0, i) != -1:
            cost[i] = badnessLine(S, M, 0, i)
            if i == len(S) - 1:
                return 0  # Everything fit on one line
        else:
            min = math.inf
            for k in range(0, i):
                before = cost[k]
                after = badnessLine(S, M, k + 1, i)
                if i == len(S) - 1 and badnessLine(S, M, k + 1, i) != math.inf:
                    after = 0  # Last Line
                max = before if before > after else after
                min = min if min < max else max
            cost[i] = min
    return cost[len(S) - 1]

if __name__=="__main__":
    S = "My name i Smita"
    sArray = [S]
    wordList = sArray[0].split()
    print(minBadDynamic(wordList, 10))
