N = map(int, input().split())
S1 = list(input())
S2 = list(input())

MOD = 10**9+7

if N == 1:
    print(3)
    exit()

def checktype(a1,a2,b1,b2):
    if a1 == a2 and b1 == b2:
        return 2
    if a1 == a2 and b1 != b2:
        return 2
    if a1 != a2 and b1 == b2:
        return 1
    if a1 != a2 and b1 != b2:
        return 3

G = {}

i = 1
if S1[0] == S2[0]:
    mul = 3
else:
    mul = 6
#print(0,mul)
while i < len(S1):
    if S1[i-1] != S1[i]:
        c = checktype(S1[i-1],S2[i-1],S1[i],S2[i])
        #print(i,c)
        mul *= c 
        mul %= MOD
#        print(c,mul)
    i += 1

print(mul)

