def isPal(x):
    cx =x;
    pal = 0
    while cx != 0:
        pal = (pal + cx % 10)*10
     
        cx = int(cx / 10)
     

    return x == int(pal / 10)


print(isPal(int(input())))        
