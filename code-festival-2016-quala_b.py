N = int(input())
A = list(map(int, input().split()))

friendly = {}
paired =[]
cnt = 0
for i in range(N):
    friendly[i] = A[i]-1
    if A[i]-1 in friendly.keys() and i in paired:
        if friendly[A[i]-1] == i:
            cnt += 1
            paired.append(A[i]-1)
            paired.append(i)
print(cnt)