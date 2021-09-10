K = int(input())
ans = 1
for a in range(1,K):
    for b in range(1, -(-K//a)+1):
        c = K//(a*b)
        ans += c

print(ans)