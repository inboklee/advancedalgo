
def allsuffixes(T):
    result = []
    for x in xrange(len(T)):
        result.append(T[x:])
    return result

def buildSA(T):
    temp = {}
    S = allsuffixes(T)
    for x in xrange(len(S)):
        temp[S[x]] = x
    S.sort()
    result = []
    for x in S:
        result.append(temp[x])
    return result

def computeLCP(T1, T2):
    n = min(len(T1), len(T2))
    count = 0
    for i in xrange(n):
        if (T1[i] == T2[i]):
            count = count + 1
        else:
            break
    return count

def buildLCP(T, SA):
    result = [-1]
    for i in xrange(1, len(T)):
        result.append(computeLCP(T[SA[i-1]:], T[SA[i]:]))
    return result
