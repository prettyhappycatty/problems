from bisect import bisect_left, insort
from array import array

L, Q = map(int, input().split())

no = [0,L]
nlist = array('i', [0, L])

for i in range(Q):
    c, x = map(int, input().split())
    if c == 2:
        #二分木でグループを探して長さを出す
        ok = bisect_left(nlist, x)
        print(nlist[ok]-nlist[ok-1])
    else:#c==1
        insort(nlist, x)
