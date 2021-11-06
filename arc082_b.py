N = int(input())

p = list(map(int, input().split()))

def swap(i,j):
    return j, i

cnt = 0
for i in range(N):
    if i+1 < N and p[i] == i+1:
        p[i], p[i+1] = swap(p[i], p[i+1])
        cnt += 1
    elif i+1 == N and p[i] == i+1:
        p[i], p[i-1] = swap(p[i], p[i-1])
        cnt += 1

print(cnt)