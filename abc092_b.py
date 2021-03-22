N = int(input())
D, X = map(int, input().split())

def eatsCnt(d, a):
    count = int((d -1) // a) + 1
    return count


choco = 0
for i in range(N):
    a = int(input()) 
    #print(a,eatsCnt(D, a))
    choco += eatsCnt(D, a)

print(choco+X)

