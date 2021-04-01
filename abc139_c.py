N = int(input())
A = list(map(int, input().split()))

print(A)

m = 0 #max
s = 0 #start_index
e = s + 1 #end_index
while s < N: # (0, 5)
    print(s, e, m)
    if A[s] >= A[e]:#次に降りたつ # 10 > 4
        e = s+1
    else: #次に降りたてない
        if m < e-s-1: 
            m = e-s-1 
        s = s + 1 #初期化して次のループへ # 1
        e = s + 1

print(m)



