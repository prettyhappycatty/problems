A, B, M = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))


a_min = 10**7
b_min = 10**7

for i in range(A):
    if a_min > a[i]:
        a_min = a[i]
for i in range(B):
    if b_min > b[i]:
        b_min = b[i]

price_min = 10**7
for i in range(M):
    x, y, c = list(map(int, input().split()))
    price = a[x-1] + b[y-1] - c
    if price_min > price:
        price_min = price

if a_min + b_min > price_min:
    print(price_min)
else:
    print(a_min + b_min)