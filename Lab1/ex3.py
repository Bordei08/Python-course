def countSubString(s1, s2):
    count = 0
    i = 0
    while i < len(s2) - (len(s1) - 1):
        if s1 == s2[i:i+len(s1)]:
            i = i + len(s1)
            count = count + 1
        else:
            i = i + 1    
    return count        

print(countSubString(str(input()), str(input())))    