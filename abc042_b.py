N, L = list(map(int, input().split()))
s = []

for i in range(N):
    tmp = input()
    s.append(tmp)

s.sort()

print(''.join(s))