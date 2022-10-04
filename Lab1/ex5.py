def finish(m):
    for i in range (0,len(m)):
        for j in range (0,len(m)):
            if m[i][j] != 1:
                return 0
            

def readSpiralMod(m):
    mflag = [[0 for _ in range(len(m))] for _ in range(len(m))]
    print(mflag)
    maxim = len(m) - 1
    minim = 0
    s = ""
    while finish(mflag) == 0 :
        for i in range (0, len(m)):
            if mflag[minim][i] == 0:
                mflag[minim][i] = 1
                s = s + m[minim][i]
        for i in range (0, len(m)):  
            if mflag[i][maxim] == 0:
               mflag[i][maxim] = 1
               s = s + m[i][maxim]     
        for i in range (len(m) - 1, 0, -1):
            if mflag[maxim][i] == 0:
                mflag[maxim][i] = 1
                s = s + m[maxim][i]
        for i in range (len(m) - 1, 0, -1): 
            if mflag[i][minim] == 0:
                mflag[i][minim] = 1
                s = s + m[i][minim]
        minim = minim + 1
        maxim = maxim - 1


    return s                

    



a = [['f','i','r','s'],['n','_','l','t'],['o','b','a','_'],['h','t','y','p']]
print(readSpiralMod(a))    