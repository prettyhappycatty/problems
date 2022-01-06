K, X = map(int, input().split())

ans = [X]
for i in range(1,K):
    if X-i >= -1000000:
        ans.append(X-i)
    if 1000000 >= X+i:
        ans.append(X+i)

ans.sort()

print(*ans)
