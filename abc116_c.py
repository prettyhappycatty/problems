N = int(input())

H = list(map(int, input().split()))
ans = H[0]
for i in range(N-1):
    a = H[i]
    b = H[i+1]
    #print(a,b)
    if a < b: ans += b - a
print(ans)