import itertools

N = int(input())
#A = list(map(int, input()))
A = [N-i for i in range(N)]
A_perm = list(itertools.permutations(A))
B = []
mi =  N*(N +1) / 2
for j in range(len(A_perm)):
    tmp = A_perm[j]
    su = 0
    for i in range(N):
        tmp = tmp[i] % A[i]
        B.append(tmp)
        su += tmp
    if su < mi:
        mi = su
print(mi)