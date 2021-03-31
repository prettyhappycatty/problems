A, B = list(map(int, input().split()))

cnt = 0
for i in range(A, B+1):
    s1, s5 = i // 10000, i % 10
    s2, s4 = i // 1000 % 10, i % 100 // 10
    if s1 == s5 and s2 == s4:
        cnt += 1

print(cnt)