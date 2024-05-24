
def LargestSmallest(s):
    s = sorted(s)
    return s[0],s[-1]




myArray = [8,3,4,6,4,2,6,8]
print(LargestSmallest(myArray))