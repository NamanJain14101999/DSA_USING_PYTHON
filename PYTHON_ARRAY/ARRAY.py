import array
array1=array.array('i',[10,20,30,40,50])
#print(array1)
#for i in array1:
    #print(i)

#marray=array.array('d',[1.2,3.2,4.3,5.4])
#print(marray)

arr=bytes((1,2,3,4))  # byte array it range is from 0-255
#print(arr[1])    # bytes are immutable

a=bytearray((1,2,3,4)) # it is mutable 
a[1]=21
#print(a)


b=array.array('i',[100,200,300])
#print(b)
b.insert(2,150)
#print(b)
b.remove(150)
#print(b)
#print(b.index(200))
b.append(400)
#print(b)
a=array.array('i',[ 10,20,30])
b=array.array('i',[ 100,200,300])
a.extend(b)
#print(a)

#list
l=[10,20,30,40,"hello",40.5]
#print(l)

b=[10,20,30,20]
print(b.index(20))


