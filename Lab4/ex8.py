import os

def ex8(directory):
    result = list()
    try:
        files = dList = os.listdir(directory)
        for x in files:
            if os.path.isfile(x):
                result.append(directory + '\\' + x)
        return result
    except Exception as e:
        print(str(e))
        return []

print(ex8('C:\\Users'))                    