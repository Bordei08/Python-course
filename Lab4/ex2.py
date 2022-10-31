import os

def ex2(director, fisier):
    try:
        f = open(fisier, "a")
        dList = os.listdir(director)
        result = list()
        for file in dList:
            if  os.path.isfile(file)  and file[0] == 'A':
                f.write(director + '\\' + file + '\n')
        return 'Done'        
    except:
        print("Nu s a putut deschide fisierul")
  

print(ex2('C:\\Users\\Bordei Mihai Gabi\\Desktop\\Lab4PythonTest', 'C:\\Users\\Bordei Mihai Gabi\\Desktop\\ex2File.txt'))       
