from array import *
arr1=array("i",[1,2,3,4,5,6])
print(arr1)

arr2=array("d",[1.1,2.2,3.3])
#print(arr2)

arr1.insert(6,7)     #insert element at last of array
print(arr1)

arr1.insert(0,0)    #insert element at begining of array
print(arr1)

arr1.insert(2,9)    #insert element at middle of array
print(arr1)


def traverseArray(array):
    for i in array:
        print(i)
traverseArray(arr2)


def accessElement(array,index):
    if index >= len(array):
        print("their is no element at givrn index ")
    else:
        print(array[index])

accessElement(arr1,1)


def searchInArray(array ,value):
    for i in array:
        if i==value:
            return array.index(value)
    return "the element doesn't exists in this array"

print(searchInArray(arr2,3.3))

arr1.remove(0)
print(arr1)