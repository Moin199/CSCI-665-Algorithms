def extraSpace(s,m,i,j):
    space=m-j+i
    for x in range(j,i+1):
        space-=len(s[x])
    return space

def badnessLine(s,m,i,j):
    sArray=[s]
    sWords=sArray[0].split()
    badness=extraSpace(sWords,m,i,j)
    if badness<0:
        return float('inf')
    return badness
if __name__=="__main__":
    S="A bri wrth akjsbf"
    print(badnessLine(S,0,1,2))
