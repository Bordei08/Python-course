def isDivisor(x, y):
    return x % y == 0


def getSolution(*pars):
    x = 1
    flag = True
    list = []
    if len(pars) == 2:
        if str(type(pars[0])).find("int") != -1:
            x = pars[0]
            list = pars[1]
        else:
            flag = pars[1]
            list = pars[0]
    elif len(pars) == 1:
        list = pars[0]        
    else:
        x = pars[0]
        list = pars[1]
        flag = pars[2]

    resultList= []
   

    for i in list:
        j = 0
        list1 = []
        s = i
        while j < len(s):
            if isDivisor(ord(s[j]), x) == flag:
                list1.append(s[j])
            j = j + 1    
        resultList.append(list1)
    return resultList   

print(getSolution(2,["test", "hello", "lab2022"],False))