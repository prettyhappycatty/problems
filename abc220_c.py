N = int(input())
A = list(map(int, input().split()))
X = int(input())

S = []
sumA = 0
for i in range(N):
    sumA += A[i]
    S.append(sumA)

#print(S)
#print(S[-1])
#Xまでに配列が何個入るか

times = X // S[-1]
rest = X % S[-1]

sumB = 0
for i in range(N):
    rest -= A[i]
    if rest < 0:
        print(1+i+times*N)
        exit()


