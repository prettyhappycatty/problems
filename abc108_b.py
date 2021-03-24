import math

a, b, c, d = list(map(int, input().split()))

x = c-a
y = d-b

e, f, g, h = (c-y), (d+x) ,(a-y) ,(b+x)

print(e, f, g, h)