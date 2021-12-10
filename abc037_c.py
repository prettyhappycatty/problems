N, K = map(int, input().split())

a = list(map(int, input().split()))

s = [0]
ss = 0
for i in range(len(a)):
    ss += a[i]
    s.append(ss)

ans = 0
for i in range(N-K+1):
    #print(s[i+K]-s[i])
    ans += s[i+K]-s[i]

print(ans)