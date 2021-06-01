H, W = 3,4

K = 2
A = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

def ruisekiwa(k):
    B = [[0 for i in range(W+1)] for j in range(H+1)]
    for x in range(H):
        for y in range(W):
            A[x][y] = 1 if A[x][y] > k else 0
            B[x+1][y+1] = B[x][y+1] + B[x+1][y] - B[x][y] + A[x][y]
    smallest = 10e9
    for x in range(H - K + 1):
        for y in range(H - K + 1):
            print(B[x][y+K] + B[x+K][y] + B[x][y] + B[x+K][y+K])
    return B

b = ruisekiwa(0)


print(b)