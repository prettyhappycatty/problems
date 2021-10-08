N = int(input())

shop = []
for i in range(N):
    tmp_shop = list(map(int, input().split()))
    shop.append(tmp_shop)

#print(shop)

n = []
for i in range(N):
    tmp_n = list(map(int, input().split()))
    n.append(tmp_n)

import itertools
lst = list(itertools.product([0,1], repeat=10))
max_score = -10**9
for l in range(1, len(lst)):
    shop_cnt = []
    ll = lst[l]
    for j in range(N):
        tmp_shop_cnt = 0
        for k in range(10):
            if ll[k] == 1 and shop[j][k] == 1:
                tmp_shop_cnt += 1
        shop_cnt.append(tmp_shop_cnt)
    #print(shop_cnt)
    score = 0
    for j in range(N):
        score += n[j][shop_cnt[j]]
    #print(ll, shop_cnt, score)

    max_score = max(max_score, score)

print(max_score)