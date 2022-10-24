def ex3(a, b):
    setAKeys = set()
    setBKeys = set()
    setAKeys.update(a.keys())
    setBKeys.update(b.keys())
    ## sau puteam verifica cu operatorul 'in' pentru fiecare cheie din A daca exista in B
    if setAKeys.symmetric_difference(setBKeys):
        return False

    for x in setAKeys:
        if type(a.get(x)) is type(b.get(x)):
            if type(a.get(x)) is dict and not ex3(a.get(x), b.get(x)):
                return False
            elif a.get(x) != b.get(x):
                return False  
        else:
            return False   
    return True         
   

print(ex3(      {   'd':{
                            'name' : 'ana'
                        },
                    'list': ['one', 'two'],
                    'number' : 2, 
                    'string' : 'Lalalala'
                },
                {   'list': ['one', 'two'],
                    'string' : 'Lalalala',
                    'number' : 2,
                    'd':{
                        'name' : 'ana'
                        }
                }))