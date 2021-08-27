def search(a, v):
    """
    searches v in array a
    returns true if found else false
    :param a:
    :param v:
    :return:
    """
    left = 0
    right = len(a) - 1
    i = 0

    while left != right:
        i += 1
        middle = (left + right) // 2
        if v == a[middle]:
            return True
        elif v < a[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return False

def main():
    arr1=[2,31,45,64,210,1000]
    print(search(arr1,45))

if __name__ == '__main__':
    main()
