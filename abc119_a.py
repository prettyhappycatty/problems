S = input()

a = S.split("/")
b = int(a[0]+a[1]+a[2])
#print(b)
if b <= 20190430:
    print("Heisei")
else:
    print("TBD")