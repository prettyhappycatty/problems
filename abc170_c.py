X, N = map(int, input().split())
Nmax = 100

p = list(map(int, input().split()))

ary = {i:True for i in range(0, Nmax+2)}

for i in range(N):
    ary[p[i]] = False

if ary[X] == True:
    print(X)
    exit()
#print(ary)
j = 1
sm = 0
dist_sm = 0
while X-j >= 0:
    if ary[X-j] == True:
        sm = X-j
        dist_sm = j
        break
    j += 1

i = 1
bi = Nmax+1
while X + i <= Nmax+1:
    if ary[X+i] == True:
        bi = X+i
        dist_bi = i
        break
    i += 1

if dist_sm > dist_bi:
    print(bi)
else:
    print(sm)