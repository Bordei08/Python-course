import os

def ex7(file):
    result = dict()
    
    try:
        assert(os.path.isfile(file)),"Calea nu este calea unui fisier"
        result["full_path"] = os.path.abspath(file)
        result["file_size"] = os.path.getsize(file)
        if '.' in file:
            result["file_extension"] = file.split(".")[1]
        else:
            result["file_extension"] = ""
        result["can_read"] = os.access(file,os.R_OK)
        result["can_write"] = os.access(file,os.W_OK)
        return result
    except Exception as e:
        print(str(e))
        return {}



print(ex7('C:\\Users\\Bordei Mihai Gabi\\Desktop\\ex2File.txt'))    