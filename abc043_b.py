s = input()

ret = ['']*len(s)
cursor = 0
for i in range(0, len(s)):
    print(cursor)
    if s[i] == 'B':
        cursor -= 1
        ret[cursor] = ''
        ret[i] = ''
    else:
        ret[i] = s[i]
        cursor += 1

print(''.join(ret))