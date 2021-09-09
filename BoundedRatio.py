def boundedRatio(a, l, r):
    b= [False]*len(a)
    for i in range(len(a)):
        for x in range(l,r+1):
            if a[i] == (i+1)*x:
                b[i]=True
        
    return b
