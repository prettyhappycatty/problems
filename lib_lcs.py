#lcs 動的計画法による最長共通部分文字列

def lcs(X, Y):
    m = len(X)
    n = len(Y)
    maxl = 0
    maxs = ''
    c = [[0 for i in range(n)] for j in range(m)]
    s = [['' for i in range(n)] for j in range(m)]
    for i in range(m):
        c[i][0] = 0
    for i in range(n):
        c[0][i] = 0
    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                c[i][j] = c[i-1][j-1]+1
                s[i][j] = s[i-1][j-1]+X[i]
            else:
                if c[i-1][j] >= c[i][j-1]:
                    c[i][j] = c[i-1][j]
                    s[i][j] = s[i][j] + s[i-1][j]
                else:
                    c[i][j] = c[i][j-1]
                    s[i][j] = s[i][j] + s[i][j-1]
            maxl = max(maxl, c[i][j])
            if len(s[i][j]) > len(maxs):
                maxs = s[i][j]
    return maxl, maxs

print(lcs('abcbdab', 'abc'))