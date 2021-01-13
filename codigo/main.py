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
filas = -1
columnas = -1


def cargar_laberinto():
    """Almacena el laberinto en una matriz

    Función:
        Leer las lineas del archivo seleccionado (ver sección  "Jerarquia
        de archivos") para conformar las filas de la matriz y colummnas de la
        matriz

    Modifica:
        matriz_laberinto: le agrega los unos y ceros que conforman el laberinto

    """
    global matriz_laberinto, cantidad_de_ceros, filas, columnas
    archivo = open("../laberintos/laberinto1.txt")
    archivo_completo = archivo.readlines()
    matriz_laberinto = []
    linea = []
    columnas = len(archivo.readline())
    for renglon in archivo_completo:
        for char in renglon:
            if char in "10":
                linea.append(int(char))
        matriz_laberinto.append(linea)
        linea = []
    filas = len(archivo_completo)
    sellar_camino_cerrado()


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
    global matriz_laberinto, cantidad_de_ceros, filas, columnas
    for _ in range(filas + columnas):
        for x4 in range(1, filas):
            for y in range(1, columnas):
                if es_camino_cerrado(x4, y):
                    matriz_laberinto[x4][y] = 1


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
    var = [0, 1, 2, 3]
    flag = False
    while not flag:
        numero_random = random.randint(0, 3)   #2
        # derecha
        if camino_disponible(0, 1) and var[numero_random] == 0:
            x_actual = x_actual
            y_actual = y_actual + 1
            flag = True
        # abajo
        elif camino_disponible(1, 0) and var[numero_random] == 1:
            y_actual = y_actual
            x_actual = x_actual + 1
            flag = True
        # izquierda
        elif camino_disponible(0, -1) and var[numero_random] == 2:
            x_actual = x_actual
            y_actual = y_actual - 1
            flag = True
        # arriba
        elif camino_disponible(-1, 0) and var[numero_random] == 3:
            y_actual = y_actual
            x_actual = x_actual - 1
            flag = True



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
    aux, aux1 = camino_seguido.pop()
    if (aux, aux1) in camino_seguido:
        x_actual = x_inicial
        y_actual = y_inicial
        camino_seguido.clear()
    else:
        camino_seguido.append((aux, aux1))

    if (x_actual == x_final) and (y_actual == y_final):
        camino_seguido.append((x_actual, y_actual))
        caminos_exitosos.append(str([camino_seguido]))
        camino_seguido.clear()
        x_actual = x_inicial
        y_actual = y_inicial

eliminar_caminos_repetidos()
# mostrar_soluciones()


for element in caminos_exitosos:
    print(element)

# DEBUG PRINTS
# print(len(caminos_exitosos))
# print(caminosExitosos.pop())
# print(len(caminosExitosos))
# print(cantidadDeCeros)
