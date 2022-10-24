def ex6(input):
    lenInput = len(input)
    inputSet = set(input)
    n2 = lenInput - len(inputSet)
    n1 = len(inputSet) - n2
    return (n1, n2)


print(ex6([1,2,1,2,3,4,5]))