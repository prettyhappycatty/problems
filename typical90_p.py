N = int(input())

A, B, C = map(int, input().split())

sm_mai = 9999*3
for i in range(9999):
    for j in range(9999):
        c = N - (A*i + B*j)
        #print(c)
        if c < 0:
            break
        if c % C == 0:
            mai = i + j + c//C
            #print(i, j, c//C)
        else:
            mai = 9999*3

        if mai < sm_mai:
            sm_mai = mai

print(sm_mai)
        
