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
    """Almacena el laberinto en una matriz

    Función:
        Leer las lineas del archivo seleccionado (ver sección  "Jerarquia
        de archivos") para conformar las filas de la matriz y colummnas de la
        matriz

    Modifica:
        matriz_laberinto: le agrega los unos y ceros que conforman el laberinto

    """
    global matriz_laberinto, filas, columnas
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
    return (matriz_laberinto[x_parametro][y_parametro + 1] +
            matriz_laberinto[x_parametro][y_parametro - 1] +
            matriz_laberinto[x_parametro + 1][y_parametro] +
            matriz_laberinto[x_parametro - 1][y_parametro])


def sellar_camino_cerrado():
    """Tapa con unos (1) los caminos cerrados

        Función:
            simplificar el laberinto para evitar avanzar por
            caminos sin salida

        Modifica:
            matriz_laberintos: cambia el valor de las celdas que son camino cerrado

    """
    global matriz_laberinto, filas, columnas
    print(filas)
    print(columnas)
    for w in range(filas + columnas):
        for x4 in range(0, filas - 1):
            for y in range(0, columnas - 1):
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

    global x_actual, y_actual, camino_seguido
    camino_seguido.append((x_actual, y_actual, es_bifurcacion()))
    bifurcaciones.append(es_bifurcacion())
    numero_random = random.randint(1, 4)
    flag = True
    i = 0
    while flag:
        # derecha
        if camino_disponible(0, 1) and (numero_random % 4) == 1:
            x_actual = x_actual
            y_actual = y_actual + 1
            flag = False
        # abajo
        elif camino_disponible(1, 0) and (numero_random % 4) == 2:
            y_actual = y_actual
            x_actual = x_actual + 1
            flag = False
        # izquierda
        elif camino_disponible(0, -1) and (numero_random % 4) == 3:
            x_actual = x_actual
            y_actual = y_actual - 1
            flag = False
        # arriba
        elif camino_disponible(-1, 0) and (numero_random % 4) == 9:
            y_actual = y_actual
            x_actual = x_actual - 1
            flag = False
        else:
            numero_random += 1
        i += 1
    no_repetir()
    add_a_finales()


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


def es_bifurcacion():
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
        for x in range(eleccion - 1):
            copia.pop
        print(copia.pop())


def no_repetir():
    global x_actual, y_actual, camino_seguido, bifurcaciones
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
    global x_actual, y_actual, camino_seguido, caminos_exitosos
    if (x_actual == x_final) and (y_actual == y_final):
        camino_seguido.append((x_actual, y_actual))
        caminos_exitosos.append(str([camino_seguido]))
        camino_seguido.clear()
        bifurcaciones.clear()
        x_actual = x_inicial
        y_actual = y_inicial


def cantidad_de_ceros_superada():
    2 + 2


# A PARTIR DE AQUÍ EJECUCIÓN DEL PROGRAMA
cargar_laberinto()
for element in matriz_laberinto:
    print(element)

for x in range(500000):
    avanzar()

print(len(caminos_exitosos))
eliminar_caminos_repetidos()
print(len(caminos_exitosos))
# mostrar_soluciones()

# for element in caminos_exitosos:
#    print(element)
