N = int(input())

if N == 0:
    print(0)
    exit()

n_sin = []
b = 1
keta_count = 0
while abs(b) < abs(N)*4:
    n_sin.append(b)
    b *= (-2)
    keta_count += 1

#print(n_sin, keta_count)

import itertools

lst = list(itertools.product([0,1], repeat=keta_count))
dic_2_shin = {}

for i in range(len(lst)):
    bl = lst[i]
    num = 0
    bl_str = ""
    for j in range(keta_count):
        num += bl[keta_count-j-1]*n_sin[j]
        bl_str += str(bl[j])
    
    #print(num, int(bl_str))
    dic_2_shin[num] = int(bl_str)
    #if num == N:
        #print(int(bl_str))
        #exit()

dic_sorted = sorted(dic_2_shin.items(), key=lambda x:x[0])

for n, k in list(dic_sorted):
    print(n, k)