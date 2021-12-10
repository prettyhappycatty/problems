A, B = list(map(int, input().split()))
a = str(A)
b = str(B)

#if A == "0" and B == "0":
#    print("Easy")
#    exit()

a = a[::-1]
b = b[::-1]
#print(a,b)
longer_AB = max(len(a),len(b))
ketas = []
for i in range(longer_AB):
    keta = 0
    #print(i)
    if len(a) > i:
        keta += int(a[i])
    if len(b) > i:
        keta += int(b[i])
    ketas.append(str(keta))

ans = ''.join(ketas[::-1])
if int(ans) == A+B and longer_AB == len(str(A+B)) :
    print("Easy")
else:
    print("Hard")