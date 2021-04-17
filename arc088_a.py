A, B = list(map(int, input().split()))

tmp = A
cnt = 0
while tmp <= B:
    tmp = tmp*2
    cnt += 1

print(cnt)