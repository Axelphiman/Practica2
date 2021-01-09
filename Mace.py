xInicial = 1
yInicial = 1
xFinal = 3  # 9
yFinal = 8  # 3
xActual = xInicial
yActual = yInicial
xAnterior = xInicial
yAnterior = yInicial
caminoSeguido = []
anteriores = []
bifurcaciones = []
caminosExitosos = []
todoExplorado = False
finalEncontrado = False
maze = []


# maze2 = []


def cargar_laberinto():
    global maze
    file = open("laberinto1.txt")
    lines = file.readlines()
    maze = []
    # maze2 = []
    row = []
    for line in lines:
        for char in line:
            if char in "10":
                row.append(int(char))
        maze.append(row)
        # maze2.append(row)
        row = []


def avanzar():
    global xActual, yActual, xAnterior, yAnterior
    # hacia derecha
    if camino_abierto(0, 1):
        yAnterior = yActual
        yActual += 1
    # hacia abajo
    elif camino_abierto(1, 0):
        xAnterior = xActual
        xActual += 1
    # hacia izquierda
    elif camino_abierto(0, -1):
        yAnterior = yActual
        yActual -= 1
    # hacia arriba
    elif camino_abierto(-1, 0):
        xAnterior = xActual
        xActual -= 1
    else:
        desapilar_por_camino_ciego()


def es_bifurcacion():
    return suma_opciones() < 2


def es_camino_ciego():
    return suma_opciones() == 3


def suma_opciones():
    global xActual, yActual, maze
    x = xActual
    y = yActual
    return maze[x][y + 1] + maze[x - 1][y] + maze[x][y - 1] + maze[x + 1][y]


def camino_abierto(x, y):
    global maze, xActual, yActual, xAnterior, yAnterior, caminoSeguido
    if maze[xActual + x][yActual + y] == 0:
        return True
    return False


def desapilar_por_camino_ciego():
    global xInicial, yInicial, xActual, yActual, xAnterior, yAnterior, caminoSeguido, todoExplorado, maze
    a, b, c = -1, -1, False

    while not c:
        a, b, c = caminoSeguido.pop()
        if a == xInicial and b == yInicial:
            xActual = xInicial
            yActual = yInicial
            xAnterior = xInicial
            yAnterior = yAnterior
            sellar_camino_ciego()
            if suma_opciones() == 4:
                todoExplorado = True
        elif c:
            xActual = a
            yActual = b
            sellar_camino_ciego()
            caminoSeguido.append((a, b, es_bifurcacion()))


def sellar_camino_ciego():
    global maze, xActual, xInicial, yActual, yInicial
    x = xActual
    y = yActual
    avanzar()
    maze[xActual][yActual] = 1
    xActual = x
    yActual = y


# A PARTIR DE AQUÍ EJECUCIÓN DEL PROGRAMA
cargar_laberinto()
caminoSeguido.append((xInicial, yInicial, True))
anteriores.append((xAnterior, yAnterior))
while not todoExplorado:

    print("Coordenada X actual: " + str(xActual) + ".Coordenada Y actual: " + str(yActual))
    avanzar()
    caminoSeguido.append((xActual, yActual, es_bifurcacion()))
    if xActual == xFinal and yActual == yFinal:
        e = caminoSeguido
        caminosExitosos.append(str(caminoSeguido))
        desapilar_por_camino_ciego()
        print("Coordenada X actual: " + str(xActual) + ".Coordenada Y actual: " + str(yActual))
        print("final encontrado")

    if es_camino_ciego():
        desapilar_por_camino_ciego()

print("los caminos hayados al final fueron los siguientes: ")

for element in caminosExitosos:
    print(element)
