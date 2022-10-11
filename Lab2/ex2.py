def isPrime(x):
    if x < 2 or x != 2 and x % 2 == 0 :
        return 0
    for i in range(3, int(x / 2), 2):
        if x % i == 0:
            return 0
    return 1


def listPrime(x):
    i = 0
    while i < len(x):
        if isPrime(x[i]) == 0:
            x.pop(i)
        else:
            i = i + 1
    return x

print(listPrime([1,2,3,4,5,9,8,3,20,21,31]))                        
