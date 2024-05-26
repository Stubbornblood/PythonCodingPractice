
def plusMinus(a):
    n = len(a)
    pcount = 0
    ncount = 0
    ocount = 0
    
    for i in range(n):
        if a[i]>0:
            pcount+=1
        elif a[i]<0:
            ncount+=1
        else:
            ocount+=1    
    print(pcount/n)
    print(ncount/n)
    print(ocount/n) 
    
    


a = [1,1,0,-1,-1]
print(plusMinus(a))