N = int(input())

sum_tmp = 0
smallest_not_times10 = 101
for i in range(N):
    tmp = int(input())
    sum_tmp += tmp
    if tmp % 10 != 0 and tmp < smallest_not_times10:
        smallest_not_times10 = tmp

if sum_tmp % 10 != 0:
    print(sum_tmp)
elif smallest_not_times10 <= 100:
    print(sum_tmp-smallest_not_times10)
else:
    print(0)
    