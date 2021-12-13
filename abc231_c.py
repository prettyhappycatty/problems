N, Q = map(int, input().split())
A = list(map(int, input().split()))

dic = {}
for i in range(N):
    dic[i] = A[i]

A.append(0)
A.append(10**9+1)
A.sort()

#print(A)

def is_ok(mid,thres):
    if thres > A[mid]: #閾値がA[mid]より小さくなる最大のmidをもとめる
        #print(mid,A[mid], "<=" ,thres)
        return True
    else:
        #print(mid,A[mid], ">" ,thres)
        return False

def binary_search(ok, ng, thres):
    while ng - ok > 1:
        mid = (ok + ng) // 2
        #print(ok,ng, A[mid], thres)
        if is_ok(mid,thres):
            ok = mid
        else:
            ng = mid
    return ok

for j in range(Q):
    q = int(input())
    ans = binary_search(0, N+2, q)
    print(N-ans)