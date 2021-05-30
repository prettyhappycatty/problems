N, K = map(int, input().split())

sumN0K = 0
for i in range(1, N+1):
    for j in range(1, K+1):
        sumN0K += i*100+j*1

print(sumN0K)
