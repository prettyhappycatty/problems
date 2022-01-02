x, y = map(int, input().split())

cnt = 0

# x = 0
# 0 -10 a*10 b x<y
# 0 10 a*10
# y = 0
# -10 0 a*10 x<y
# 10 0 b a*10

if x == 0 or y == 0:
    if x < y:
        print(abs(x)+abs(y))
    else:
        print(abs(x)+abs(y)+1)
    exit()

#abs(x) - abs(y) < 0
# -10 -20 b a*10 b x*y > 0 and y < x
# 10 20 a*10  x*y > 0 and x < y
# -10 20 b a*10 x*y < 0 and x < 0
# 10 -20 a*10 b x*y < 0 and y < 0
#abs(x) - abs(y) > 0
# -20 -10 a*10 x*y > 0 and x < y
# 20 10 b b a*10 b x*y > 0 and y < x
# -20 10 a*10 b x*y < 0 and x < 0
# 20 -10 b a*10 x*y < 0 and y < 0

if x*y > 0 and y < x:
    print(abs(abs(x)-abs(y))+2)
elif x*y > 0 and x < y:
    print(abs(abs(x)-abs(y)))
else:
    print(abs(abs(x)-abs(y))+1)


