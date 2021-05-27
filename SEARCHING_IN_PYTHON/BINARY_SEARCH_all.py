'''def binary_search(a,v):
    l=0
    h=len(a)
    if h>=l:
        f=-1
        while l<=h:
            mid=l+(h-l)//2
            #mid=(l+h)//2 # use here mid=l+(h-l)//2 which will work very efficiently for large test
            if a[mid]==v:
                f=1
                break
            elif v>a[mid]:
                l=mid+1
            else:
                h=mid-1
        if f==1:
            print("item founded")
        else:
            print("item not founded")
ar=[1,2,3,4,5]
va=4
binary_search(ar,va)'''


'''def binary_search(a,v): when array in decresing order binary search
    l=0
    h=len(a)
    if h>=l:
        f=-1
        while l<=h:
            mid=l+(h-l)//2
           # mid=(l+h)//2 # use here mid=l+(h-l)//2 which will work very efficiently for large test cases
            if a[mid]==v:
                f=1
                break
            elif v<a[mid]:
                l=mid+1
            else:
                h=mid-1
        if f==1:
            print("item founded")
        else:
            print("item not founded")
#ar=[1,2,3,4,5]
ar=[5,4,3,2,1]
va=4
binary_search(ar,va)'''

'''
#order- ignoistic binary search in which we dont know array is sorted in asc or des order
def binary_search(a,v):
    l=0
    h=len(a)
    asc=0
    if a[0]>a[1]:
        asc=1
    if h>=l:
        f=-1
        while l<=h:
            mid=l+(h-l)//2
           # mid=(l+h)//2 # use here mid=l+(h-l)//2 which will work very efficiently for large test cases
            if a[mid]==v:
                f=1
                break
            if asc==0:
                if v<a[mid]:
                    h=mid-1
                else:
                    l=mid+1
            else:
                if v<a[mid]:
                    l=mid+1
                else:
                    h=mid-1
        if f==1:
            print("item founded")
        else:
            print("item not founded")
ar=[1,2,3,4,5]
#ar=[5,4,3,2,1]
va=4
binary_search(ar,va)'''

''' binary search program to calculate the firs tand last occurance of a number on array
def first(a,x,n):
    res=-1
    l=0
    h=n-1
    while l<=h:
        mid=l+(h-l)//2
        if a[mid]>x:
            h=mid-1
        elif a[mid]<x:
            l=mid+1
        else:
            res=mid
            h=mid-1
    return res

arr=[1,2,2,2,3,4]
print("first occur ",first(arr,4,len(arr)))

def last(a,x,n):
    res=-1
    l=0
    h=n-1
    while l<=h:
        mid=l+(h-l)//2
        if a[mid]>x:
            h=mid-1
        elif a[mid]<x:
            l=mid+1
        else:
            res=mid
            l=mid+1
    return res

arr=[1,2,2,2,3,4]
print("last occur ",last(arr,4,len(arr)))'''
'''
def rotate(b,n):
    l=0
    h=n-1
    if h<l:
        return 0
    if h==l:
        return l
    mid=l+(h-l)//2
    while l<=h:
        next=(mid+1)%n
        prev=(mid-1+n)%n
        if b[mid]<=b[next] and b[mid]<=b[prev]:
            return mid
        elif mid<=h:
            h=mid-1
        elif mid>=l:
            l=mid+1
#a=[1,2,3,4,5]
b=[5,4,3,2,1]
print(rotate(b,len(b)))'''

'''
def countRotations(arr,low, high): 
  # This condition is needed to 
  # handle the case when array 
  # is not rotated at all 
  if (high < low): 
    return 0
  # If there is only one 
  # element left 
  if (high == low): 
    return low 
  # Find mid 
  # (low + high)/2 
  mid = low + (high - low)/2; 
  mid = int(mid) 
  # Check if element (mid+1) is 
  # minimum element. Consider 
  # the cases like {3, 4, 5, 1, 2} 
  if (mid < high and arr[mid+1] < arr[mid]): 
    return (mid+1) 
  # Check if mid itself is 
  # minimum element 
  if (mid > low and arr[mid] < arr[mid - 1]): 
    return mid 
  # Decide whether we need to go 
  # to left half or right half 
  if (arr[high] > arr[mid]): 
    return countRotations(arr, low, mid-1); 
  return countRotations(arr, mid+1, high) 

arr = [15, 18, 2, 3, 6, 12] 
n = len(arr) 
print(countRotations(arr, 0, n-1))'''

