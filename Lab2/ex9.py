def getSpectator(m):
    result = []
    for i in range(0,len(m[0])):
        maxim = m[0][i]
        for j in range(1, len(m)):
            if m[j][i] <= maxim:
                a = (j,i)
                result.append(a)
            else:
                maxim = m[j][i]    
    print(result)            


getSpectator([[1, 2, 3, 2, 1, 1],
[2, 4, 4, 3, 7, 2],
[5, 5, 2, 5, 6, 4],
[6, 6, 7, 6, 7, 5]] )        