n = int(input())
c = 10**6+2
cl = [0 for i in range(c)]

for i in range(n):
    a, b = map(int, input().split())
    cl[a] = cl[a]+1
    cl[b+1] = cl[b+1]-1

#print(cl)

rui = 0
ans = []
for i in range(c):
    rui += cl[i]
    ans.append(rui)

print(max(ans))
