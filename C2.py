def add_numbers(x, y, z=4, flag=False):
    if (flag):
        print('Flag is true!')
    if (z == None):
        return x + y
    else:
        return (x + y )/ z


print(add_numbers(1, 3, flag=True))