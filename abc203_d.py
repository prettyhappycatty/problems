N, K = map(int, input().split())

A = []
for i in range(N):
    tmpA = list(map(int,input().split()))
    A.append(tmpA)

#print(A)
def kosuu(k,ary):
    ret = 0
    for i in range(len(ary)):
        if k < ary[i]:
            ret += 1
    return ret

def getmed(k, ary):#二分探索
    left = 0
    right = 800 * 800 
    while right-left >1:
        mid = (right+left)//2
        #print('p=',mid)
        v = kosuu(mid, ary) # 2分した真ん中の積載量を出す
        #print(right,left,mid)
        if v < k*k//2 + 1:
            #print(v,'>=',k//2)
            right = mid
        else:
            left = mid

    return right, v

#ある区間KxKの配列セット
area_set =[]
smallest = 10e9
smallest_v = 0
for i in range(N-K+1):
    tmp_set = []
    for j in range(K):
        for k in range(K):
            tmp_set.append(A[i+j][i+k])
    tmp_med, v = getmed(K, tmp_set)#時間かかりそう

    if smallest > tmp_med:
        smallest = tmp_med


#print(area_set)

print(v+1)
