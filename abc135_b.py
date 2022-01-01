N = int(input())
p = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if p[i]-1 != i:
        cnt += 1

if cnt <= 2:
    print("YES")
else:
    print("NO")