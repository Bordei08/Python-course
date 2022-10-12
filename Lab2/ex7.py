def isPal(x):
    cn = x
    pal = 0
    while cn :
        pal = pal * 10 + int(cn % 10)
        cn = int(cn / 10)

    return x == pal


def pal(list):
    countPal = 0
    maxPal = 0
    for x in list:
        if isPal(x) :
            countPal = countPal + 1
            if maxPal < x:
                maxPal = x
    return countPal, maxPal


print(pal([12,11,22,33,44,55,90]))
