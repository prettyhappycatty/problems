X = input()

#if len(X) % 2 != 0:
#    print(0)
#else:
for i in range(1,1000001):
    if int(str(i) * 2) > int(X):
        print(i-1)
        break 