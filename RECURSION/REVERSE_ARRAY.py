def rev(arr,i,j):
    if i==j:
        print(arr[i])
        return 
    else:
        print(a[j])
        rev(arr,i,j-1)
        return 
a=[1,2,3,4,5,6]
i=0
j=len(a)-1
# rev(a,i,j)

def min(arr,i,j):
    if i==j:
        print(arr[i])
        return 
    else:
        if a[i]>a[j]:
            min(arr,i+1,j)
        else:
            min(arr,i,j-1)
min(a,i,j)
