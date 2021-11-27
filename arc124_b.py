N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def isGood(aa,bb):
    for i in range(0,N):
        if aa[i] != bb[i]:
            return False
    return True

X = []
for i in range(N):
    X.append(a[0] ^ b[i])

#print(X)

ans = []

for j in range(N):
    C = []
    x = X[j]
    for i in range(N):
        C.append(a[i]^x)

    b.sort()
    C.sort()
    if isGood(b,C) and x not in ans:
        ans.append(x)

ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])

    


