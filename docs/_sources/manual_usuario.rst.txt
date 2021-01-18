Manual de usuario
=================

Formato laberintos:
-------------------

+-------------+
|111111111111 |
|             |
|101111111111 |
|             |
|101110000011 |
|             |
|101110111011 |
|             |
|100000111011 |
|             |
|111111111001 |
|             |
|111111111111 |
+-------------+

Los laberintos son cargados por medio de un archivo texto y tienen el siguiente formato:
* El archivo debe de contener los caracteres ‘0’ y ‘1’ y ningún otro más, estos representan caminos y paredes respectivamente.
* No hay espacios entre los caracteres.
* La totalidad de los caracteres deben de formar un rectángulo de tamaño m*n.
* La posición inicial se encontrará en las coordenadas (2,2) y la final en (m – 1, n – 1).
* La totalidad del borde del rectángulo está conformado por ‘1’s.

Además, el archivo texto conteniendo el laberinto deberá almacenarse en la carpeta laberintos/ con el nombre laberinto1.txt

Menú del juego:
^^^^^^^^^^^^^^^

Al ejecutar la aplicación se encontrará con un mensaje de bienvenida, la representación del laberinto y el siguiente menú de opciones:

1. Mostrar número de soluciones: Al seleccionar esta opción, se mostrará en pantalla la1 cantidad de soluciones que tiene el laberinto ingresado.

2. Mostrar todas las soluciones: Al seleccionar esta opción se mostrará en pantalla una serie de listas cada una representando una solución, estas listas además estarán ordenadas por tamaño, es decir, por el número de pasos realizados dentro del laberinto.

3. Mostrar n-ésima solución: Al seleccionar esta opción, deberá ingresar el número de la solución que quiera ver (recuerde que las soluciones están ordenadas por tamaño) si se ingresa un número mayor a la cantidad de soluciones, la aplicación mostrará un mensaje de error y podrá volver a intentarlo.

4. Salir: Al seleccionar esta opción se cerrará la aplicación.



