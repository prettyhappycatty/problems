N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ab_sum = 0
flg = 0
for i in range(N):
    ab_sum += abs(A[i] - B[i])

#print(ab_sum)
if ab_sum % 2 != K % 2:
    print("No")
elif ab_sum <= K:
    print("Yes")
else:
    print("No")
    

