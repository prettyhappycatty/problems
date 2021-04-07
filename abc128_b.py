N = int(input())
dict_restaurant = {}

for i in range(N):
    tmp = list(input().split())
    list_restaurant = {}
    if tmp[0] in dict_restaurant.keys():
        dict_restaurant[tmp[0]][i] = int(tmp[1])
    else:
        dict_restaurant[tmp[0]] = {}
        dict_restaurant[tmp[0]][i] = int(tmp[1])

#dict_restaurantがdict型, keyでソート
sorted_city = sorted(dict_restaurant.items(), key=lambda x:x[0])
for item in sorted_city:
    #item[1]がdict型, valueでソート
    sorted_score = sorted(item[1].items(), key=lambda x:x[1], reverse=True)
    for item2 in sorted_score:
        print(item2[0]+1)

