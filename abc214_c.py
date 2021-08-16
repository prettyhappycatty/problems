N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

again = [i for i in range(N)]

def calc(again):
    next = []
    for i in again:
        if i == 0:
            if T[N-1]+S[N-1] < T[0]:
                T[i]= T[N-1]+S[N-1]
                next.append(0)
            else:
                T[i]= T[0]
        else:
            if T[i-1]+S[i-1] < T[i]:
                T[i]= T[i-1]+S[i-1]
                next.append(i)
            else:
                T[i] = T[i]
        #print(T)
    return next


calc(again)
calc(again)
for i in range(N):
    print(T[i])

    
