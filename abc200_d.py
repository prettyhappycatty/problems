N = int(input())
A = list(map(int, input().split()))

#print(A)

rest = {}

max_len = min(len(A),9)
A =A[0:max_len]
N = max_len

#print(rest)

for i in range(N):
    r = A[i]%200
    if r not in rest.keys():
        rest[r]=[]
    rest[r].append(i+1)
    #print(r, rest)

#print(len(rest))

import itertools

lst = list(itertools.product([0,1], repeat=len(rest)))#最悪10**60になるのでNG

rest_list = list(rest.items())
#print(rest_list)
if len(rest) == 1:
    print("Yes")
    print("1", rest_list[0][1][0])
    print("1", rest_list[0][1][1])
    exit()

#print(lst)
if len(lst)>1:
    cnt_1= []
    str_1 = []
    for l in range(1,len(lst)):
        cnt1 = 0
        str1 = []
        ll = lst[l]
        for i in range(len(rest)):
            if ll[i] == 1:
                cnt1 = (cnt1 + A[i]) % 200
                str1.append(i+1)
        str_1.append(str1)
        cnt_1.append(cnt1)

#print(str_1)
#print(cnt_1)

for i in range(len(cnt_1)):
    for j in range(i+1, len(cnt_1)):
        if cnt_1[i]%200 == cnt_1[j]%200:
            print("Yes")
            print(len(str_1[i]), *str_1[i])
            print(len(str_1[j]), *str_1[j])
            exit()


#print(str_1, cnt_1)

#print("Yes")
#print(len(str1), *str1)
print("No")

