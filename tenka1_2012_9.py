import math

n = int(input())

i = 2
ary = []
cnt = 0
while i < n:
    flg = False
    for a in ary:
        if a > math.sqrt(n):
            break
        if i % a == 0:
            flg = True
    
    if flg == False:
        ary.append(i) 
        cnt += 1
    i += 1

print(cnt)

