#TLE

K, Q = map(int, input().split())

A = list(map(int, input().split()))

Q_list = []
for i in range(Q):
    Q_tmp = int(input())
    Q_list.append(Q_tmp)


A_dic = {}
for i in range(K):
    A_dic[A[i]] = True


#print(A)
def ruisekiwa(k):
    B = [0 for i in range(K+1)]
    #print(B)
    for x in range(K):
        #print(x)
        a_tmp = 1 if A[x] <= k else 0
        B[x+1] = B[x] + a_tmp
    #print(B)
    return B[K]

for i in range(Q):
    tmp = Q_list[i]
    c = ruisekiwa(tmp) #それ未満の個数が何個
    #みまんの数が何個
    d = tmp + c
    #print(tmp,c, d)
    while d < Q_list[i] or d in A_dic.keys():
        tmp = tmp + 1
        c = ruisekiwa(tmp) #それ未満の個数が何個
        d = tmp + c
    #    print(tmp,c, d)

    print(d)

