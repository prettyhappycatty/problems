import bisect

Q = int(input())
bis = []

cnt = 0
for i in range(Q):
    qq = list(map(int, input().split()))
    if qq[0] == 1:
        x = qq[1]
        bisect.insort_left(bis, x)
        cnt +=1
    elif qq[0] == 2:
        x = qq[1]
        k = qq[2]
        id = bisect.bisect_right(bis, x)
        if  id<= k-1:
            print(-1)
        else:
            ary = bis[id-k:id]
            print(ary[0])
    else: #qq[0]==3
        x = qq[1]
        k = qq[2]
        id = bisect.bisect_left(bis, x)
        if cnt-id <= k-1:
            print(-1)
        else:
            ary = bis[id:id+k]
            print(ary[k-1])