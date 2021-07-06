mytupe=(1,2,3,4,5)
#newtuple=tuple("123435")
#print(newtuple) tuple is indexable but it cannot be updateable tuple is immutable
#print(mytupe[1])

#for i in range(len(mytupe)):
    #print(mytupe[i])

def search(tup,ele):
    for i in tup:
        if i==ele:
            return tup.index(i)
    else:
        return "not found"

#print(search(mytupe,3))

new=(2,3,4,5,6)

# print(mytupe+new)

# print(mytupe*3)

# only two function are in tuple they are-> count(),index()

# print(mytupe.count(2))
print(mytupe.index(2))