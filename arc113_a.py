K = int(input())
ans = 1
for a in range(1,K): #AはKより小さい
    for b in range(1, K//a+1): #BはK//aより小さい
        c = K//(a*b)
        ans += c

print(ans)