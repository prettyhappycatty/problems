X, K, D = map(int, input().split())

if X < 0:
    X = -X

plus = X % D
minus = abs(plus - D)

times = X // D #Kの偶奇が一致する場合にplus, 一致しない場合にminus
#print(plus, minus)
if K >= times:
    if times % 2 == K % 2:
        print(plus)
    else:
        print(minus)
else:
    print(X - K*D)