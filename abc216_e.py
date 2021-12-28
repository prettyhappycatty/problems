N, K = map(int, input().split())
A = list(map(int, input().split()))

A_rev = sorted(A, reverse=True)
A_rev.append(0)

#print(A_rev)

sa = [] #楽しさの最大との差を足していったもの 
tmp_sa = 0
A_max = A_rev[0] #楽しさの最大 
for i in range(N+1):
    tmp_sa += A_max-A_rev[i]
    sa.append(tmp_sa)

sa2 = [0]
for i in range(N):
    sa2.append((sa[i+1] - sa[i])*(i+1))

#print(sa2)

ans = 0
for i in range(1, N+1):
    #print(K, sa2[i])
    if K > sa2[i]:
        #print("(", A_rev[i-1], "+" ,(A_rev[i]+1) , ")*(", A_rev[i-1], "-",A_rev[i], ")//2*", i)
        ans += (A_rev[i-1] + (A_rev[i]+1))*(A_rev[i-1] - A_rev[i])*i//2
    else:#途中で止める必要がある場合
        #A_rev[i]を途中で止めるところまでに変える
        #足す最後の個数(A_rev[i]+1)を途中で止めるところまでに変える
        #かけるiを、単純にかけるわけではなくて途中だったら途中にする
        sa_K = K-sa2[i-1]
        #print(sa_K)#最後のスロットで何個まで使う必要があるか
        #print(sa_K // i)#最後のスロットで使うのは何ターン分か
        #print("lot", A_rev[i-1] - sa_K // i)#最後のスロットでこの数字まで行く
        tmp_last_slot_val = A_rev[i-1] - sa_K // i
        #print(sa_K % i)#余りはあるか？

        #print("(", A_rev[i-1], "+" ,(tmp_last_slot_val-1) , ")*(", A_rev[i-1], "-",tmp_last_slot_val, ")//2*", i)
        ans += (A_rev[i-1] + tmp_last_slot_val)*(A_rev[i-1]-tmp_last_slot_val)*i//2
        ans += (sa_K % i) * (tmp_last_slot_val+1)
        break

    #print(ans)

print(ans)