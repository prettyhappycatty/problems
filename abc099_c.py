N = int(input())

# 1.具体的に
# i=1  1  1
# i=2  2  1x2 DP[n]+DP[i-n]
# i=3  3  1x3 
# i=4  4  1x4 
# i=5  5  1x5 
# i=6  1  6
# i=7  2  6+1 
# i=8  3  6+1x2 
# i=9  1  9 
# i=10  2  9+1 
# ...
# N=35 6  9x3+6x1+1x2 
# N=36 1 6^2
# 2.一般化（再帰的に）
# 1になるタイミングはa = [1, 6*6, 9*9, 6*6*6, 6*6*6*6, 9*9*9...]
# 直近の1になるタイミングからいくつ増やしたものかを管理
# n = N - (上の配列で直近の数字)を求めて、DP[n] = 1 DP[i] = DP[i-n]+1
# i not in a: DP[i] = DP[i-a[idx-1]]+1 #ただし、それまでのidxに対して回す（1にするまとまりをどれにするかで一番小さくなるものを探索）
# i in a: DP[i] = 1
# 3.初期値
# 上述の1になるタイミング

i6 = 6 #6の乗数
i9 = 9 #9の乗数
a = [1]
i6_cnt = 0
i9_cnt = 0
while i6 < N+1:
    a.append(i6)
    i6 *= 6

while i9 < N+1:
    a.append(i9)
    i9 *= 9
a.append(i6) #ダミー
a.append(i9) #ダミー
a = sorted(a)
#print(sorted(a))

idx = 0
DP = [0 for i in range(N+1)]
for i in range(N+1):
    if i == 0:
        DP[0] = 0 #1の時の回数は1
        continue
    if a[idx] == i: #a[idx]は1からスタートする
        DP[i] = 1
        idx += 1
    else:
        min_dp = 10**7
        for j in range(1, idx+1):
            min_dp = min(DP[i-a[j-1]]+1, min_dp)
        DP[i] = min_dp
        
print(DP[N])