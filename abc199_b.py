N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
for j in range(1, 1001):
    flg = 0
    for i in range(N):
        #print(A[i], B[i], j)
        if A[i] <= j <= B[i]:
        #    print(i, "yes")
            flg +=1
    if flg == N:
        cnt += 1

print(cnt)

