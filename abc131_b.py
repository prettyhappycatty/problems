N, L = map(int, input().split())

z_min = 10**9
for i in range(N):
    #print(L+i)
    if z_min > abs(L+i):
        z_min = abs(L+i)
        #print(z_min)
        z_i = i
#print(z_i)

ans = 0
for i in range(N):
    if z_i != i:
        ans += L+i
        #print(L+i, ans)

print(ans)

