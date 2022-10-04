def cmmdc(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

input1 = input()
numbers = str(input1).split(" ")
if len(numbers) == 1:
    res = int(numbers[0])
elif len(numbers) == 2:    
    res = cmmdc(int(numbers[0]), int(numbers[1]))
elif len(numbers) > 2:
    res = cmmdc(int(numbers[0]), int(numbers[1]))
    for i in range (2, len(numbers)):
        res = cmmdc(res,int(numbers[i]))
print(res)

            