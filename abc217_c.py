N = int(input())
q = []
p = list(map(int, input().split()))

for i in range(N):
    q.append(-1)

for i in range(N):
    q[p[i]-1] = i+1

print(*q)