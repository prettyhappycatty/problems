X = int(input())

last=1
i = 1

def ex(a, b):
    s = 1
    for i in range(b):
        s *= a
    return s

i = 1
while i < X:
    j = 2
    while j < X:
        if ex(i,j) <= X:
            #if(j > 2):
            #    print(i,j,ex(i,j),last)
            if last < ex(i,j):
                last = ex(i,j)
            j +=1
        else:
            break
    i += 1
            
            

print(last)
