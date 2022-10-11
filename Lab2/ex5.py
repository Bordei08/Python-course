def modMatrix(m):
    for i in range(0, len(m)):
        for j in range(0, len(m)):
            if i > j:
                m[i][j] = 0
    return m
# sub Diagonala principala i > j
print(modMatrix([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]))                