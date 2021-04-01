N = int(input())
A = list(map(int, input().split()))

#print(A)

m = 0 #max
s = 0 #start_index
bef = s
e = s + 1 #end_index
i = 0
while e < N: # (0, 5)
#    print(s, e, bef, e-s,m, A[s], A[bef], A[e])
    if A[bef] >= A[e]:#次に降りたつ # 10 > 4
        bef = e
        e += 1
    else: #次に降りたてない
        if m < e-s-1: 
            m = e-s-1
        s = e #初期化して次のループへ # 1
        bef = s
        e = s + 1
    if i > 1000000:
        break
if m < e-s-1: 
    m = e-s-1

print(m)



