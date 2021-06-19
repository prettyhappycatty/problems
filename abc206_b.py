N = int(input())

if N == 1:
    print(N)

for i in range(N):
    a = i*(i+1)//2
    if a >= N:
        print(i)
        exit()
