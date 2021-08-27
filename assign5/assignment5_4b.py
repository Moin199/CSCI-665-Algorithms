def knapsack(vwpair, capacity):
    """
        Returning the maximum of the knapsack using dynamic programming
        :param vwpair: Dictionary
        :param capacity: Capacity of the knapsack
        :return: max value of knapsack
        """
    key = list(vwpair.keys())
    values = list(vwpair.values())
    n = len(vwpair)
    K = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif values[i - 1] <= w:
                K[i][w] = max(K[i - 1][w],key[i - 1]
                              + K[i - 1][w - values[i - 1]]
                              )
            else:
                K[i][w] = K[i - 1][w]
    return K[n][capacity]


if __name__ == '__main__':
    print(knapsack({10:20,1:2,12:5},5))


