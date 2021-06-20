#余事象を使う問題
H, W = list(map(int, input().split()))

H_sum = [0]*H
W_sum = [0]*W

ary = []
#print(W, H)


for i in range(H):
    tmp = list(map(int, input().split()))
    ary.append(tmp)
    for j in range(W):
        #print(i,j, W)
        H_sum[i] += tmp[j] 
        W_sum[j] += tmp[j]
     

for i in range(H):
    tmp_ary = []
    for j in range(W):
        #print(H_sum[i], W_sum[j], ary[i][j])
        tmp_ary.append(H_sum[i]+W_sum[j]-ary[i][j])
    print(*tmp_ary)
        
