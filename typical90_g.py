N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = []
A.sort()

def solve(n):#二分探索
    left = 0
    right = len(A)-1 #最大

    if len(A) == 1:
        return A[0]
    while right-left >1:
        mid = (right+left)//2
        if A[mid] > n:
            right = mid
        else:
            left = mid

    if left != len(A) and abs(A[left] - n) > abs(A[left+1] - n):
        return A[left+1]
    else:
        return A[left]

for i in range(Q):
    tmp_B = int(input())
    cls = solve(tmp_B)
    print(abs(cls-tmp_B))