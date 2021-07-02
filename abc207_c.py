N = int(input())

T = []
L = []
R = []

for i in range(N):
    tmpT, tmpL, tmpR = map(int, input().split())
    T.append(tmpT)
    L.append(tmpL)
    R.append(tmpR)

def check(T1, L1, R1, T2, L2, R2):
    if L1 > L2:
        tmpL = L1
        L1 = L2
        L2 = tmpL
        tmpT = T1
        T1 = T2
        T2 = tmpT
        tmpR = R1
        R1 = R2
        R2 = tmpR
    #L1の方が小さいもしくはイコールとなる
    if L2 < R1:
        return True
    elif L2 == R1:
        if (T1 == 1 or T1 == 3) and (T2 == 1 or T2 == 2):
            return True
        else:
            return False
    else:
            return False


sumA =0
for i in range(N):
    for j in range(i+1, N):
        #print(i,j,T[i], L[i], R[i], T[j], L[j], R[j], check(T[i], L[i], R[i], T[j], L[j], R[j]))
        if check(T[i], L[i], R[i], T[j], L[j], R[j]):
            sumA += 1
print(sumA)


