X, A, B = map(int, input().split())

#想定解？
cnt = 0
for a in range(A+1):
    b = X - a*100# X円からa枚*100円を引いたときの残り
    if b % 10 == 0 and b // 10 <= B and b >= 0: #10で割り切れるかつ b // 10 が0枚〜B枚の範囲内
        cnt +=1

print(cnt)

#全探索
cnt2 = 0
for i in range(A+1):
    for j in range(B+1):
        if i*100 + j*10 == X:
            cnt2 += 1
print(cnt2)