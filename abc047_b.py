W, H, N = map(int, input().split())

R = [[ False for i in range(W)] for j in range(H)]

for i in range(N):
    x, y, a = map(int, input().split())
    if a == 2:
        for j in range(x, W):
            for k in range(H):
                R[k][j] = True
    elif a == 1:
        for j in range(0, x):
            for k in range(H):
                R[k][j] = True
    elif a == 4:
        for j in range(y,H):
            for k in range(W):
                R[j][k] = True
    elif a == 3:
        for j in range(0, y):
            for k in range(W):
                R[j][k] = True

#print(R)

cnt = 0
for i in range(H):
    for j in range(W):
        if R[i][j] == False:
            cnt += 1

print(cnt)




