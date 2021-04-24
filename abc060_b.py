A, B, C = list(map(int, input().split()))

i = 1
timesA = i*A
flg = 0
while i <= B:
    if timesA % B == C:
        flg = 1
        break
    i += 1
    timesA = i*A

if flg == 0:
    print('NO')
else:
    print('YES')