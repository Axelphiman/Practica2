import random

xInicial = 1
yInicial = 1
xFinal = 10
yFinal = 10
maze = []
xActual = xInicial
yActual = yInicial
cantidadDeCeros = 0
caminoSeguido = []
caminosExitosos = []


def cargar_laberinto():
    global maze, cantidadDeCeros
    file = open("laberinto1.txt")
    lines = file.readlines()
    maze = []
    row = []
    for line in lines:
        for char in line:
            if char in "10":
                row.append(int(char))
        maze.append(row)
        row = []
    cantidadDeCeros = contar_ceros()
    sellar_camino_ciego()
    cantidadDeCeros = contar_ceros()


def contar_ceros():
    global maze
    i = 0
    for m in range(12):
        for n in range(12):
            if maze[m][n] == 0:
                i = i + 1
    return i


def es_camino_ciego(xx, yy):
    global maze, xInicial, yInicial, xFinal, yFinal
    if (xx == xInicial and yy == yInicial) or (xx == xFinal and yy == yFinal):
        return False
    else:
        return suma_opciones(xx, yy) >= 3


def suma_opciones(x1, y1):
    global maze
    return maze[x1][y1 + 1] + maze[x1][y1 - 1] + maze[x1 + 1][y1] + maze[x1 - 1][y1]


def sellar_camino_ciego():
    global maze, cantidadDeCeros
    i = 0
    while i <= cantidadDeCeros:
        for x4 in range(1, 11):
            for y in range(1, 11):
                if es_camino_ciego(x4, y):
                    maze[x4][y] = 1
        i += 1


def avanzar():
    global xActual, yActual, xInicial, yInicial, xFinal, yFinal
    caminoSeguido.append((xActual, yActual))
    w = random.randint(1, 4)
    # derecha
    if camino_despejado(0, 1) and w == 1:
        xActual = xActual
        yActual = yActual + 1
    # abajo
    elif camino_despejado(1, 0) and w == 2:
        yActual = yActual
        xActual = xActual + 1
    # izquierda
    elif camino_despejado(0, -1) and w == 3:
        xActual = xActual
        yActual = yActual - 1
    # arriba
    elif camino_despejado(-1, 0) and w == 4:
        yActual = yActual
        xActual = xActual - 1
    else:
        if camino_despejado(0, 1):
            xActual = xActual
            yActual = yActual + 1
        elif camino_despejado(1, 0):
            yActual = yActual
            xActual = xActual + 1
        elif camino_despejado(0, -1):
            xActual = xActual
            yActual = yActual - 1
        elif camino_despejado(-1, 0):
            yActual = yActual
            xActual = xActual - 1


def camino_despejado(x2, y2):
    global maze, xActual, yActual
    return maze[xActual + x2][yActual + y2] == 0


# A PARTIR DE AQUÍ EJECUCIÓN DEL PROGRAMA
cargar_laberinto()
for x in range(100000):
    avanzar()
    w = caminoSeguido.copy()
    w.pop()
    if (xActual, yActual) in w:
        xActual = xInicial
        yActual = yInicial
        caminoSeguido.clear()
        w.clear()
    if (xActual == xFinal) and (yActual == yFinal):
        caminoSeguido.append((xActual, yActual))
        s = caminoSeguido.copy()

        if len(s) <= cantidadDeCeros:
            caminosExitosos.append(str([s]))
        caminoSeguido.clear()
        xActual = xInicial
        yActual = yInicial

print(len(caminosExitosos))
newlist = sorted(set(caminosExitosos), key=lambda x: caminosExitosos.index(x))

for element in newlist:
    print(element)

print(len(newlist))
# DEBUG PRINTS
# print(caminosExitosos.pop())
# print(len(caminosExitosos))
# print(cantidadDeCeros)
# for element in maze:
# print(element)
