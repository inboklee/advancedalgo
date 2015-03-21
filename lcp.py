def computeLCP(T1, T2):
    X = " " + T1
    Y = " " + T2
    D = [[0 for x in xrange(len(X))] for y in xrange(len(Y))]
    for i in xrange(len(Y)):
        D[i][0] = 0
    for j in xrange(len(X)):
        D[0][j] = 0
    for i in xrange(1,len(Y)):
        for j in xrange(1, len(X)):
            if (X[j] == Y[i]):
                D[i][j] = D[i-1][j-1] + 1
            else:
                D[i][j] = max(D[i-1][j], D[i][j-1])
    return D[len(T2)][len(T1)]

def computeED(T1, T2):
    X = " " + T1
    Y = " " + T2
    D = [[0 for x in xrange(len(X))] for y in xrange(len(Y))]
    for i in xrange(len(Y)):
        D[i][0] = i
    for j in xrange(len(X)):
        D[0][j] = j
    for i in xrange(1,len(Y)):
        for j in xrange(1, len(X)):
            if (X[j] == Y[i]):
                temp = D[i-1][j-1]
            else:
                temp = D[i-1][j-1] + 1
            D[i][j] = min(D[i-1][j]+1, D[i][j-1]+1, temp)
    return D[len(T2)][len(T1)]
