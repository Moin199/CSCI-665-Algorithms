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

def partition_equal(a,l,h):
    """
    This partitions the array in terms of inequality without the equal to signature
    :param a:
    :param l:
    :param h:
    :return:
    """
    x = a[h]
    i = l-1
    j = l
    while j<h:
        if a[j] < x:
            i = i+1
            a[i],a[j] = a[j],a[i]
        j = j+1
    a[i+1],a[h]= a[h],a[i+1]
    return i+1

def iSelectHelper(arr,elem,low,high):
    """
    Helper function that recursively partitions the array and checks the
    value of the element with the various other elements of the
    newly created element.
    :param arr:
    :param elem:
    :param low:
    :param high:
    :return:
    """
    if len(arr)==0:
        return "Bad Index"
    lower_array = partition(arr,low,high)
    if elem <= lower_array:
        l = partition_equal(arr,0,lower_array)
        if elem < l:
            return iSelectHelper(arr,elem,low,l-1)
        else:
            return arr[l]
    else:
        return iSelectHelper(arr,elem,lower_array+1,high)

def iSelect(arr,elem):
    return iSelectHelper(arr,elem,0,len(arr)-1)

if __name__ == '__main__':
    print(iSelect([45,23,3154,7,64,323,45,5],1))
