N = int(input())

h = list(map(int, input().split()))

# c2 = h2-h1
# c3 = min(c2, (h3-h1))
# c4 = min(c2+h4-h2, c3+h4-h3) 
ans = [0 for _ in range(N)]

for i in range(1,N):
    if i == 1:
        ans[i] = abs(h[i] - h[i-1])
    else:
        ans[i] = min(ans[i-1] + abs(h[i] - h[i-1]), ans[i-2] + abs(h[i]-h[i-2]))

print(ans[N-1])