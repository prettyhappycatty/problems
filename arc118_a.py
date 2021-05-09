import math

t, N = list(map(int, input().split()))

mods = {}

def geti(i):
    return math.ceil((100+t)*i/100)

cnt = 0
for i in range(100):
    fst = math.floor((100+t)*(i+1)/100)
    snd = math.floor((100+t)*(i+2)/100)
    y = t * (i+1) % 100
    x = t * (i+1) // 100
    if snd - fst == 2:
        #print(i+1, x, y, fst, snd, geti(x))
        #print("Yes", fst+1)
        mods[cnt] = fst + 1
        cnt += 1

#print(mods, cnt)
s = (N-1) // cnt
m = (N-1) % cnt
#print(s, m)
print(s * (100+t) + mods[m])

