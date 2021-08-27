def select(arr,elem):
    if len(arr)==0:
        return "Bad Index"
    x=arr[0]
    l=[i for i in arr if i<x]
    s = [i for i in arr if i == x]
    m=[i for i in arr if i>x]
    if elem<len(l):
        return select(l,elem)
    elif len(l)<=elem and elem<(len(l)+len(s)):
        return x
    else:
        return select(m,elem-(len(l)+len(s)))

if __name__ == '__main__':
    print(select([2,1,4,6,5,3,5,6,78,1],3))

