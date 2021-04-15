N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A = [A1, A2]

row = 0
sm_sum_j = 0
for i in range(N):#どのタイミングで下に移動するか
    j = 0
    sum_j = 0
    row = 0
    while j < N:
        sum_j += A[row][j]
        if j == i:
        #    print(row, j,i,  sum_j)
            row = 1
            sum_j += A[row][j]
        j += 1
    if sum_j > sm_sum_j:
        sm_sum_j = sum_j
        #print(i, sum_j)

print(sm_sum_j)