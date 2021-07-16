N, K = map(int, input().split())

P = list(map(int, input().split()))

s = []
tmps = 0
for i in range(N):
    tmps += (P[i]+1)/2.0
    s.append(tmps)

#print(s)

if N == K:
    print(tmps)
    exit()

ss = []
for i in range(N-K):
    ss.append(s[i+K]-s[i])


ss.sort(reverse=True)
print(ss[0])

