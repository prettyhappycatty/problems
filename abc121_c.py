N, M = list(map(int, input().split()))

A = {}
B = {}

for i in range(N):
    tmp1, tmp2 = list(map(int, input().split()))
    A[i] = tmp1
    B[i] = tmp2

#print(A)
sorted_A = sorted(A.items(), key=lambda x:x[1]) #値段でソート

#print(sorted_A)
#print(B)

rest = M
sum_price = 0
for i in range(len(sorted_A)):
    #sorted_A[i][0] お店のIndex
    #sorted_A[i][1] お店で買える値段
    #B[sorted_A[i][0]] お店で買える本数
    if rest > B[sorted_A[i][0]]:
        buy = B[sorted_A[i][0]]
        rest = rest - buy
        sum_price += buy * sorted_A[i][1]
    else:
        buy = rest
        rest = 0
        sum_price += buy * sorted_A[i][1]
    #print(buy, sorted_A[i][0], sum_price)

print(sum_price)



