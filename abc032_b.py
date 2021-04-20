s = input()
k = int(input())

pa = {}

if len(s) < k:
    print(0)
else:
    for i in range(len(s)-k+1):
        if s[i:i+k] not in pa.keys():
            pa[s[i:i+k]] = True
    print(len(pa.keys()))