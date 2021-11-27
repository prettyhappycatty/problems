N = int(input())

def isZorome(x):
    s = str(x)
    l = len(s)
    if s.count(s[0]) == l:
        return True
    else:
        return False

cnt = 1
for i in range(1,1000000):
    #print(cnt, i)
    zorome = isZorome(i)
    if cnt == N and zorome == True:
        print(i)
        exit() 
    if zorome == True:
        cnt += 1
