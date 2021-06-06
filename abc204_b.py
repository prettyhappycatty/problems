N = int(input())

A= list(map(int, input().split()))
mi = 0
for i in range(N):
    if A[i] > 10:
        mi += A[i] - 10

print(mi)
        

