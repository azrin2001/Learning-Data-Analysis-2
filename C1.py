x=1
y=2
Z=x+y
print(Z)
def p(m,n):
    return m+n
print(p(1,3))
def add_numbers(x,y,z=None):
    if (z==None):
        return x+y
    else:
        return x+y+z

print(add_numbers(3, 2))
print(add_numbers(1, 2, 3))