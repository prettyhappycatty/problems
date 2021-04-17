S1 = input()
S2 = input()
S3 = input()

s_dict = {}
for s in S1:
    if s in s_dict.keys():
        s_dict[s] += 1
    else:
        s_dict[s] = 1

for s in S2:
    if s in s_dict.keys():
        s_dict[s] += 1
    else:
        s_dict[s] = 1

for s in S3:
    if s in s_dict.keys():
        s_dict[s] += 1
    else:
        s_dict[s] = 1
#print(len(s_dict))
#print(s_dict)

candidate1 = range(1, 9)
candidate2 = range(0, 9)
candidate = {}
for s_key in s_dict.keys():
    if S1[0] == s_key or S2[0] == s_key or S3[0] == s_key:
        candidate[s_key] = candidate1
    else:
        candidate[s_key] = candidate2
print(candidate)

def alternate(s, a, ran):
    ary = []
    for i in ran:
        ary.append(s.replace(a,str(i)))
    return ary
        
#TODO

    
