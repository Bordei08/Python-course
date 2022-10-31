import os

result = list()

def isFile(path):
    try:
        f = open(path, "r")
        text = str(f.read())
        resultS = ""
        for i in range(len(str(text)) - 20, len(str(text))):
            resultS = resultS + text[i] 
        return resultS    
    except:
        return "Nu s a putut deschide fisierul "    


def isDirectory(path):
    dList = os.listdir(path)
    
    for item in dList:
        if os.path.isfile( path+'\\'+item):
            result.append(item.split(".")[1])
        else:
            isDirectory(path + '\\' + item)
    
    return result


def ex3(path):
    if os.path.isfile(path) :
        return isFile(path)
    resultF = list()
    files = isDirectory(path)
    
    while 0 != len(files):
        count = 1
        j = 1
        while j < len(files):
            if files[0] == files[j]:
                count = count + 1
                files.pop(j)
            else:    
                j = j + 1
        resultF.append((files[0], count))
        files.pop(0)
    return sorted(resultF, key=lambda el:el[1],reverse=True)



##file test
print(ex3('C:\\Users\\Bordei Mihai Gabi\\Desktop\\ex2File.txt'))
##file directory
print(ex3('C:\\Users\\Bordei Mihai Gabi\\Desktop\\Lab4PythonTest'))