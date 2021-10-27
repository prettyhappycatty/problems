import math

N = int(input())
X = []
Y = []

for i in range(N):
    tmpX, tmpY = map(int, input().split())
    X.append(tmpX)
    Y.append(tmpY)

def isLine(ii,jj,kk):
    #距離が足したものになるかを確認
    dx1 = X[ii] - X[jj]
    dy1 = Y[ii] - Y[jj]
    dx2 = X[ii] - X[kk]
    dy2 = Y[ii] - Y[kk]
    if dx1*dy2 == dx2*dy1:
        return True
    return False

cnt = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1,N):
            if isLine(i,j,k) == False:
                cnt += 1

print(cnt)