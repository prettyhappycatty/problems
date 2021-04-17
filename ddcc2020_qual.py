N = int(input())
A = list(map(int, input().split()))

sum_i, sum_j = 0, 0
i, j = 0, N-1
while i <= j:
    if sum_i < sum_j:
      sum_i += A[i]
      i += 1
    else:
      sum_j += A[j]
      j -= 1
      

print(sum_i, sum_j, A[i])

if sum_i == sum_j:
    print(0)
else:
    a = abs(sum_i - sum_j +1)//2
    print(a)