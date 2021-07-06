from array import *

#1 create an array and travserse.
my_array=array("i",[1,2,3,4,5])

for i in my_array:
    print(i)
print("----------------------------------------")

#2 access individual elements through indexes.
print(my_array[0])
print("----------------------------------------")

#3 append any value to the array using append() method
my_array.append(6)
print(my_array)
print("----------------------------------------")

#4 insert value in an array using insert() method
my_array.insert(3,11)
print(my_array)
print("----------------------------------------")

#5 extend python array using extend() method
my_array1=array("i",[10,11,12])
my_array.extend(my_array1)
print(my_array)
print("----------------------------------------")

#6 add items from list into array using fromlist() method
tempList=[20,21,22]
my_array.fromlist(tempList)
print(my_array)
print("----------------------------------------")

#7 remove any array element using remove() method
my_array.remove(22)
print(my_array)
print("----------------------------------------")

#8 remove last array element using pop() method
my_array.pop()
print(my_array)
print("----------------------------------------")

#9 fetch any element through its index using index() emthod
print(my_array.index(20))
print("----------------------------------------")

#10 reverse a python array using reverse() method

my_array.reverse()
print(my_array)
print("----------------------------------------")

#11 get array bufer information through buffer_info() method
print(my_array.buffer_info())
print("----------------------------------------")

#12 check for number of occurreneces of an element usinf count() method
print(my_array.count(11))
print("----------------------------------------")

#13 convert array to string using tostring() method
strTemp=my_array.tostring()
print(strTemp)
ints=array("i")
ints.fromstring(strTemp)
print(ints)
print("----------------------------------------")

#14 convert array to a python list with same elements using tolist() method
print(my_array.tolist())
print("----------------------------------------")

#15 slice elements from an array
print(my_array[1:4])
print("----------------------------------------")