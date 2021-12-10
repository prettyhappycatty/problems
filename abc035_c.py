N, Q = map(int, input().split())

o = [0 for _ in range(N+1)]

for i in range(Q):
    l, r = map(int, input().split())
    o[l-1] += 1
    o[r] -= 1

#print(o)

s = 0
ans = []
for i in range(N):
    s += o[i]
    ans.append(s)

def mod2(i):
    return str(i % 2)

print(''.join(list(map(mod2, ans))))


