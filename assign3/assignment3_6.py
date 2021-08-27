def partition(a,l,h):
    """
    arranges the array
    :param a:
    :param l:
    :param h:
    :return:
    """
    x = a[h]
    i = l-1
    j = l
    while j<h:
        if a[j] <= x:
            i = i+1
            a[i],a[j] = a[j],a[i]
        j = j+1
    a[i+1],a[h]= a[h],a[i+1]
    return i+1

def qs_helper(a, l, h):
    """
    recursively sorts the array a
    :param a:
    :param l:
    :param h:
    :return:
    """
    while l<=h:
        m = partition(a,l,h)
        if (m - l < h - m):
            qs_helper(a, l, m - 1)
            l = m + 1
        else:
            qs_helper(a, m + 1, h)
            h = m - 1

def quicksort(a):
    qs_helper(a, 0, len(a) - 1)

def main():
    a = [12,34,5,6,7,83,8,7,4]
    quicksort(a)
    print(a)
if __name__ == '__main__':
    main()