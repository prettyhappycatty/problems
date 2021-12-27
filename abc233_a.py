X, Y = map(int, input().split())

if Y <= X:
    print(0)
    exit()

if (Y-X) % 10 == 0:
    print((Y-X)//10)
else:
    print((Y-X)//10+1)
