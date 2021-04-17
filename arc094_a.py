A, B, C = list(map(int, input().split()))

m = max(A, B, C)

if B == m:
    a = B - A
    b = B - C
elif A == m:
    a = A - B
    b = A - C
else:
    a = C - B
    b = C - A

#print(a, b)

if abs(a-b) % 2 == 1:
    print((m*3-(A+B+C))//2 + 2)
else:
    #全部２増やすで行ける場合
    print((m*3-(A+B+C))//2)