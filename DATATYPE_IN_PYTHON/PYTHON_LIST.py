"""
shoppingList=['milk','chess','butter']
#print(shoppingList[0])

l=[1,2,3,4,5,6,7]
print(l)

l.insert(0,11)
print(l)
l.append(55)
print(l)
l.extend([0,0,0])
print(l)
"""
"""
l=['a','b','c','d','e','f']
#print(l[0:2])
#l.pop(1)
#del l[0:2]
l.remove('e')
print(l)
"""
"""
l=[10,20,30,40,50,60,70,80,90]

#if 20 in l:
#    print(l.index(20))
#else:
#    print("the value does'nt exits in the list")

def searchlist(list,value):
    for i in list:
        if i==value:
            return list.index(value)
    return "the value does'nt exits in the list"

print(searchlist(l,20))

"""
"""
a=[1,2,3]
b=[4,5,6]
c=a+b
#print(c)

a=[0,1]
a=a*4
print(a)
"""
a='span1-span2-span3'
delimiter='-'
b=a.split(delimiter)
print(b)

print('@'.join(b))
