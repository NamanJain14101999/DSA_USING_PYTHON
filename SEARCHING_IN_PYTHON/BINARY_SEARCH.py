def binary_search(a,v):
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
binary_search(ar,va)
