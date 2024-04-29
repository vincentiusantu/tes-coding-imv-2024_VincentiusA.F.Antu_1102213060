for i in range(0,7):
    for k in range(i,7):
        print(" ", end="")
    for j in range(0,i):
        print("* ", end="")
    print('\n')

for i in range(0,7):
    for k in range(0,i):
        print(" ", end="")
    for j in range(i,7):
        print("* ", end='')
    print("\n")