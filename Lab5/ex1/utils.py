def isPrim(x):
    if x < 2 or (x != 2 and x % 2 == 0):
        return False
    for i in range(3, int(x/2), 2):
        if x % i == 0:
            return False
    return True            

def process_item(x):
    if x % 2 == 0 or x == 1:
        n = x + 1
    else:
        n = x + 2    
    while isPrim(n) == False:
        n = n + 2
    return n    

print("Number :")
number = int(input())
print("Result : ")
print(process_item(number))