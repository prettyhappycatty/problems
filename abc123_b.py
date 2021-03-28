A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

t_max = -1
id_max = -1
ary = [A, B, C, D, E]

for i in range(len(ary)):

    tmp = ((ary[i]+9)//10)*10
    tmp_loss = tmp - ary[i]
#    print("loss", tmp_loss)
    if tmp_loss > t_max:
        t_max = tmp_loss
        id_max = i

#print("loss_max", t_max)
t_sum = 0
for i in range(len(ary)):
    if i != id_max:
        tmp = ((ary[i]+9)//10)*10
#        print(tmp)
        t_sum += tmp

print(t_sum + ary[id_max])
        