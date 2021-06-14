import bisect

K, Q = map(int, input().split())

A = list(map(int, input().split()))
A.sort()

B = [0] * K
for i in range(K):
    B[i] = A[i] - (i+1) 

#print(B)
#print(A)

for i in range(Q):
    tmp = int(input())
    #print(tmp, A[0], A[K-1])
    if tmp < A[0]:
        print(tmp)
        #print("1->", tmp)
    elif tmp > A[K-1]:
        print(int(tmp + K))
        #print("2->", int(tmp + K))
    else:
        idx = bisect.bisect_left(B, tmp) -1
        print(A[idx] + tmp - B[idx])
        #print("3->", A[idx] + tmp - B[idx])
        #print(A[idx],tmp,B[idx])

