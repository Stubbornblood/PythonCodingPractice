
def sumDigonal(a):
    temp = 0
    emp = 0
    
    for i in range(len(a)):
        temp += a[i][i]
    for j in range(len(a)):
        emp += a[j][len(a)-1-j]
  
    print(abs(temp-emp))
            




a = [[1,2,3],[4,5,6],[9,8,9]]
sumDigonal(a)