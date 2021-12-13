N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
A.append(10**9)
B.sort()
B.append(10**9)
C.sort()
C.append(10**9)

#print(A)
#print(B)
#print(C)

def isOk(a, b, thres):
    print(a,thres)
    if a < thres:
        return True
    else:
        return False

def bi(thres, ary):
    #二分探索でi以上でK以上となる最小indexjを求める
    st = 0
    end = N
    while end - st > 1:
        mid = ( st + end ) // 2
        #print("st",st, "mid",mid, "end",end,  ary[mid], thres )
        if isOk(ary[mid], ary[mid+1],thres):
            st = mid
        else:
            end = mid
    #print("st=",i, "s=", s[st], K, N-st)
    #print(st)
    return st

cnt = 0
for i in range(N):
    a = A[i]
    b_cnt = bi(a, B)
    b = B[b_cnt:N]
    print(b)
    for j in range(len(b)):
        print(b[j])
        c_cnt = bi(b[j], C)
        c = C[c_cnt:N]
        cnt += N-c_cnt
        print("+",N-c_cnt, c)

print(cnt)


#test = [2, 50, 79, 288, 383, 2643, 1000000000]

#ret = bi(8, test)
#print(ret)