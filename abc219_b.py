S1 = input()
S2 = input()
S3 = input()
T = input()

dic = {"1":S1, "2":S2, "3":S3}

ret = ""

for i in range(len(T)):
    ret = ret + dic[T[i]]

print(ret)