def fibDyn(n):
    fib_array = [0] * (n + 1)
    fib_array[0] = 0
    fib_array[1] = 1
    for k in range(2, n + 1):
        fib_array[k] = fib_array[k - 1] + fib_array[k - 2]
    return fib_array[n]


if __name__ == '__main__':
    print(fibDyn(10))
