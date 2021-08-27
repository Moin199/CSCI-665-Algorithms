import math


def extraSpace(s,m,i,j):
    space=m-j+i
    for x in range(j,i+1):
        space-=len(s[x])
    return space

def badnessLine(s,m,i,j):
    badness=extraSpace(s,m,i,j)
    if badness<0:
        return -1
    return badness

def minBad(s,m,i):
    if badnessLine(s, m, i, len(s) - 1) != -1:
        return 0

    min = math.inf

    for k in range(i + 1, len(s)):
        end = minBad(s, m, k)
        front = badnessLine(s, m, i, k - 1)
        max = end if end > front else front
        min = min if min < max else max
    return min
def main():
    S = "My name i Smita"
    sArray=[S]
    wordList=sArray[0].split()
    print(minBad(wordList,1,0))

if __name__=="__main__":
    main()

