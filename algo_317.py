# 発電計画問題
# t-1秒ではオフだった時、以前にすでに得られた利益が存在するのでそれをdpとしてもっている、
# それ以降で一番多く利益を出せるもの(t秒からT秒までの)を足す。それをdp[T]とする。

T = int(input())
 
g = []
 
dp = [0 for _ in range(T+2)]
# T-1 秒ではオフだった場合の総利得の最大値
 
for i in range(T):
    tmp_g = list(map(int, input().split()))
    ar = [0]
    ar.extend(tmp_g)
    g.append(ar)

#print(g)

for t in range(T+2):
    tmpdp = 0
    for i in range(t):
        for j in range(i+1,t):
            #t=i以降で、i~jまでのうちで一番Valueが高いものをたす
            #print(g[i][j])
            tmpdp = max(tmpdp, dp[i] + g[i][j])
            #print("T=",t,"i,j=",i,j,"g=",g[i][j],tmpdp)
    dp[t] = tmpdp

print(dp[T+1])