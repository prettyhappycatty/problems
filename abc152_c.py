N = int(input())
P = list(map(int, input().split()))

cnt = 0
v_min = N+1
for i in range(N):
    if v_min > P[i]:
        cnt += 1
        v_min = P[i]


print(cnt)
    
