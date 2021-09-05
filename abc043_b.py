s = input()

ret = ['']*len(s)
cursor = 0
for i in range(0, len(s)):
    #print(cursor)
    if s[i] == 'B':
        cursor -= 1
        ret[cursor] = ''
        ret[i] = ''
        if cursor < 0:
            cursor = 0
    else:
        ret[cursor] = s[i]
        cursor += 1
    #print(cursor, ret)

print(''.join(ret))