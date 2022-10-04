def convertString(s):
    i = 1
    if s[0].isupper():
        s[0] = s[0].lower()
    if s[len(s) - 1].isupper():
        s[len(s) - 1] = s[len(s) - 1].lower()  
    while i < len(s) - 1:
        if s[i].isupper():
            s = s[:i]+"_"+s[i:]
            print(s[i])
            i = i + 1     
        i = i + 1

    print(s.lower())

convertString("gabiEsteBine")            
