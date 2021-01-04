file = open("laberinto1.txt")
lines = file.readlines()
mace = []
mace2 = []
row = []
for line in lines:
    for char in line:
        if char in "10":
            row.append(int(char))
    mace.append(row)
    mace2.append(row)
    row = []


def avanzar(mace, current_x, current_y, last_x, last_y):
    if mace[current_x + 1][current_y + 1] == 0:  # Abajo- Derecha
        return current_x + 1, current_y + 1, current_x, current_y
    elif mace[current_x][current_y + 1] == 0:  # Derecha
        return current_x, current_y + 1, current_x, current_y
    elif mace[current_x - 1][current_y + 1] == 0:  # Arriba-Derecha
        return current_x - 1, current_y + 1, current_x, current_y
    elif mace[current_x - 1][current_y] == 0:  # Arriba
        return current_x - 1, current_y, current_x, current_y
    elif mace[current_x - 1][current_y - 1] == 0:  # Arriba- Izquierda
        return current_x - 1, current_y - 1, current_x, current_y
    elif mace[current_x][current_y - 1] == 0:  # Izquierda
        return current_x, current_y - 1, current_x, current_y
    elif mace[current_x + 1][current_y - 1] == 0:  # Abajo- Izquierda
        return current_x + 1, current_y - 1, current_x, current_y
    elif mace[current_x + 1][current_y] == 0:  # Abajo
        return current_x + 1, current_y, current_x, current_y
    return current_x, current_y, last_x, last_y
def is_bifurcacion(mace, current_x, current_y):
    print(mace[current_x + 1][current_y + 1] + mace[current_x][current_y + 1] + mace[current_x - 1][current_y + 1] + \
           mace[current_x - 1][current_y] + mace[current_x - 1][current_y - 1]
    + mace[current_x][current_y - 1] + mace[current_x + 1][current_y - 1] + mace[current_x + 1][current_y])
    return mace[current_x + 1][current_y + 1] + mace[current_x][current_y + 1] + mace[current_x - 1][current_y + 1] + \
           mace[current_x - 1][current_y] + mace[current_x - 1][current_y - 1]
    + mace[current_x][current_y - 1] + mace[current_x + 1][current_y - 1] + mace[current_x + 1][current_y] < 6


current_x, current_y, last_x, last_y = 1, 1, 1, 1
bifurcaciones_current = []
bifurcaciones_last = []
while True:
    print(current_x, current_y)
    if is_bifurcacion(mace2, current_x, current_y):
        bifurcaciones_current.append((current_x, current_y))
        bifurcaciones_last.append((last_x, last_y))
    current_x, current_y, last_x, last_y = avanzar(mace2, current_x, current_y, last_x, last_y)
    if (current_x, current_y) in bifurcaciones_current:
        current_x, current_y = bifurcaciones_current.pop()
        last_x, last_y = bifurcaciones_last.pop()
        mace2[avanzar(mace2,current_x,current_y,last_x,last_y)[0]][avanzar(mace2,current_x,current_y,last_x,last_y)[1]] = 1
    #for i in range(9):
        #print(i, mace2[i][:])
