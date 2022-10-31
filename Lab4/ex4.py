import os
import sys

def ex4(input):
    directory = str()
    for i in range(1, len(input)):
        if i == len(input) - 1:
            directory = directory + input[i] 
        else:    
            directory =directory +  input[i] + ' '    
    return sorted(list(set(list( x.split(".")[1] for x in list(filter(lambda x: (os.path.isfile(directory + '\\'+x)), os.listdir(directory)))))))

print(ex4(list(sys.argv)))
