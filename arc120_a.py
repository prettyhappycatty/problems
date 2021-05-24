N = int(input())
A = list(map(int, input().split()))

max_a2 = [0 for i in range(N)]

ret = []

max_a = 0
sum_a = 0
sum_a_sum = 0
for i in range(0, N):
    if max_a < A[i]:
        max_a = A[i]
    sum_a += A[i]
    sum_a_sum += sum_a
    nm = (i+1)*max_a
    #print(sum_a_sum, max_a, i+1)
    print(nm+sum_a_sum)
    #print(sum_a_sum)


