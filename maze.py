xInicial = 9
yInicial = 1
xFinal = 3  # 9
yFinal = 8  # 3
xActual = xInicial
yActual = yInicial
xAnterior = xInicial
yAnterior = yInicial
caminoSeguido = []

bifurcaciones = []
caminosExitosos = []
todoExplorado = False
finalEncontrado = False
maze = []


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

    # derecha
    if camino_despejado(0, 1) and no_devolverse(0, 1):
        yAnterior = yActual
        xAnterior = xActual
        yActual = yActual + 1
    # abajo
    elif camino_despejado(1, 0) and no_devolverse(1, 0):
        yAnterior = yActual
        xAnterior = xActual
        xActual = xActual + 1
    # izquierda
    elif camino_despejado(0, -1) and no_devolverse(0, -1):
        yAnterior = yActual
        xAnterior = xActual
        yActual = yActual - 1
    # arriba
    elif camino_despejado(-1, 0) and no_devolverse(-1, 0):
        yAnterior = yActual
        xAnterior = xActual
        xActual = xActual - 1
    else:
        print("algo se hizo mal")


def es_bifurcacion():
    return suma_opciones() < 2


def es_camino_ciego():
    return suma_opciones() == 3


def suma_opciones():
    global xActual, yActual, maze
    x = xActual
    y = yActual
    return maze[x][y + 1] + maze[x - 1][y] + maze[x][y - 1] + maze[x + 1][y]


def camino_despejado(x, y):
    global maze, xActual, yActual
    return maze[xActual + x][yActual + y] == 0


def no_devolverse(x, y):
    global xActual, yActual, xAnterior, yAnterior
    return not (((xActual + x) == xAnterior) and ((yActual + y) == yAnterior))


def desapilar_por_camino_ciego():
    global xInicial, yInicial, xActual, yActual, xAnterior, yAnterior, caminoSeguido, todoExplorado
    a, b, c, ww, www = -1, -1, False, -1, -1

    while not c:
        a, b, c, ww, www = caminoSeguido.pop()
        if a == xInicial and b == yInicial:
            xActual = xInicial
            yActual = yInicial
            xAnterior = xInicial
            yAnterior = yAnterior
            sellar_camino_ciego()
            if suma_opciones() == 4:
                todoExplorado = True
        elif c:
            # TODO: simplificar este método poniendo parte en sellar
            xActual = a
            yActual = b
            xAnterior = ww
            yAnterior = www
            sellar_camino_ciego()
            xActual = a
            yActual = b
            xAnterior = ww
            yAnterior = www
            caminoSeguido.append((a, b, es_bifurcacion(), ww, www))


def sellar_camino_ciego():
    global maze, xActual, xInicial, yActual, yInicial, xAnterior, yAnterior
    x = xActual
    y = yActual
    avanzar()
    maze[xActual][yActual] = 1
    xActual = x
    yActual = y


# A PARTIR DE AQUÍ EJECUCIÓN DEL PROGRAMA
cargar_laberinto()
caminoSeguido.append((xInicial, yInicial, True, xInicial, yInicial))

while not todoExplorado:

    print(" X actual: " + str(xActual) + ". Y actual: " + str(yActual))
    print(" X anterior: " + str(xAnterior) + ". Y anterior: " + str(yAnterior))
    avanzar()
    caminoSeguido.append((xActual, yActual, es_bifurcacion(), xAnterior, yAnterior))
    if xActual == xFinal and yActual == yFinal:
        caminosExitosos.append(str(caminoSeguido))
        desapilar_por_camino_ciego()
        print("X actual: " + str(xActual) + ".Y actual: " + str(yActual))
        print("final encontrado")

    elif es_camino_ciego():
        desapilar_por_camino_ciego()

print("los caminos hayados al final fueron los siguientes: ")
if len(caminosExitosos) == 0:
    print("no hay soluciones para mostrar")
else:
    for element in caminosExitosos:
        print(element)
