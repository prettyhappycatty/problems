n, X = map(int, input().split())
a = list(map(int, input().split()))


x = X
price = 0
i = 0
while x != 0:
    b = x % 2
    x = x // 2
    price += b*a[i]
    i +=1

print(price)