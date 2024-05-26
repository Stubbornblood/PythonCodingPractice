
def compareTriplets(a, b):
    countA = 0
    countB = 0
    c = []
    for i in range(len(a)):
        if a[i]==b[i]:
            pass
        elif a[i] > b[i]:
            countA+=1
        else:
            countB+=1
        
    c.append(countA)
    c.append(countB)
            
    return c 


a = [5,6,7]
b = [3,6,10]
result = compareTriplets(a, b)

print(result)