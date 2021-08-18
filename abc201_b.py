N = int(input())

first = ""
first_height = 0
second = ""
second_height = 0

for i in range(N):
    tmp_s, tmp_t = input().split()
    if int(tmp_t) > first_height and int(tmp_t) > second_height:
        second_height = first_height
        first_height = int(tmp_t)
        second = first
        first = tmp_s
    elif first_height > int(tmp_t) > second_height:
        second_height = int(tmp_t)
        second = tmp_s

print(second)
        
