N, K = map(int, input().split())
a = list(map(int, input().split()))

s = [0]
tmp_s = 0
for i in range(N):
    tmp_s += a[i]
    s.append(tmp_s)

#print(s)

cnt = 0
for i in range(N):
    #二分探索でi以上でK以上となる最小indexjを求める
    st = i
    end = N+1
    while end - st > 1:
        mid = ( st + end ) // 2
        #print("st",st, "mid",mid, "end",end,  s[mid] - s[i], K )
        if s[mid] - s[i] < K:
            st = mid
        else:
            end = mid
    #print("st=",i, "s=", s[st], K, N-st)
    cnt += N- st

print(cnt)

