N = int(input())

S = []
dic = {}

for i in range(N):
    tmp_S = input()
    not_ex_S = tmp_S.replace("!", "")

    if tmp_S not in dic.keys():
        dic[tmp_S] = True

    #print(not_ex_S)
    if not_ex_S in dic.keys() and "!"+not_ex_S in dic.keys():
        print(not_ex_S)
        exit()

print("satisfiable")

    