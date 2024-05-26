
def LargestSmallest(s):
    for i in range(len(s)):
        for j in range(0,len(s)-i-1):
            if s[j] < s[j+1]:
                s[j],s[j+1] = s[j+1],s[j]
                
    return s[0],s[-1]




arr = [64, 34, 25, 12, 22, 11, 90]
print(LargestSmallest(arr))
