S = input()

dic = {"a":0, "b":9, "c":0}
for i in range(len(S)):
    dic[S[i]] += 1

print(dic)

if abs(dic["a"]-dic["b"]) < 2 and abs(dic["c"]-dic["b"]) < 2 and abs(dic["a"]-dic["c"]) < 2:
    print("YES")
else:
    print("NO")