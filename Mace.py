xInicial = 1
yInicial = 1
xFinal = 3  # 9
yFinal = 8  # 3
xActual = xInicial
yActual = yInicial
xAnterior = xInicial
yAnterior = yInicial
bifurcaciones = []
caminoSeguido = []
caminosExitosos = []
todoExplorado = False
finalEncontrado = False
mace = []


# mace2 = []


def cargar_laberinto():
    global mace
    file = open("laberinto1.txt")
    lines = file.readlines()
    mace = []
    # mace2 = []
    row = []
    for line in lines:
        for char in line:
            if char in "10":
                row.append(int(char))
        mace.append(row)
        # mace2.append(row)
        row = []


def avanzar():
    global xActual, yActual, xAnterior, yAnterior, bifurcaciones
    bifurcaciones.append((xActual, yActual, es_bifurcacion()))
    # hacia derecha
    if coordenadas_avance(0, 1):
        yAnterior = yActual
        yActual += 1
    # hacia abajo
    elif coordenadas_avance(1, 0):
        xAnterior = xActual
        xActual += 1
    # hacia izquierda
    elif coordenadas_avance(0, -1):
        yAnterior = yActual
        yActual -= 1
    # hacia arriba
    elif coordenadas_avance(-1, 0):
        xAnterior = xActual
        xActual -= 1


def es_bifurcacion():
    return suma_opciones() < 2


def es_camino_ciego():
    return suma_opciones() == 3


def camino_cerrado():
    return suma_opciones() == 3


def suma_opciones():
    global xActual, yActual, mace
    x = xActual
    y = yActual
    return mace[x][y + 1] + mace[x - 1][y] + mace[x][y - 1] + mace[x + 1][y]


def coordenadas_avance(x, y):
    global mace
    global xActual
    global yActual
    if mace[xActual + x][yActual + y] == 0:
        return True
    return False


def desapilar_por_camino_ciego():
    a, b, c = -1, -1, False
    while not c:
        a, b, c = bifurcaciones.pop()
    bifurcaciones.append((a,b,c))

# A PARTIR DE AQUÍ EJECUCIÓN DEL PROGRAMA
cargar_laberinto()

while not finalEncontrado:
    print("Coordenada X actual: " + str(xActual) + ".Coordenada Y actual: " + str(yActual))
    avanzar()
    print(bifurcaciones)
    if xActual == xFinal and yActual == yFinal:
        finalEncontrado = True
        print("Coordenada X actual: " + str(xActual) + ".Coordenada Y actual: " + str(yActual))
        print("final encontrado")
