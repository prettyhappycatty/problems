#２次元累積和

R, C, K = map(int, input().split())
s = []

for i in range(R):
    s.append(list(input()))

rui = [[0 for _ in range(C+1)] for _ in range(R+1)]
for i in range(R):
    for j in range(C):
        if s[i][j] == "o":
            rui[i+1][j+1] = rui[i][j+1] + rui[i+1][j] - rui[i][j] + 1
        else:
            rui[i+1][j+1] = rui[i][j+1] + rui[i+1][j] - rui[i][j]
for i in range(len(rui)):
    print(rui[i])
cnt = 0
for x in range(K//2-1,R-K//2+1):
    for y in range(K//2-1,C-K//2+1):
        tmp = K//2
        if (rui[x][y+tmp]-rui[x][y-tmp]>=K*2 and rui[x+tmp][y] - rui[x-tmp][y] >= K*2):
            print(x,y)
            cnt += 1
            print("+")
print(cnt)

