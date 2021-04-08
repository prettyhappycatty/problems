X = int(input())

n100 = X // 100 #個数

rest = [i*5 for i in range(100000)]

if X - n100*100 <= rest[n100]:
    print(1)
else:
    print(0)