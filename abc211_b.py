dic = {"H":False, "2B":False, "3B":False, "HR":False}

for i in range(4):
    tmpS = input()
    dic[tmpS] = True

for k,v in dic.items():
    if v == False:
        print("No")
        exit()

print("Yes")
