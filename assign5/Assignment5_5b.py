def extraSpace(s,m,i,j):
    space=m-j+i
    for x in range(j,i+1):
        space-=len(s[x])
    return space
if __name__ == '__main__':
    S="A bri wrth akjsbf"
    sArray=[S]
    wordList=sArray[0].split()
    print(extraSpace(wordList,10,1,2))

    # print(extraSpace(["My","asdw","qwdwqd","tre"],10,2,1))