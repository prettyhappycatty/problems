import itertools

S = input()

S_sorted = sorted(S, reverse=True)
#print(S_sorted)

A = ""
B = ""

lst = list(itertools.product([0,1],repeat=len(S)))
#print(lst)

mulmax = 1
for v in lst:  
    A = ""
    B = ""
    for j in range(len(v)):
        if v[j] == 1:
            A += S_sorted[j]
        else:
            B += S_sorted[j]
    #print(A,B)
    if A == "" or B == "":
        continue
    mulmax = max(mulmax, int(A)*int(B))

print(mulmax)


