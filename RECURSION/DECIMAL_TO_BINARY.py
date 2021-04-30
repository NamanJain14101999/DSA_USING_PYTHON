def D_to_B(n):
    assert int(n)==n,"number should be integer only"
    if n==0:
        return 0
    else:
        return n%2+10*D_to_B(int(n/2))
print(D_to_B(13))