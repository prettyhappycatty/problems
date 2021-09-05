
contests = {"ABC":False , "ARC":False , "AGC":False , "AHC":False}

for i in range(3):
    tmp = input()
    contests[tmp] = True

for k in contests.keys():
    if contests[k] == False:
        print(k)
        exit()
