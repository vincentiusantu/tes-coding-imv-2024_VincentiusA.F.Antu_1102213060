matriks = [[98, 88, 78],
           [77, 78, 79],
           [66, 67, 68],
           [32, 33, 31]]

matriks_transpose = [[0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0]]

for i in range(4):
    for j in range(3):
        matriks_transpose[j][i] = matriks[i][j]
        
for i in range(3):
    for j in range(4):
        print(matriks_transpose[i][j], end=' ')
    print('\n')