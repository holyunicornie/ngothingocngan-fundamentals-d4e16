string = 'a b c d e f'

list_char = string.split(' ')
print(list_char)

string = 'a, b, c, d, e, f'

list_char = string.split(', ')
print(list_char)


string = input('...')
list_char = string.split(', ')
print(list_char)


string = 'word'
list_char = list(string)
print(list_char)