N = int(input())

def strsum(st):
    ans = 0
    for i in range(len(st)):
        ans += int(st[i])
    return ans

stn = strsum(str(N))

#print(stn)

if N % stn == 0:
    print("Yes")
else:
    print("No")