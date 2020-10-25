mon_an1 = 'phở'
mon_an2 = 'cơm'
mon_an3 = 'bún'
mon_an4 = 'thịt chó'
#list
foods = ['phở', 'cơm', 'bún', 'thịt chó', 'bún đậu'] 
#list có thể chứa bất cứ kiểu dữ liệu: boolean, int...
a = input('Enter new items')
foods.append(a) #CREAT
# mon_thit_cho = foods[3] thì đổi foods[3] = 'thịt bò' sẽ ko thay đổi
foods[3] = 'thịt bò' #UPDATE

foods.remove('phở') #DELETE by value #xóa thằng đầu tiên ở trong list, vd có 2 phở
foods.pop(0) #điền số index (lệnh pop lưu dữ liệu vào biến, vd removed_item = foods.pop(0) )
index = foods.index('bún đậu')
print(foods[index])

print('bún đậuu' in foods)



print(foods)
for i in range(4):
    print(foods[i])
print(foods)


for i in foods:
    print(i)
print(len(foods))
for i in range(len(foods)):
    print(i, foods[i])
for food in foods:
    print(i)
print(a)
print(foods)

