N, X = map(int, input().split())
A = list(map(int, input().split()))

dic = {}
done = {i+1:False for i in range(len(A))}
for i in range(len(A)):
    dic[i+1] = A[i]

cnt = 1
if dic[X] == X:
    done[X] = True
    print(cnt)
else:
    to = dic[X]
    done[X] = True
    while done[to] == False:
        done[to] = True
        to = dic[to]
        cnt += 1
    print(cnt)

#print(dic, done)