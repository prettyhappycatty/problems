S = input()

bef = 0

def isACGT(s):
    if s == 'A' or s == 'C' or s == 'G' or s == 'T':
        return True
    else:
        return False

bef = 0
arr = [0]
for i in range(len(S)):
    if isACGT(S[i]):
        bef += 1
    else:
        arr.append(bef)
        bef = 0

arr.append(bef)

maxlen = 0
for j in range(len(arr)):
    if maxlen < arr[j]:
        maxlen = arr[j]

print(maxlen)
