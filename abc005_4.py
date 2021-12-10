#2次元の累積和

N = int(input())
D = []

for i in range(N):
    tmpD = list(map(int, input().split()))
    D.append(tmpD)


#print(D)

D_sum = [[0 for _ in range(N+1)]]
for i in range(N):
    d_sm_tmp = [0]
    for j in range(N):
        d_sm_tmp.append(d_sm_tmp[j] + D[i][j])
    D_sum.append(d_sm_tmp)

#print(D_sum)

for i in range(1,N+1):
    for j in range(N+1):
        D_sum[i][j] += D_sum[i-1][j]

tako = [0 for _ in range((N+1)*(N+1))]
for i in range(N):
    for j in range(N):
        for k in range(i,N+1):
            for l in range(j, N+1):
              t = D_sum[k][l] - D_sum[k][j] - D_sum[i][l] + D_sum[i][j]
              tako[(l-j)*(k-i)] = max(tako[(l-j)*(k-i)], t)

#print(tako)

for i in range(1, len(tako)):
    if tako[i-1] > tako[i]:
        tako[i] = tako[i-1]

#print(tako)

Q = int(input())
for i in range(Q):
    P = int(input())
    print(tako[P])
#print(D_sum)
