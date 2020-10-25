choice = input('Welcome to the shop, what do you want? (C,R,U,D)')
clothes = ['1. T shirt', '2.Sweater', '3.Denim']
print(clothes)
if choice == 'C':
C = input('Enter new items')
clothes.append(C)
if choice == 'R':
R = int(input('Enter the index'))
removed_item = clothes.pop(R)
#index = int(input('please enter the index'))
#clothes.[index] = str(input('please enter the alternatives'))
#U = clothes.[index]
