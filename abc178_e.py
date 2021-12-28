#マンハッタン距離
# 45度回転、　z=x+y, w=x-yとしてO(N)で最大値と最小値が求まる


N = int(input())

z_max = -10**9*2
z_min = 10**9*2
w_max = -10**9*2
w_min = 10**9*2


for i in range(N):
    x,y = map(int, input().split())
    z = x + y
    w = x - y
    z_max = max(z_max, z)
    z_min = min(z_min, z)
    w_max = max(w_max, w)
    w_min = min(w_min, w)

print(max(z_max-z_min, w_max-w_min))
