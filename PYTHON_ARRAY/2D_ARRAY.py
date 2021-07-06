import numpy as np

twoDArray=np.array([[11, 15, 10, 6],[10, 14, 11, 5],[12, 17, 12, 8],[15, 18, 14, 9]])
print(twoDArray)


"""
newArray = np.insert(twoDArray,0,[[1,2,3,4]],axis=1)  # here 0 represent index value , axis=1 means column axis=0 means rows
print(newArray)


new2Array = np.append(twoDArray,[[1,2,3,4]],axis=0) # it will append new row or column at last of it 
print(new2Array)

"""

"""

in this we access the elements in array

def accessElement(array,rowIndex,colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print("incorrect index")
    else:
        print(array[rowIndex][colIndex])

accessElement(twoDArray,1,2)

"""

"""
def traverseArray(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j],end=" ")
        print()
traverseArray(twoDArray)
"""

"""
search in 2d array

def searchArray(array,value):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == value:
                return "the value is located at index "+str(i)+","+str(j)

    return "the element is not found"

print(searchArray(twoDArray,14))
"""

"""
in this we delete a row or column in array

new2DArray=np.delete(twoDArray,0,axis=0)
print(new2DArray)

"""

