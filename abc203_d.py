N, K = map(int, input().split())

A = []
max_A = 0


lim = K*K //2 + 1

for i in range(N):
    tmpA = list(map(int,input().split()))
    for j in range(len(tmpA)):
        if max_A < tmpA[j]:
            max_A = tmpA[j]
    A.append(tmpA)

#print(A)
def ruisekiwa(k):
    B = [[0 for i in range(N+5)] for j in range(N+5)]
    #print(B)
    for x in range(N):
        for y in range(N):
            a_tmp = 1 if A[x][y] > k else 0
            B[x+1][y+1] = B[x][y+1] + B[x+1][y] - B[x][y] + a_tmp
    #print(k, B)
    #smallest = 10e9
    ext = False
    for x in range(N - K + 1):
        for y in range(N - K + 1):
            tmp_med =  - B[x][y+K] - B[x+K][y] + B[x][y] + B[x+K][y+K]
            #print(B)

            if tmp_med < lim:
                #print(True)
                ext = True
    return ext

#for i in range(10):
    #print(i)
#    print(i, ruisekiwa(i))
#        exit()

def getmed(k,ary):#二分探索
    #rui = ruisekiwa(k)
    #print(rui)
    ok,ng = -1,10**9+1

    while ng-ok>1:
        m = (ng+ok)//2
#        print(ok,ng)
        judge =ruisekiwa(m)
#        print(m, judge)
        if judge:
            ng = m
        else:
            ok = m

    return ng

right = getmed(K, A)

print(right)
