#ekiden

N = int(input())

A = []
for i in range(N):
    tmpA = list(map(int, input().split()))
    A.append(tmpA)

C = [i for i in range(len(A))]

Q = int(input())


X = []
Y = []
for i in range(Q):
    tmpX, tmpY = map(int, input().split())
    X.append(tmpX)
    Y.append(tmpY)


def checkXY(a):
    if Q == 0:
        return True
    bef = a[0]
    #print(a)
    for j in range(1, N):
        for i in range(Q):
            if bef == X[i]-1 and a[j] == Y[i]-1:
                #print(X[i],Y[i])
                return False
            elif bef == Y[i]-1 and a[j] == X[i]-1:
                #print(X[i],Y[i])
                return False
        bef = a[j]
    return True





#順列全探索
import itertools

sm_all = 10*1000 + 1

for v in itertools.permutations(C, len(C)):

    l = list(v)
    if checkXY(l) == False:
        #print(l,"false")
        continue

    #print(l,"true")
    #lに走順が入っている
    #A[iさんの][j番目区画の時間]
    #     sm = 10*100 + 1
    bef = 0
    j_sum = 0
    for j in range(len(l)):
        j_sum += A[l[j]][j]
        #print(j_sum)
    if sm_all > j_sum:
        sm_all = j_sum
    #print(sm)
#print(sm_all)
if sm_all < 1000*N+1:
    print(sm_all)
else:
    print("-1")

