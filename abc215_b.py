N = int(input())

mul = 1
cnt = 0
while mul <= N:
    cnt += 1
    mul *= 2

print(cnt-1)
