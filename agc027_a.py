N,x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

i = 0
sums = a[i]
while x >= sums:
    i += 1
    if i == N and x > sums:
        i -= 1
        break
    elif i == N:
        break
    sums = sums + a[i]

print(i)

