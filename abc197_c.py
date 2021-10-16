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

    print(ar)
    #print(ar1, ar2)
    #a = int(b1, 0) ^ int(b2, 0)
    for i in range(len(ar)):
        for j in range(len(ar[i])):
            if j == 0:
                b = ar[i][j]
            else:
                b = ar[i][j] or b
        if i == 0:
            ret = b
        else:
            ret = ret ^ b
#        print("b", ret)

    smallest = min(ret, smallest)
    #print("sm", smallest)
    
#print(j,a)
#print(a, smallest)

print(smallest)

#print(int(bin(7 ^ 5 ^ 1),0))
#print(int(bin(7),0) ^ int(bin(5 or 7),0))
    