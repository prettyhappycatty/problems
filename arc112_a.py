#要復習

N = int(input())

for i in range(N):
    L, R = map(int, input().split())
    n=R-L*2
    if n<0:
        print(0)
        continue
    print((n+1)*(n+2)//2)