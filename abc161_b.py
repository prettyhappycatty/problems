N, M = map(int, input().split())

A = list(map(int, input().split()))

A.sort(reverse=True)
sumA = sum(A)
border = sumA / (4*M)
#print(A)

cnt = 0
for i in range(N):
    if A[i] >= border:
        cnt += 1

#print(border,cnt)
if cnt >= M:
    print("Yes")
else:
    print("No")


