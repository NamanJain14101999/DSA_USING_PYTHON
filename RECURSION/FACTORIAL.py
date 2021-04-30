#import sys
#sys.setrecursionlimit(10000)
def factorial(n):
    assert n >= 0 and int(n) == n , "this number must be poistive integer only"
    if n in [1,0]:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))