from collections import deque

H, W = map(int, input().split())

C = []
I = [] #int
D = []
s_h, s_w = -1, -1
g_h, g_w = -1, -1
for i in range(H):
    tmpC = input()
    C.append(tmpC)
    tmpI = []
    tmpD = []
    for j in range(W):
        tmpI.append(-1)
        tmpD.append(False)
    I.append(tmpI)
    D.append(tmpD)


for i in range(H):
    for j in range(W):
        if C[i][j] == "s":
            s_h, s_w = i, j
        if C[i][j] == "g":
            g_h, g_w = i, j

#print(C)
#print(I)

I[s_h][s_w] = 0
I[s_h][s_w] = 0
#方針　到達できない部分を-1、到達できる部分を壁を何個壊したら到達できるか？に変更する

d = deque()
d.append((s_h,s_w)) 

neigh= [(-1, 0), (0, -1), (1, 0), (0, 1)]

haji = deque()
#壊さずに到達できる範囲を求める。
while len(d) > 0:
    q = d.pop()
    #print(q)
    for nei in neigh:
        #print(q, nei)
        now_h = q[0] + nei[0]
        now_w = q[1] + nei[1]
        #print(now_h, now_w)

        if now_h == -1 or now_h == H or now_w == -1 or now_w == W:
            continue
        if I[now_h][now_w] > -1:#完了している
            continue

        if C[now_h][now_w] == "." or C[now_h][now_w] == "g":#壊さない
            I[now_h][now_w] = 0
            d.append((now_h, now_w))
            D[now_h][now_w] = True
        elif C[now_h][now_w] == "#": #壊す
            #端っこになるキューに追加
            print(haji)
            haji.append((now_h, now_w))
            D[now_h][now_w] = True
            continue

#print(I)
print(haji)


haji1 = deque() #1回壊して到達できるキュー
while len(haji) > 0:
    #print(haji)
    q = haji.pop()
    #print(q)
    for nei in neigh:
        #print(q, nei)
        now_h = q[0] + nei[0]
        now_w = q[1] + nei[1]
        #print(now_h, now_w)

        if now_h == -1 or now_h == H or now_w == -1 or now_w == W:
            continue
        if D[now_h][now_w] == True:#完了している
            continue

        if C[now_h][now_w] == "." or C[now_h][now_w] == "g":#壊さない
            if I[now_h][now_w] > 0:
                I[now_h][now_w] = min(I[q[0]][q[1]], I[now_h][now_w])
                haji1.append((now_h, now_w))
            else:
                I[now_h][now_w] = I[q[0]][q[1]]
                haji1.append((now_h, now_w))
        elif C[now_h][now_w] == "#": #壊す
            if I[now_h][now_w] > 0:
                I[now_h][now_w] = min(I[q[0]][q[1]]+1, I[now_h][now_w])
                haji1.append((now_h, now_w))
            else:
                I[now_h][now_w] = I[q[0]][q[1]]+1
                haji1.append((now_h, now_w))

        D[now_h][now_w] = True

print(haji1)
print(I)
print(I[g_h][g_w])
if -1 < I[g_h][g_w] and I[g_h][g_w] < 3:
    print("YES")
else:
    print("NO")