
#Triangles with different orientation

def left_oriented_tri(symbol, depth):
    for i in range(1, depth, 1):
        print(str(symbol) * i)

def centered_oriented_tri(symbol, depth):
    for i in range(depth):
        if i % 2 == 1:
            print('{:^10}'.format(str(symbol) * i))

def diamond_shape(symbol, depth):
    for i in range(depth):
        if i % 2 == 1:
            print('{:^20}'.format(str(symbol)*i))
    for j in range(depth, 0, -1):
        if j % 2 ==1:
            print('{:^20}'.format(str(symbol)*j))

#using the defined functions

left_oriented_tri('x', 5)
centered_oriented_tri('x', 10)
diamond_shape('o', 10)