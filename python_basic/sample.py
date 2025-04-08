import numpy as np


l1 = np.array([23,45,67,56,89,90,23,32])
l2 = l1
l2 is l1
print(id(l1))
print(id(l2))

l3 = l1.copy()
print(id(l3))
l3 is l1
l3.base is l1
l3.base is l2
l3.flags.owndata
l3 = l3.reshape(2,4)
print(l3)
print(l1)
print(l2)
l3[1,1] = 99999

print(l1)
print(l2)
print(l3)


def match_point(point):
    match point:
        case (0,0):
            print("Origin")
        case (0,y):
            print(f"Y={y}")
        case (x,0):
            print(f"X={x}")
        case (x,y):
            print(f"X={x},Y={y}")
        case _:
            raise ValueError("Not a point")
        
match_point((4,0))
match_point("")

def foo(**some_input):
    for k in some_input:
        print(k,": ",some_input[k])

def foo2(*some_input):
    for element in some_input:
        print(element)

foo(a='apple',b='ball',c='candle')
foo2(4,6,7)



