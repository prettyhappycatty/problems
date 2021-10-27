N, M = map(int, input().split())
X = list(map(int, input().split()))

X.sort()

sa = []
if M < N:
    print(0)
    exit()

for i in range(0, M-1):
    sa.append(X[i+1]-X[i])

sa.sort()
cnt = 0
for i in range(M-N):
    cnt += sa[i]

print(cnt)
#print(sa)