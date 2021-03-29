N = int(input())
a_except_max = {}
a = []

first = 0
secound = 0
first_i = 0
secound_i = 0
for i in range(N):
    tmp = int(input())
    a.append(tmp)
    #print(tmp, first, secound, first_i, secound_i)
    if tmp >= first and first >= secound:
        secound = first
        first = tmp
        secound_i = first_i
        first_i = i
    elif first > tmp and tmp >= secound:
        secound = tmp
        secound_i = i 


#print(tmp, first, secound, first_i, secound_i)

for i in range(N):
    if i == first_i:
        print(a[secound_i])
    else:
        print(a[first_i])

    

