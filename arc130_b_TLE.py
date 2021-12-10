H, W, C, Q = map(int, input().split())

import heapq

class MasuSet:
    def __init__(self, i, t, n, c):
        self.i = i
        self.t = t
        self.n = n
        self.c = c
    def __lt__(self,other):
        return self.i < other.i


dic = {} # [t, n]:[i, t,n,c]を入れる
#cnt_1 = {i: 0 for i in range(C)} # color の塗ってある行
cnt_1 = {}
#cnt_2 = {i: 0 for i in range(C)} # color の塗ってある列
cnt_2 = {}
cnt = {i: 0 for i in range(C)} # color の塗ってある個数

#クエリを簡略化するため、同じ行に複数回塗る場合には最後のものを採用するようにする
for i in range(Q):
    tt, nt, ct = map(int, input().split())
    dic[tuple((tt, nt))] = [i, tt-1, nt-1, ct-1]

#print(dic)
#print(len(dic))
HH = []
heapq.heapify(HH)# [t, n]:[i, t,n,c]を入れるH, W, C, Q = map(int, input().split())
for k,v in dic.items():
    #print(v)
    a = MasuSet(v[0], v[1],v[2],v[3])
    #print(a)
    heapq.heappush(HH,a)

#print(HH)
if H + W > 10**9:
    #cnt_1 = {i: 0 for i in range(C)} # color の塗ってある行
    cnt_1 = {}
    #cnt_2 = {i: 0 for i in range(C)} # color の塗ってある列
    cnt_2 = {}
    while len(HH) > 0:
        a = heapq.heappop(HH)
        order = a.i
        tt = a.t
        nt = a.n
        ct = a.c
        #print(order, tt, nt, ct)
        if tt == 1:
            if ct not in cnt_1:
                cnt_1[ct] = 0
            cnt_1[ct] += 1 
            cnt[ct] += H
            for k, v in cnt_2.items():
                cnt[k] -= v
        else: #tt == 2
            if ct not in cnt_2:
                cnt_2[ct] = 0
            cnt_2[ct] += 1 
            cnt[ct] += W
            for k, v in cnt_1.items():
                cnt[k] -= v
        #print(cnt)
else:
    cnt_1 = {i: 0 for i in range(C)} # color の塗ってある行
    #cnt_1 = {}
    cnt_2 = {i: 0 for i in range(C)} # color の塗ってある列
    #cnt_2 = {}
    while len(HH) > 0:
        a = heapq.heappop(HH)
        order = a.i
        tt = a.t
        nt = a.n
        ct = a.c
        #print(order, tt, nt, ct)
        if tt == 1:
            cnt_1[ct] += 1 
            cnt[ct] += H
            for k, v in cnt_2.items():
                cnt[k] -= v
        else: #tt == 2
            cnt_2[ct] += 1 
            cnt[ct] += W
            for k, v in cnt_1.items():
                cnt[k] -= v

ans = []
for k,v in cnt.items():
    ans.append(v)

print(*ans)



