def matrix_chain_order(p):
    n = len(p) - 1

    m = [[0 for x in range(0, n)] for y in range(0, n)]
    s = [[0 for x in range(0, n)] for y in range(0, n)]

    for i in range(0, n):
        m[i][i] = 0

    # compute smallest matrix costs first
    # for chains of length 2 to n
    for l in range(2, n + 1):
        for i in range(0, n - l + 1):
            j = i + l - 1  # j is the endpoint of the chain
            if i < j:  # skip the i > j cases since we must multiply in order
                # cost values
                c = [m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1] for k in range(i, j)]

                # get minimum index and value from costs
                (s[i][j], m[i][j]) = min(enumerate(c), key=lambda x: x[1])

                print("A_%d" % i, "A_%d" % j, " = ", [m[i][k] + m[k + 1][j] for k in range(i, j)], '+', p[i], '*', [p[k + 1] for k in range(i, j)], '*', p[j + 1], " = ", [x for x in enumerate(c)])

                s[i][j] = s[i][j] + i + 1  # correct our s value (count from 1, offset by i because of enumerate)

    return m, s


def print_optimal_parens(s, i, j):
    if i == j:
        print("A_%d" % (i + 1), end=' ')
    else:
        print("(", end=' ')
        print_optimal_parens(s, i, s[i][j] - 1)
        print_optimal_parens(s, s[i][j], j)
        print(")", end=' ')


m, s = matrix_chain_order([10, 5, 2, 20, 12, 4, 60])

print_optimal_parens(s, 0, 5)
