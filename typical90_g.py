N = int(input())

A = list(map(int, input().split()))

Q = int(input())

B = []


A.sort()

#print(A)

def solve(n):#二分探索
    left = 0
    right = len(A)-1 #最大

    if len(A) == 1:
        return A[0]
    #print("n=",n)
    while right-left >1:
        mid = (right+left)//2
        #print('p=',mid)
        #v = kosuu(mid) # 2分した真ん中の積載量を出す
        #print(left,mid,right)
        #print(A[left],A[mid],A[right])
        if A[mid] > n:
            #print(v,'>=',n)
            right = mid
        else:
            left = mid

    if left != len(A) and abs(A[left] - n) > abs(A[left+1] - n):
        #print(left+1)
        return A[left+1]
    elif left != 0 or abs(A[left] - n) > abs(A[left-1] - n):
        #print(left-1)
        return A[left-1]
    else:
        #print(left)
        return A[left]

for i in range(Q):
    tmp_B = int(input())
    cls = solve(tmp_B)
    print(abs(cls-tmp_B))
    #print(cls)