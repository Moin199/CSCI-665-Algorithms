def mergeSort(sorted_array):
    """
    sorts the array using merge sort technique
    :param sorted_array:
    :return:
    """
    if len(sorted_array) > 1:

        mid = len(sorted_array) // 2
        left = sorted_array[:mid]
        right = sorted_array[mid:]
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_array[k] = left[i]
                i += 1
            else:
                sorted_array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            sorted_array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            sorted_array[k] = right[j]
            j += 1
            k += 1


def HasSum(array1, x):
    """
    Checks for sum after sorting the array
    :param array1:
    :param x:
    :return:
    """
    mergeSort(array1)
    left = 0
    right = len(array1) - 1
    while left < right:
        if array1[left] + array1[right] == x:
            return True
        elif array1[left] + array1[right] < x:
            left += 1
        else:
            right -= 1
    return False


def main():
    S = [6, 2, 7, 31, 0, -1, 20]
    print(HasSum(S, 9))

if __name__ == '__main__':
    main()