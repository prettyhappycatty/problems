N = int(input())

A = list(map(int, input().split()))

ans_ = 0

for i in range(N):
    ans_ += 1/A[i]

print(1/ans_)