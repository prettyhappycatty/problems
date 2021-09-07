N = int(input())
A = list(map(int, input().split()))

#A_sort = sorted(A, reverse=True)

sum_fumidai = 0
bef = 0
for i in range(N):
    if bef > A[i]:
        fumidai = bef - A[i]
        sum_fumidai += fumidai
        A[i] += fumidai
    bef = A[i]

print(sum_fumidai)