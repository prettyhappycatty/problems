H, W, X, Y = list(map(int, input().split()))

S = []

for i in range(H):
    tmp = input()
    S.append(tmp)

#S[x][y]でアクセス

flg = [1,1,1,1]#上下左右カウントするか
X = X-1
Y = Y-1
i = 1
j = 1
cnt = 1 #自身の数を最初に足しておく
while (0 <= X+i < H or 0 <= X-i < H ) and (flg[0] == 1 or flg[1] == 1):
    if X+i < H and S[X+i][Y] == '.' and  flg[0] == 1:
        #print(X+i, Y)
        cnt += 1
    else:
        flg[0] = 0
    
    if 0 <= X-i and S[X-i][Y] == '.' and  flg[1] == 1:
        #print(X-i, Y)
        cnt += 1
    else:
        flg[1] = 0
    i += 1

i = 1
while (0 <= Y+i < W or 0 <= Y-i < W ) and (flg[2] == 1 or flg[3] == 1):

    if Y+i < W and S[X][Y+i] == '.' and  (flg[2] == 1):
        #print(X, Y+1)
        cnt += 1
    else:
        flg[2] = 0
    
    if 0 <= Y-i  and S[X][Y-i] == '.' and  (flg[3] == 1):
        #print(X, Y-i)
        cnt += 1
    else:
        flg[3] = 0
    i += 1

print(cnt)