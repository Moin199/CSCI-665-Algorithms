def multiply(matrix1, matrix2):
    """
    Matrix multiplication
    :param matrix1:
    :param matrix2:
    :return:
    """
    x1=matrix1[0][0]*matrix2[0][0]+matrix1[0][1]*matrix2[1][0]
    x2 = matrix1[0][0] * matrix2[0][1] + matrix1[0][1] * matrix2[1][1]
    x3= matrix1[1][0] * matrix2[0][0] + matrix1[1][1] * matrix2[1][0]
    x4 = matrix1[1][0] * matrix2[0][1] + matrix1[1][0] * matrix2[1][1]

    return [[x1,x2],[x3,x4]]

def raise_to_n(matrix, n):
    """
    Raising a matrix to n
    :param matrix:
    :param n:
    :return:
    """
    if n==1:
        return matrix
    else:
        result=raise_to_n(matrix, n // 2)
        if n%2==0:
            return multiply(result,result)
        else:
            result1=multiply(result,matrix)
            return multiply(result,result1)


def fibPow(n):
    """
    Caller function to calculate fibonacci numbers
    :param n:
    :return: nth fibonacci Number
    """
    L_matrix = [[0,1], [1,1]]
    result=raise_to_n(L_matrix, n)
    return result[0][1]
if __name__ == '__main__':
    print(fibPow(21))
