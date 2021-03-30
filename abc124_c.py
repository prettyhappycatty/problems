S = input()

odd_1 = 0 #奇数番目を1にする場合に必要な変換数
even_1 = 0 #奇数番目を1にする場合に必要な変換数
for i in range(len(S)):
    if int(S[i]) % 2 == 1:
        if i % 2 == 0:
            odd_1 += 1
        else:
            even_1 += 1
    else:
        if i % 2 == 0:
            even_1 += 1
        else:
            odd_1 += 1

if even_1 > odd_1:
    print(odd_1)
else:
    print(even_1)