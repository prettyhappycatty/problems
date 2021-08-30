S = input()

sar = S.split(".")
X = int(sar[0])
Y = int(sar[1])

#print(X,Y)

if 0 <= Y and Y < 3:
    ans = str(X)+"-"
elif Y < 7:
    ans = str(X)
else:
    ans = str(X)+"+"

print(ans)