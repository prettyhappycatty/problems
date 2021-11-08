import sys
sys.setrecursionlimit(10**6)

N = int(input())

T, K, A = [],[],[]

cost_comp = [False for i in range(N)]

def minus1(a):
    return a-1 

for i in range(N):
    l = list(map(int, input().split()))
    #print(l)
    T.append(l[0])
    K.append(l[1])
    if l[1] > 0:
        A.append(list(map(minus1, l[2:])))
    else:
        A.append([])

num = 0
cost_list = {i:False for i in range(N)}
def get_cost(i):
    if  cost_comp[i] or K[i] == 0:
        cost_list[i] = True
        cost_comp[i] = True
        return 
    else:
        for a in A[i]:
            if cost_comp[a] == False:
                get_cost(a)
        cost_comp[i] = True
        cost_list[i] = True
        return

get_cost(N-1)
#print(cost)
#print(T, K, A)

#print(cost_list)
ans = 0
for k,v in cost_list.items():
    if v == True:
        ans += T[k]
print(ans)
