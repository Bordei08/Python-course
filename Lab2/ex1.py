def listFibonacci(n):
    result = []
    if n == 1:
        result.append(1)
    elif n == 2:
        result.append(1)
        result.append(1)
    elif n > 2:
        result.append(1)
        result.append(1)
        n = n - 2
        a = 1
        b = 1
        c = 0
        while n:
            c = a + b
            result.append(c)
            n = n - 1
            a = b
            b = c
    return result
    


print(listFibonacci(int(input())))   