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

def ex7(*sets):
    result = dict()
    for i in range(0,len(sets)):
        j = i + 1
        while j < len(sets):
            result[str(sets[i] ) + "|" + str(sets[j])] = reunited(sets[i], sets[j])
            result[str(sets[i] ) + "&" + str(sets[j])] = intersected(sets[i], sets[j])
            result[str(sets[i] ) + "-" + str(sets[j])] = minus(sets[i], sets[j])
            result[str(sets[j] ) + "-" + str(sets[i])] = minus(sets[j], sets[i])
            j = j + 1

    return result   

print(ex7({1,2}, {2,3}))         


