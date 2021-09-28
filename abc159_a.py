N , M = map(int, input().split())

# N+M個から選ぶ
# 足して偶数は、N個から2個、M個から2個選ぶパターン
if N == 1:
    n = 0
else:
    n = N*(N-1)//2
if M == 1:
    m = 0
else:
    m = M*(M-1)//2

print(n+m)
