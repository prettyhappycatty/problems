N = int(input())
A = list(map(int, input().split()))

if N == 1:
    print(int(A[0]))
    exit()

import itertools

lst = list(itertools.product([1,0], repeat=N-1))


smallest = 10**10
ar = []
ar.append([])
a = A[0]
for l in range(len(lst)):#間
    ll = lst[l] #間のビット
#    print(ll)
    #ar.append([])
    ar = []
    ar.append([])
    a = A[0]
    j = 0 #jつ目の集合
    i = 0
    ar[j].append(a)
    while i < N-1:#iつめの
        if ll[i] == 1: #切る場合
            j += 1 #インクリメント
            a = A[i+1]
            ar.append([])
            b = a
        else:
            b = A[i+1]
            #a = b
            #b = bin(int(ar[j][-1],0) ^ int(b, 0))
            #ar.append(a)
        ar[j].append(b)
        i += 1

    #print(ar)
    #print(ar1, ar2)
    #a = int(b1, 0) ^ int(b2, 0)

    ary_bs = []
    for i in range(len(ar)):
        #ret = 1
        for j in range(len(ar[i])):
            if j == 0:
                b = ar[i][j]
            else:
                b = int(bin(ar[i][j] or b), 0)
        ary_bs.append(b)

    #print("sm", smallest)
    
    #print(ary_bs)

    for i in range(len(ary_bs)):
        if i == 0:
            ret = ary_bs[i]
        else:
            ret = ary_bs[i] ^ ret

        #print("b", ret, ary_bs[i])
    smallest = min(ret, smallest)
#print(j,a)
#print(a, smallest)

print(smallest)

#print(int(bin(1 or 3),0))
#print(int(bin(3 or 1),0))
#print(int(bin(1 or 3),0) ^ int(bin(3 or 1),0))
    