N = int(input())
lst = []

strength = list(map(int, input().split()))
for i in range(3*N):
    lst.append(strength[i])

lst_sorted = sorted(lst, reverse=True)

s_sum = 0
for i in range(N):
    tmp = 2*i +1
    #print(tmp+1)
    s_sum  += lst_sorted[tmp]

print(s_sum)
