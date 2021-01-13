import random

x_inicial = 1
y_inicial = 1
x_final = 10
y_final = 10
x_actual = x_inicial
y_actual = y_inicial
matriz_laberinto = []
cantidad_de_ceros = 0
camino_seguido = []
caminos_exitosos = []


def cargar_laberinto():
    """Almacena el laberinto en una matriz

    Función:
        Leer las lineas del archivo seleccionado (ver sección  "Jerarquia
        de archivos") para conformar las filas de la matriz y colummnas de la
        matriz

    Modifica:
        matriz_laberinto: le agrega los unos y ceros que conforman el laberinto

    """
    global matriz_laberinto, cantidad_de_ceros
    file = open("../laberintos/laberinto1.txt")
    lines = file.readlines()
    matriz_laberinto = []
    row = []
    m = file.readline()
    for line in lines:
        for char in line:
            if char in "10":
                row.append(int(char))
        matriz_laberinto.append(row)
        row = []
    contar_ceros(len(lines) - 1, len(m))
    sellar_camino_cerrado()
    contar_ceros(len(lines) - 1, len(m))


def contar_ceros(filas, columnas):
    """Cuenta la cantidad de celdas habiles para moverse

    Función:
        evitar bucles infinitos en caminos circulares

    Modifica:
        cantidad_de_ceros: le da el valor de celdas disponibles para el movimiento

    """
    global matriz_laberinto, cantidad_de_ceros
    i = 0
    for filas in range(12):
        for columnas in range(12):
            if matriz_laberinto[filas][columnas] == 0:
                i = i + 1
    cantidad_de_ceros = i


def es_camino_cerrado(x_parametro, y_parametro):
    """Compueba si una celda es o no un camino sin salida

    Función:
        Servir como método de control para otros métodos

    Argumentos:
        x_parametro (int): coordenada x de la casilla a verificar

        y_parametro (int): coordenada y de la casilla a verificar

    Retorno:
        bool: True en caso de que la casilla sea un camino sin salida, falso
        de lo contrario

    """
    global matriz_laberinto, x_inicial, y_inicial, x_final, y_final
    # Notar que una celda es un camino sin salida si la suma del valor de
    # las celdas adyacentes es mayor o igual a 3
    if (x_parametro == x_inicial and y_parametro == y_inicial) \
            or (x_parametro == x_final and y_parametro == y_final):
        return False
    else:
        return suma_adyacentes(x_parametro, y_parametro) >= 3


def suma_adyacentes(x_parametro, y_parametro):
    """Suma los valores de las casillas adyacentes

        Función: método auxiliar a otros métodos que requieren
        comprobar el estado de una casilla

        Argumentos:
            x_parametro: coordenada x de la casilla a verificar

            y_parametro: coordenada y de la casilla a verificar

        Retorno:
            int: suma del valos de las casilla adyacentes
    """
    global matriz_laberinto
    return matriz_laberinto[x_parametro][y_parametro + 1] \
           + matriz_laberinto[x_parametro][y_parametro - 1] \
           + matriz_laberinto[x_parametro + 1][y_parametro] \
           + matriz_laberinto[x_parametro - 1][y_parametro]


def sellar_camino_cerrado():
    """Tapa con unos (1) los caminos cerrados

        Función:
            simplificar el laberinto para evitar avanzar por
            caminos sin salida

        Modifica:
            matriz_laberintos: cambia el valor de las celdas que son camino cerrado

            cantidad_de_ceros: la cantidad de ceros se actualiza, pues se disminuye

    """
    global matriz_laberinto, cantidad_de_ceros
    i = 0
    while i <= cantidad_de_ceros:
        for x4 in range(1, 11):
            for y in range(1, 11):
                if es_camino_cerrado(x4, y):
                    matriz_laberinto[x4][y] = 1
        i += 1


def avanzar():
    """Avanza de una casilla a una subsiguiente

        Función:
            avanzar aleatoriamente por la matriz actualizando las coordenadas
            y comprobando que casillas estan disponibles para el avance

        Modifica:
            x_actual: le resta o suma (1)

            y_actual: le resta o suma (1)

    """

    global x_actual, y_actual
    camino_seguido.append((x_actual, y_actual))
    numero_random = random.randint(1, 4)
    # derecha
    if camino_disponible(0, 1) and numero_random == 1:
        x_actual = x_actual
        y_actual = y_actual + 1
    # abajo
    elif camino_disponible(1, 0) and numero_random == 2:
        y_actual = y_actual
        x_actual = x_actual + 1
    # izquierda
    elif camino_disponible(0, -1) and numero_random == 3:
        x_actual = x_actual
        y_actual = y_actual - 1
    # arriba
    elif camino_disponible(-1, 0) and numero_random == 4:
        y_actual = y_actual
        x_actual = x_actual - 1
    else:
        if camino_disponible(0, 1):
            x_actual = x_actual
            y_actual = y_actual + 1
        elif camino_disponible(1, 0):
            y_actual = y_actual
            x_actual = x_actual + 1
        elif camino_disponible(0, -1):
            x_actual = x_actual
            y_actual = y_actual - 1
        elif camino_disponible(-1, 0):
            y_actual = y_actual
            x_actual = x_actual - 1


def camino_disponible(x_parametro, y_parametro):
    """Controla por cuales casillas adyacentes se puede avanzar

        Función:
            servir como método de apoyo para las toma de decisiones en avanzar()

        Argumentos:
            x_parametro (int): valor a sumar en la coordenada x

            y_parametro (int): valor a sumar en la cordenada y

        Retorno:
            Bool: True si es posible avanzar por esa casilla, False de lo contrario

    """
    global matriz_laberinto, x_actual, y_actual
    return matriz_laberinto[x_actual + x_parametro][y_actual + y_parametro] == 0


# Este método se crea debido a que las pilas de python no lo implementan
def peek(stack):
    """Permite visualizar el último elemento añadido a la lista sin eliminarlo

        Argumentos:
            stack: lista[]

        Retorno:
            var: variable dependiente de lo que se almacene en la lista
    """
    if stack == []:
        return None
    else:
        copia = stack.copy()
        return copia.pop()


def eliminar_caminos_repetidos():
    global caminos_exitosos
    caminos_exitosos = sorted(set(caminos_exitosos), key=lambda k: caminos_exitosos.index(k))


def mostrar_soluciones():
    if len(caminos_exitosos) == 0:
        print("Este laberinto no tiene solución")
    else:
        copia = caminos_exitosos.copy()
        print("Hubo " + str(len(caminos_exitosos)) + " soluciones distintas para este laberinto")
        print("ingrese el número de la que desea ver, ingrese XXX para ver la mejor, ingrese WWWW" \
              + " para verlas todas")
        eleccion = int(input())
        for x in range(eleccion - 1):
            copia.pop
        print(copia.pop())


# A PARTIR DE AQUÍ EJECUCIÓN DEL PROGRAMA
cargar_laberinto()

for x in range(500000):
    avanzar()
    w = camino_seguido.copy()
    w.pop()
    if (x_actual, y_actual) in w:
        x_actual = x_inicial
        y_actual = y_inicial
        camino_seguido.clear()

    if (x_actual == x_final) and (y_actual == y_final):
        camino_seguido.append((x_actual, y_actual))
        s = camino_seguido.copy()
        caminos_exitosos.append(str([camino_seguido]))
        camino_seguido.clear()
        x_actual = x_inicial
        y_actual = y_inicial

eliminar_caminos_repetidos()
#mostrar_soluciones()


for element in caminos_exitosos:
    print(element)

# DEBUG PRINTS
# print(len(caminos_exitosos))
# print(caminosExitosos.pop())
# print(len(caminosExitosos))
# print(cantidadDeCeros)

