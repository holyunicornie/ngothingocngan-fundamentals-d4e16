for y in range (1, 10):
    str_x = ''
    for x in range (1,10):
        if x*y > 9:
            str_x += str(x*y) + ' '  #str_x += : str_x = str_x + str(x)
        else:
            str_x += str(x*y) + '  '
    print(str_x)



