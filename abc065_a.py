TMP = input().split()
X = int(TMP[0])
A = int(TMP[1])
B = int(TMP[2])

if A - B >= 0:
    print("delicious")
elif B - A <= X:
    print("safe")
else:
    print("dangerous")