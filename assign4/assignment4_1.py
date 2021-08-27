def max2(a,b):
    """
    Finding the max without any comparison and using 2's complement logic
    where each number is represented in binary 32 bit where the 32nd bit represents
    the sign of the value.
    :param a:
    :param b:
    :return:
    """
    dif=a-b
    k=(dif>>31) & 1
    max=a-k*dif
    return max

if __name__ == '__main__':
    print(max2(124,1000))
