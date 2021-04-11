N = input()

def is_rotate(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

flg = False
for i in range(10):
    st = '0'*i + N
    if is_rotate(st):
        flg = True
        break

if flg == True:
    print('Yes')
else:
    print('No')


