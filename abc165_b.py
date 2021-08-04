X = int(input())

x = 100
ans = 0
while x < X:
    x = x + x//100
    X = X
    ans += 1

print(ans)
