abc = int(input())

a = abc // 100
b = (abc - a*100)//10
c = (abc - a*100 - b * 10)

print((a+b+c)*111)