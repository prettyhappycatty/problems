N, D = map(int, input().split())

l = []

for i in range(N):
    l.append(tuple(map(int, input().split())))

print(l)

l.sort()

print(l)