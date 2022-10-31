import os
 
def ex1(directory):
    dList = os.listdir(directory)
    result = list()
    for x in dList:
        result.append(x.split(".")[1])
    
    result = list(set(result))

    return sorted(result)

print(ex1('C:\\Users\\Bordei Mihai Gabi\\Desktop\\Lab4PythonTest'))    