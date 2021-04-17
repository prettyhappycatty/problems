N = int(input())

infin = 10**9 + 7
power = 1
for i in range(1, N+1):
    #print(power)
    power = (power*i) % infin

print(power)