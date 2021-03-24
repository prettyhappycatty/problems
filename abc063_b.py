S = input()
mydict = {}

flg = 0
for i in range(len(S)):
    if S[i] in mydict.keys():
        print("no")
        flg = 1
        break
    else:
        mydict[S[i]] = 1

if flg == 0:
    print("yes")