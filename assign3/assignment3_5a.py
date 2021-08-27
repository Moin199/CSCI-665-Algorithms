def sortedHasSum(array, x):
    """
    returns false if sum is not present eles true
    :param array: 
    :param x: 
    :return: 
    """
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] + array[right] == x:
            return True
        elif array[left] + array[right] < x:
            left += 1
        else:
            right -= 1
    return False


def main():
    sorted_array = [-10, 2, 11, 1, 5, 6]
    print(sortedHasSum(sorted_array, 12))

if __name__ == '__main__':
    main()