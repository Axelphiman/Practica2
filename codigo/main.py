import random

x_inicial = 1
y_inicial = 1
x_final = 10
y_final = 10
x_actual = x_inicial
y_actual = y_inicial
matriz_laberinto = []
camino_seguido = []
caminos_exitosos = []
bifurcaciones = []
filas = -1
columnas = -1


def cargar_laberinto():
    """Almacena el laberinto en una matriz.

    :Función:
        Leer las lineas del archivo seleccionado (ver sección  "Jerarquia
        de archivos") para conformar las filas de la matriz y colummnas de la
        matriz.

    :Modifica:
        matriz_laberinto: le agrega los unos y ceros que conforman el laberinto.

    """
    global matriz_laberinto, filas, columnas, x_final, y_final
    archivo = open("../laberintos/laberinto1.txt")
    archivo_completo = archivo.readlines()
    matriz_laberinto = []
    linea = []
    columnas = len(archivo_completo)

    for renglon in archivo_completo:
        for char in renglon:
            if char in "10":
                linea.append(int(char))
        matriz_laberinto.append(linea)
        linea = []
    filas = len(archivo_completo)
    sellar_camino_cerrado()
    x_final = filas - 2
    y_final = columnas - 2


def es_camino_cerrado(x_parametro: int, y_parametro: int) -> bool:
    """Compueba si una celda es o no un camino sin salida.

    :Función:
        Servir como método de control para apoyar las
        decisiones tomadas en otros métodos.

    Args:
        x_parametro (int): coordenada x de la casilla a verificar.
        y_parametro (int): coordenada y de la casilla a verificar.

    :Retorno:
        Bool: True en caso de que la casilla sea un camino sin salida, falso
        de lo contrario.

    """
    global matriz_laberinto, x_inicial, y_inicial, x_final, y_final
    # Notar que una celda es un camino sin salida si la suma del valor de
    # las celdas adyacentes es mayor o igual a 3
    if (x_parametro == x_inicial and y_parametro == y_inicial) \
            or (x_parametro == x_final and y_parametro == y_final):
        return False
    else:
        return suma_adyacentes(x_parametro, y_parametro) >= 3


def suma_adyacentes(x_parametro: int, y_parametro: int) -> int:
    """Suma los valores de las casillas adyacentes.

        Función: método auxiliar para el funcionamiento de otros métodos que requieren
        comprobar el estado de una casilla.

        Args:
            x_parametro: coordenada x de la casilla a verificar.
            y_parametro: coordenada y de la casilla a verificar.

        Retorno:
            int: suma del valos de las casilla adyacentes.
    """
    global matriz_laberinto
    return (matriz_laberinto[x_parametro][y_parametro + 1] +
            matriz_laberinto[x_parametro][y_parametro - 1] +
            matriz_laberinto[x_parametro + 1][y_parametro] +
            matriz_laberinto[x_parametro - 1][y_parametro])


def sellar_camino_cerrado():
    """Tapa con unos (1) los caminos cerrados.

        :Función:
            simplificar el laberinto para evitar avanzar por
            caminos sin salida.

        :Modifica:
            matriz_laberintos: cambia el valor de las celdas que son parte
             de un camino cerrado.

    """
    global matriz_laberinto, filas, columnas
    for i in range(filas + columnas):
        for x4 in range(0, filas - 1):
            for y in range(0, columnas - 1):
                if es_camino_cerrado(x4, y):
                    matriz_laberinto[x4][y] = 1


def avanzar():
    """Avanza de una casilla a una subsiguiente.

        :Función:
            avanzar por la matriz actualizando las coordenadas actuales
            y comprobando que casillas estan disponibles para el avance.

        :Modifica:
            x_actual: le resta o suma uno (1).
            y_actual: le resta o suma uno (1).

    """
    global x_actual, y_actual, camino_seguido
    camino_seguido.append((x_actual, y_actual, es_bifurcacion()))
    bifurcaciones.append(es_bifurcacion())
    numero_random = random.randint(1, 4)
    flag = True
    while flag:
        # movimiento a la derecha
        if camino_disponible(0, 1) and (numero_random % 4) == 1:
            x_actual = x_actual
            y_actual = y_actual + 1
            flag = False
        # movimiento a abajo
        elif camino_disponible(1, 0) and (numero_random % 4) == 2:
            y_actual = y_actual
            x_actual = x_actual + 1
            flag = False
        # movimiento a la izquierda
        elif camino_disponible(0, -1) and (numero_random % 4) == 3:
            x_actual = x_actual
            y_actual = y_actual - 1
            flag = False
        # movimiento a arriba
        elif camino_disponible(-1, 0) and (numero_random % 4) == 9:
            y_actual = y_actual
            x_actual = x_actual - 1
            flag = False
        else:
            numero_random += 1
    no_repetir()
    add_a_finales()


def camino_disponible(x_parametro: int, y_parametro: int) -> bool:
    """Controla por cuales casillas adyacentes se puede avanzar.

        :Función:
            servir como método de apoyo para las toma de decisiones en avanzar().

        Args:
            x_parametro (int): valor a sumar en la coordenada x.
            y_parametro (int): valor a sumar en la cordenada y.

        :Retorno:
            Bool: True si es posible avanzar por esa casilla, False de lo contrario.

    """
    global matriz_laberinto, x_actual, y_actual
    return matriz_laberinto[x_actual + x_parametro][y_actual + y_parametro] == 0


def eliminar_caminos_repetidos():
    """Elimina soluciones al laberinto duplicadas.
    """
    global caminos_exitosos
    caminos_exitosos = sorted(set(caminos_exitosos), key=lambda k: caminos_exitosos.index(k))


def es_bifurcacion() -> bool:
    """Compueba si la celda actual es o no un camino una bifurcación del camino.

    :Función:
        Servir como método de control para apoyar las
        decisiones tomadas en otros métodos

    :Retorno:
        Bool: True en caso de que la casilla sea bifurcacion, falso
        de lo contrario.

    """
    if (x_actual == x_inicial) and (y_actual == y_inicial):
        return True
    return suma_adyacentes(x_actual, y_actual) < 2


def mostrar_soluciones():
    if len(caminos_exitosos) == 0:
        print("Este laberinto no tiene solución")
    else:
        copia = caminos_exitosos.copy()
        print("Hubo " + str(len(caminos_exitosos)) + " soluciones distintas para este laberinto")
        print("ingrese el número de la que desea ver, ingrese XXX para ver la mejor, ingrese WWWW"
              + " para verlas todas")
        eleccion = int(input())
        for i in range(eleccion - 1):
            copia.pop
        print(copia.pop())


def no_repetir() -> bool:
    """Evita que se pase dos veces por encima del mismo camino.

        :Función:
            verificar en la pila del camino seguido si ya se
            habia estado anteriormente en esa casilla.

        :Modifica:
            camino_seguido: le añade las coordenadas análizadas
            en caso de que sean totalmente nuevas.

        :Retorna:
            Bool: True si en las coordenadas ya se había
            visidado con anterioridad, False de lo contario.

    """
    global x_actual, y_actual, camino_seguido, bifurcaciones, matriz_laberinto
    aux, aux1, aux3 = camino_seguido.pop()
    if (aux, aux1, aux3) in camino_seguido or (aux, aux1, not aux3) in camino_seguido:
        a, b, c = camino_seguido.pop()
        while not c:
            a, b, c = camino_seguido.pop()
        x_actual, y_actual = a, b
        return True

    else:
        camino_seguido.append((aux, aux1, aux3))
        return False


def add_a_finales():
    """Almacena caminos a la pila de finales

        :Función:
            Si un camino logra partir desde el inicio y llegar hasta el final,
             este método lo almacena

        :Modifica:
            caminos_exitosos: le  añade un nuevo camino a la pila.

    """
    global x_actual, y_actual, camino_seguido, caminos_exitosos
    if (x_actual == x_final) and (y_actual == y_final):
        camino_seguido.append((x_actual, y_actual))
        caminos_exitosos.append(str([camino_seguido]))
        camino_seguido.clear()
        bifurcaciones.clear()
        x_actual = x_inicial
        y_actual = y_inicial


# A PARTIR DE AQUÍ EJECUCIÓN DEL PROGRAMA
cargar_laberinto()
for x in range(500000):
    avanzar()

eliminar_caminos_repetidos()
