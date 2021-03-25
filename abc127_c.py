N, M = list(map(int, input().split()))

L_max = 0
R_min = N
for i in range(M):
    L, R = list(map(int, input().split()))
    if L_max < L:
        L_max = L
    if R_min > R:
        R_min = R

#print(L_max, R_min)
if L_max > R_min:
    print(0)
else:
    print(R_min-L_max+1)