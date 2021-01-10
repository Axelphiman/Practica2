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


def contar_ceros():
    global maze
    i = 0
    for x in range(12):
        for y in range(12):
            if maze[x][y] == 0:
                i = i + 1
    return i


def es_camino_ciego(x, y):
    global maze, xInicial, yInicial, xFinal, yFinal
    if (x == xInicial and y == yInicial) or (x == xFinal and y == yFinal):
        return False
    else:
        return suma_opciones(x, y) >= 3


def suma_opciones(x, y):
    global maze
    return maze[x][y + 1] + maze[x][y - 1] + maze[x + 1][y] + maze[x - 1][y]


def sellar_camino_ciego():
    global maze, cantidadDeCeros
    i = 0
    while i <= cantidadDeCeros:
        for x in range(1, 11):
            for y in range(1, 11):
                if es_camino_ciego(x, y):
                    maze[x][y] = 1
        i += 1


def avanzar():
    global xActual, yActual
    x = random.randint(1, 4)
    # derecha
    if camino_despejado(0, 1) and x == 1:
        yActual = yActual + 1
    # abajo
    elif camino_despejado(1, 0) and x == 2:
        xActual = xActual + 1
    # izquierda
    elif camino_despejado(0, -1) and x == 3:
        yActual = yActual - 1
    # arriba
    elif camino_despejado(-1, 0) and x == 4:
        xActual = xActual - 1
    else:
        print("algo se hizo mal")


def camino_despejado(x, y):
    global maze, xActual, yActual
    return maze[xActual + x][yActual + y] == 0


# A PARTIR DE AQUÍ EJECUCIÓN DEL PROGRAMA
cargar_laberinto()

caminoSeguido.append((xInicial, yInicial, True, xInicial, yInicial))

# DEBUG PRINTS
# print(cantidadDeCeros)
# for element in maze:
#    print(element)
