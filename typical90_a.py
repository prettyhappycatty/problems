N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))
A.append(L)

def check(n):
    cut = 0
    tmp = A[0]
    shortest = 10**9
    ary = []

    if tmp >= n:
        cut += 1
        if shortest > tmp:
            shortest = tmp
        ary.append(tmp)
        tmp = 0

    for i in range(1,len(A)):
        tmp += A[i] - A[i-1]
        if tmp >= n:
            cut += 1
            if shortest > tmp:
                shortest = tmp
            ary.append(tmp)
            tmp = 0
    #print(ary, cut, shortest)
    return cut, shortest
    


def nibutan(n):
    left = 1
    right = 10**9
    mid = (left + right) // 2
    mid_val,shortest = check(mid)
    #print("nibn=", left, right, mid, mid_val)
    while right - left > 1:
        if mid_val < K+1:
            #print("right to mid", right, mid)
            right = mid
        else:
            #print("left to mid", left, mid)
            left = mid
        mid = (left + right) // 2
        mid_val,shortest = check(mid)
        #print("nextn=",i, left, right, mid, mid_val)
    return left, shortest

j, val = nibutan(N)
print(j)