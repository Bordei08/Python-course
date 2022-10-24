def intersected(a,b):
    result = set()
    result = a.intersection(b)
    return result

def reunited(a,b):
    result = set()
    result = result.union(a,b)
    ## else result.update(a)  result.update(b)
    return result

def minus(a,b):
    result = set()
    result.update(a)
    result = result.difference(b)
    return result

def ex1(a,b):
   result = list()
   result.append(intersected(a,b))
   result.append(reunited(a,b))
   result.append(minus(a,b))
   result.append(minus(b,a))
   return result


print(ex1({1,2,},{2,3}))    