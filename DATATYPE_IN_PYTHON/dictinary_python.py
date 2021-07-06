"""mydict={"name":"edy","age":26}
mydict["address"]="london"

def traverse(dict):
    for key in dict:
        print(dict[key])
#traverse(mydict)

def serachdict(dict,value):
    for key in dict:
        if dict[key]==value:
            return key,value
    return "value not found in dict"

#print(serachdict(mydict,26))

mydict["education"]="bachelors"
#print(mydict)

mydict.pop("name")
mydict.popitem()
print(mydict)"""

mydict={"name":"edy","age":26,"address":"london","education":"btech"}
#print(mydict)
# mydict.clear() it will delete complete dictinary and return none
# dict=mydict.copy() it return the shallow copy of given dictionary

#new={}.fromkeys([1,2,3],0)
#print(new)

#print(mydict.get('agesds',"not found "))

# print(mydict.items())
 
#print(mydict.keys())

# print(mydict.popitem()) it will arbitary pop and key value from given dict

# print(mydict.setdefault("nameq","naaaa")) it will return value if key is present if not present then will insert the value by default

#print(mydict.pop("name","is key is not present i will print"))

# print(mydict.values()) it will return of all values in list form 

new={"a":1,"c":2,"d":3}
# mydict.update(new)
# print(mydict)

# python functions on dictinary

# all(dict) it will return true or false baed on condition
#any(dict) it will return true or false based on condition
#print(any(new))
# sorted(itreable,reverse,key)
print(sorted(new,key=len))
