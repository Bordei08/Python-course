def findNr(txt):
    res = ""
    for i in str(txt):
        if i.isdigit():
            res = res + i
        else:
            res = res + "_"   
            
    
    res = res.split("_")
    for i in range (0, len(res)):
        if res[i] != '':
            return int(res[i])



print(findNr(str(input())))