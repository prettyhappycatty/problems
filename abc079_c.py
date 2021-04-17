ABCD = input()

op = ['+++', '-++','+-+','++-','+--','-+-','--+','---']

for i in range(len(op)):
    sum = int(ABCD[0])
    sum_str = ABCD[0]
    for j in range(0,3):
        if op[i][j] == '+':
            sum += int(ABCD[j+1])
            sum_str += '+' + ABCD[j+1]
        else:
            sum -= int(ABCD[j+1])
            sum_str += '-' + ABCD[j+1]
    if sum == 7:
        print(sum_str+'=7')
        break
    