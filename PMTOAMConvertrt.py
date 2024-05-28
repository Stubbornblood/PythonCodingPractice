def timeConversion(s):
    n = len(s)
    
    if s[-2:] == "AM":
        eTime = int(s[0:2])
        if eTime == 12:
            val = 0
        else:
            val = 12+eTime
    
    print(str(val) + s[2:])
    
        

v = "07:05:45AM"
timeConversion(v)