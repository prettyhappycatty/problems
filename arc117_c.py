import math

N = int(input())
S = input()

def init():
    bg = [0]*400001
    bf = [0]*400001
    for i in range(1,400001):
        pos = i
        while pos % 3 == 0:
            pos /= 3
            bf[i] += 1
        bg[i] = pos % 3
	
    bg[0] = 1
    for i in range(1,400001):
        bf[i] += bf[i - 1]
    for i in range(1,400001):
        bg[i] = (bg[i] * bg[i - 1]) % 3
    return bg, bf

def ncr_mod_3(n, r):
    if bf[n] != bf[r] + bf[n - r]:
        return 0
    if bg[n] == 1 and bg[r] * bg[n - r] == 1:
        return 1
    if bg[n] == 1 and bg[r] * bg[n - r] == 2:
        return 2
    if bg[n] == 1 and bg[r] * bg[n - r] == 4:
        return 1
    if bg[n] == 2 and bg[r] * bg[n - r] == 1:
        return 2
    if bg[n] == 2 and bg[r] * bg[n - r] == 2:
         return 1
    if bg[n] == 2 and bg[r] * bg[n - r] == 4:
         return 2
    return -1

def col2num(s):
    b, w, r  = 0, 1, 2
    if s == 'R':
        return r
    elif s == 'W':
        return w
    elif s == 'B':
        return b

def num2col(n):
    b, w, r = 0, 1, 2
    if n == r:
        return 'R'
    elif n == w:
        return 'W'
    elif n == b:
        return 'B'

bg, bf = init()
#print(bf, bg)
su = 0
for i in range(N):
    ncrmod =ncr_mod_3(N-1,i)
    tmp = col2num(S[i])*ncrmod
    print(col2num(S[i]),N-1, i, ncrmod,tmp)
    su += tmp
    su = su % 3 
    
print(num2col(su))

#TLE