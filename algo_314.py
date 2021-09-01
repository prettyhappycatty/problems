#lcs 動的計画法による最長共通部分文字列

def lcs(X, Y):
    m = len(X)
    n = len(Y)
    maxl = 0
    #maxs = ''
    c = [[0 for i in range(n+1)] for j in range(m+1)]
    #s = [['' for i in range(n+1)] for j in range(m+1)]
    for i in range(m):
        c[i][0] = 0
    for i in range(n):
        c[0][i] = 0
    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                c[i][j] = c[i-1][j-1]+1
    #            s[i][j] = s[i-1][j-1]+X[i]
            else:
                if c[i-1][j] >= c[i][j-1]:
                    c[i][j] = c[i-1][j]
    #                s[i][j] = s[i-1][j]
                else:
                    c[i][j] = c[i][j-1]
    #                s[i][j] = s[i][j-1]
            maxl = max(maxl, c[i][j])
    #        if len(s[i][j]) > len(maxs):
    #            maxs = s[i][j]


        lcs_str = ''
        i, j = m-1, n-1
        while i >= 0 and j >= 0:
            if X[i] == Y[j]:
                lcs_str = X[i] + lcs_str#or Y[j-1]
                i -= 1
                j -= 1
            else:
                if c[i-1][j] > c[i][j-1]:
                    i -= 1
                else:
                    j -= 1

    return maxl, lcs_str

S = input()
T = input()
l, st = lcs(S, T)
print(l)