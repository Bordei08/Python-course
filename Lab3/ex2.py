def ex2(s):
    resultLetters = list()
    
    for i in  range(ord('A'),ord('Z') + 1): 
        afterLen = len(s)
        t = s.replace(chr(i), '')
        beforeLem = len(t)
        resultLetters.insert(i - 65, afterLen - beforeLem)

    for i in  range(ord('a'),ord('z') + 1): 
        afterLen = len(s)
        t = s.replace(chr(i), '')
        beforeLem = len(t)
        resultLetters.insert(i - ord('a') + (ord('Z') - ord('A')) + 1, afterLen - beforeLem)    

    result = dict()
    for i in  range(ord('A'),ord('Z') + 1):
        if resultLetters[i - 65] > 0:
            key = chr(i)
            result[key] = resultLetters[i - 65] 

    for i in  range(ord('a'),ord('z') + 1):
        if resultLetters[i - ord('a') + (ord('Z') - ord('A')) + 1] > 0:
            key = chr(i)
            result[key] = resultLetters[i - ord('a') + (ord('Z') - ord('A')) + 1]             

    return result

print(ex2("Ana has apples"))
