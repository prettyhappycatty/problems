N, Q = map(int, input().split())
A = list(map(int, input().split()))

B = []
sumA = 0
for i in range(N-1):
    B.append(A[i+1]-A[i])
    sumA += abs(A[i+1]-A[i])

##print(sumA)
#print(len(B)) #※BはNー2までしかない
#print(B)
#print("start")


for i in range(Q):
    tmpL, tmpR, tmpV = map(int, input().split())
    mae = 0
    ato = 0
    if tmpL > 1:
        mae += abs(B[tmpL-2])
        B[tmpL-2] += tmpV
        ato += abs(B[tmpL-2])
    if tmpR < len(B)+1:
        mae += abs(B[tmpR-1])
        B[tmpR-1] -= tmpV
        ato += abs(B[tmpR-1])
    
    #print(B)
    sumA += ato - mae
    #print("L=",tmpL-2, "R=",tmpR-1, "V=",tmpV, "mae=",mae,"ato=",ato)
    #sumA += ato - mae
    print(sumA)