n = int(input())
a = list(map(int, input().split()))


sn_hiku_1_sum = 0
for i in range(n-1):
    sn_hiku_1_sum += a[i+1]-a[i]

ans = sn_hiku_1_sum/(n-1)
print(ans)
