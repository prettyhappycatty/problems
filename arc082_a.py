N = int(input())
a = list(map(int, input().split()))

range_set = [1,0, -1]
cnt = {}

for i in range(N):
    for offset in range_set:
        off = a[i]-1+offset
        if off not in cnt.keys():
            cnt[off] = 1
        else:
            cnt[off] += 1

max_cnt = 0
for k in cnt.keys():
    if cnt[k] > max_cnt:
        max_cnt = cnt[k]
print(max_cnt)

