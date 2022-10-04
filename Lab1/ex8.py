def countBits1(x):
    count = 0
    while x != 0 :
        if x % 2 != 0:
            count = count + 1
        x = int(x / 2) 

    return count

print(countBits1(24))           