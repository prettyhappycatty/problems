N = int(input())

def cnt0(n):
    if n >= 10**3:
        ans = 10**3 - 10**0
    elif n >= 10**0:
        ans = n - 10**0 + 1
    else:
        ans = 0
    return ans

def cnt1(n):
    if n >= 10**6:
        ans = 10**6 - 10**3
    elif n >= 10**3:
        ans = n - 10**3 + 1
    else:
        ans = 0
    return ans

def cnt2(n):
    if n >= 10**9:
        ans = 10**9 - 10**6
    elif n >= 10**6:
        ans = n - 10**6 + 1
    else:
        ans = 0
    return ans

def cnt3(n):
    if n >= 10**12:
        ans = 10**12 - 10**9
    elif n >= 10**9:
        ans = n - 10**9 + 1
    else:
        ans = 0
    return ans

def cnt4(n):
    if n >= 10**15:
        ans = 10**15 - 10**12
    elif n >= 10**12:
        ans = n - 10**12 + 1
    else:
        ans = 0
    return ans

def cnt5(n):
    if n == 10**15:
        ans = 1
    else:
        ans = 0
    
    return ans


#print(cnt0(N),cnt1(N),cnt2(N),cnt3(N),cnt4(N),cnt5(N))
print(cnt0(N)*0+cnt1(N)*1+cnt2(N)*2+cnt3(N)*3+cnt4(N)*4+cnt5(N)*5)
