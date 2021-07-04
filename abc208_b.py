P = int(input())

coins = []
mul = 1
for i in range(1,11):
    mul *= i
    coins.append(mul)

#print(coins)

rest = P
c_i = -1
for i in range(10):
    if rest < coins[i]:
        c_i = i-1
        break
if c_i == -1:
    c_i = 9
#print(c_i)

n_coin = 0
while rest > 0:
    n_rest = rest // coins[c_i]
    n_coin += n_rest
    rest -= n_rest*coins[c_i]
    c_i -= 1

print(n_coin)
