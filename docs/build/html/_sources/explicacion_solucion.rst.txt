Explicación de la solución
==========================

El código que soluciona el laberinto se encuentra en Practica2/codigo/main.py .
Este código lee un archivo .txt que contiene un rectangulo o cuadrado (todas las lineas
deben tener la misma longitud) formado de ceros (0) y unos (1) como el que se puede observar a continuación:

+--------+
|1111111 |
|        |
|1011111 |
|        |
|1011111 |
|        |
|1011111 |
|        |
|1011111 |
|        |
|1000001 |
|        |
|1111111 |
+--------+

En donde  los ceros representan que se puede avanzar por esa celda, mientras que los unos
representan una pared. Es muy importante que el laberinto tenga una "pared externa" es decir,que
**todos sus bordes esten conformados por unos**, esto con el fin de evitar errores del tipo
indice por fuera de los limites durante la ejecución.


Variables
^^^^^^^^^

Las variables usadas en el proyecto son las siguientes:

+-----------------+------------+-------------------------------+
| Nombre          |    Tipo    |          Explicación          |
+=================+============+===============================+
| x_inicial       |    int     | Coordenada en x desde         |
|                 |            |                               |
|                 |            | donde se parte                |
+-----------------+------------+-------------------------------+
| y_inicial       |    int     | Coordenada  en y desde        |
|                 |            |                               |
|                 |            | donde se parte                |
+-----------------+------------+-------------------------------+
| x_final         |    int     | Coordenada en x a donde se    |
|                 |            |                               |
|                 |            | quiere llegar                 |
+-----------------+------------+-------------------------------+
| y_final         |    int     | Coordenada en y a donde se    |
|                 |            |                               |
|                 |            | quiere llegar                 |
+-----------------+------------+-------------------------------+
| x_actual        |    int     | Coordenada x en la cima de la |
|                 |            |                               |
|                 |            | pila camino_seguido           |
+-----------------+------------+-------------------------------+
| y_actual        |    int     | Coordenada y en la cima de la |
|                 |            |                               |
|                 |            | pila camino_seguido           |
+-----------------+------------+-------------------------------+
| filas           |    int     | Filas que contiene el .txt    |
|                 |            |                               |
|                 |            | que contiene el laberinto     |
+-----------------+------------+-------------------------------+
| columnas        |     int    | Columnas que contiene el .txt |
|                 |            |                               |
|                 |            | que contiene el laberinto     |
+-----------------+------------+-------------------------------+
| matriz_laberinto|  int[][]   | Laberinto leido convertido    |
|                 |            |                               |
|                 |            | en una matriz                 |
+-----------------+------------+-------------------------------+
| camino_seguido  | stack      | Contiene los pares  x y y de  |
|                 |            |                               |
|                 |            | coordenadas seguidos para     |
|                 |            |                               |
|                 |            | Llegar hasta las coordenadas  |
|                 |            |                               |
|                 |            | actuales                      |
+-----------------+------------+-------------------------------+
| caminos_exitosos| stack      | Contiene las pilas de caminos |
|                 |            |                               |
|                 |            | que llevan hasta el final     |
+-----------------+------------+-------------------------------+
| bifurcaciones   | stack      | Contiene las coordenadas de   |
|                 |            |                               |
|                 |            | celdas que son bifurcaciones  |
+-----------------+------------+-------------------------------+

Funcionamiento resumido
=======================

Carga del laberinto
^^^^^^^^^^^^^^^^^^^
El laberinto se carga de el .txt a la matriz_laberinto, por defecto y comodidad el inicio siempre estara en la posición
(1,1) y el final en la posicion (filas-1, columnas-1)  (hay que tener en cuenta que se empieza a contar desde cero).
En el siguiente laberinto X representa el inicio y F el final, se puede observar que sus cordenadas son (1,1) y
(3,3) respectivamente.

+--------+
|1111111 |
|        |
|1X11111 |
|        |
|1011111 |
|        |
|1011111 |
|        |
|1011111 |
|        |
|10000F1 |
|        |
|1111111 |
+--------+

Una vez se ha cargado el laberinto se procede a simplificarlo, esto es eliminar los callejones sin salida, despues de simplificar
el laberinto de la izquierda quedaria como el que se encuentra al lado derecho

+--------+--------+
|1111111 |1111111 |
|        |        |
|1X11111 |1X11111 |
|        |        |
|1011101 |1011111 |
|        |        |
|1000001 |1011111 |
|        |        |
|1011111 |1011111 |
|        |        |
|1000001 |1000001 |
|        |        |
|1111111 |1111111 |
+--------+--------+



Avance
^^^^^^
Cada que se va a avanzar de una casilla a otra se realizan varias
comprobaciones, entre ellas estan:

* Si la casilla esta disponible para el avance, es decir si su valor es 0

* Si en la casilla ya se habia estado con anterioridad: en caso afirmativo la pila camino_seguido se desapila hasta regresar a la última bifurcacion e intentar avanzar por el otro camino que no se había seguido inicialmente.

* Si la casilla actual es una bifurcación: en caso afirmativo se almacena en la pila de bifurcaciones.

* Si la casilla actual es el final: en caso afirmativo se almacena camino_seguido en la pila caminos_exitosos y se borra el contenido de camino_seguido para volver a empezar e intentar hallar otro camino.

Finalización
^^^^^^^^^^^^
Después de haberse ejecutado determinado número de veces el programa se detiene, elimina los caminos_exitosos duplicados, los ordena
y dispone una interfaz para interactuar con el usuario

Uso de pilas
^^^^^^^^^^^^
En python usar pilas es equivalente a usar listas con los siguientes métodos:

+--------------+-------------------------+
|nombre método |implementación en python |
+==============+=========================+
| apilar       |pila.append()            |
+--------------+-------------------------+
| desapilar    | pila.pop()              |
+--------------+-------------------------+
| cima         | píla[-1]                |
+--------------+-------------------------+
| esVacia      | len(pila)==0            |
+--------------+-------------------------+





