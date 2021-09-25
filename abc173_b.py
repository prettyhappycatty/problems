N = int(input())
cnt = {"AC":0, "WA":0,"TLE":0,"RE":0}
for i in range(N):
    s = input()
    cnt[s] += 1

for ans in cnt.keys():
    print(ans, "x", cnt[ans])
    
