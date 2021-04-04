A, B, K = list(map(int, input().split()))

sm = []
bg = []
for i in range(0, K):
    if A+i <= B:
        sm.append(A+i)
    if B-i >= A:
        bg.append(B-i)

#print(sm, bg)

# リスト同士の結合
sm.extend(bg)
#print(sm)

# 重複を除外する
sm=set(sm)
#print(sm)


for i in sorted(sm):
    print(i)