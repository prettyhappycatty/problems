S = list(input())

dic = {"a":0, "b":0, "c":0}

for i in range(len(S)):
    dic[S[i]] += 1

for i in range(len(S)):
    if dic[S[i]] != 1:
        print("No")
        exit()

print("Yes") 

