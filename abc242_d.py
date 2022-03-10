s = "ABC"

ii = []
for i in range(len(s)):
    if s[i] == "A":
        ii.append(0)
    elif s[i] == "B":
        ii.append(1)
    else:
        ii.append(2)

print(ii)

def solve(ii, n):
    for i in range(n):
        new_ary = []
        for j in range(len(ii)):
            new_ary.append((ii[j]+1)%3)
            new_ary.append((ii[j]+2)%3)
        ii = new_ary
    return new_ary

ans = solve(ii, 3)

print(ans)

ret = []
for i in range(len(ans)):
    if ans[i] == 0:
        ret.append("A")
    elif ans[i] == 1:
        ret.append("B")
    else:
        ret.append("C")

print(ret)    
        

