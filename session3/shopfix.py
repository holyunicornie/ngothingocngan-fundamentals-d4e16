def print_menu ():
    print('our items:')
    for i in range(len(menu)):
        print(f'{i+1}.menu{i}')

menu = [T-shirt, jeans, sweater]

while True:
choice = input('Welcome (C,R,U,D)')
choice = choice.upper() #hoac choice.lower()
if choice == 'C':
    new_item = input('enter new item')
    menu.append(new_item)
    print_menu()
elif choice == 'R':
    print_menu()
elif choice == 'U':
    index = int(input('Enter update position')) - 1
    menu[index] = input('enter new value')
    print_menu()
elif choice == 'D':
    index = int(input('Enter update position')) - 1
    menu.pop(index)
    print_menu()
else:
    print('invalid action')
    break 