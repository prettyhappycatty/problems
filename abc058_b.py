O = input()
E = input()

lst = []
if len(O) > len(E):
    shorter_len = len(E)
    longer_arr = O
else:
    shorter_len = len(O)
    longer_arr = E

for i in range(shorter_len):
    lst.append(O[i])
    lst.append(E[i])

for j in range(shorter_len, len(longer_arr)):
    lst.append(longer_arr[j])

print(''.join(lst))