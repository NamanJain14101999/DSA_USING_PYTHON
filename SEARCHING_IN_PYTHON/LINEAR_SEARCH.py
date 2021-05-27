def linear_search(a,value):
    for i in a:
        if i==value:
            return 1
    return -1
a=[1,2,3,4,5]
v=2
result=linear_search(a,v)
if result==1:
    print("item founded")
else:
    print("item not founded")