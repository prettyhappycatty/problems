N, K = map(int,input().split())
A = []

for i in range(N):
    tmp_A = int(input())
    A.append(tmp_A)
#print(len(A))
sum_a = 0
for i in range(len(A)):
    sum_a += A[i]
    if K <= sum_a:
        print(i+1)
        break
