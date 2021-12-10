N = int(input())
ma = int(N ** 0.5)
dic = {}

for a in range(2, ma + 1):
    x = a * a #2条からスタート
    while x <= N:
        dic[x] = True
        x *= a
print(N - len(dic))