count = 0
while count <7:
    username = input('username:')
    if username == 'd4e':
        password = input('password:')
        if password == 'd4e':
            print('welcome to d4e')
            break
        else:
            count = count + 1
            print('bye')
    else:
        count += 1
        print('bye')    
print('give up pls')