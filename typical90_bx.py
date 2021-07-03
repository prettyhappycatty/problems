#TLE

N = int(input())
A = list(map(int, input().split()))

sumA = []

cnt = 0
for i in range(2*N):
    cnt += A[i]
    sumA.append(cnt)
    if i < N:
        A.append(A[i])

#print(sumA)

if sumA[N-1] % 10 != 0:
    print("No")
    exit()

ans =  sumA[N-1] // 10

def nibutan(i, n):
    left = 1
    right = 2*N-i-1
    mid = (left + right) // 2
    mid_val = sumA[i+mid]-sumA[i]
    #print("nibn=",i, left, right, mid, mid_val)
    while right - left > 1:
        if mid_val > n:
            #print("right to mid", right, mid)
            right = mid
        else:
            #print("left to mid", left, mid)
            left = mid
        mid = (left + right) // 2
        mid_val = sumA[i+mid]-sumA[i]
        #print("nextn=",i, left, right, mid, mid_val)
    return left, mid_val



for i in range(len(A)):
    l, val = nibutan(i, ans)
    #print(i, ans, l, val)
    if val == ans:
        print("Yes")
        exit()

print("No")

