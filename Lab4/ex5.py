import os

result = list()
def searchInFile(target, to_search):
    try:
        f = open(to_search, "r")
        text = f.read()
        f.close()
        if target in text:
            result.append(to_search)
    except:
        print('Nu s a putut deschide fisierul ' + target)        


def searchInDirectory(target,to_search):
    files = os.listdir(to_search)
    for x in files:
        if os.path.isfile(to_search + '\\' + x):
            searchInFile(target,to_search + '\\' + x)
        else:
            searchInDirectory(target, to_search + '\\' + x)    

def ex5(target, to_search):
    
    if os.path.isfile(target):
        searchInFile(target,to_search)
    else:
        searchInDirectory(target, to_search)

    testing = len(result)
    
    if len(result) == 0:
        raise ValueError('Target ul nu a fost gasit')
       
    return result        


print(ex5('Lab4', 'C:\\Users\\Bordei Mihai Gabi\\Desktop\\Lab4PythonTest'))    