![Python Logo](./readme_img/python.png)

# Introducción a la Complejidad Algorítmica

Este documento proporciona una introducción a la complejidad algorítmica, basada en el curso de [David Aroesti](https://github.com/jdaroesti) en [Platzi](https://platzi.com). La complejidad algorítmica es una medida de cuánto tiempo o espacio consume un algoritmo en función del tamaño de su entrada.

## Tipos de Complejidad Algorítmica

- **O(1) Constante**: Independientemente del tamaño de la entrada, el tiempo de ejecución del algoritmo es constante.

- **O(n) Lineal**: El tiempo de ejecución del algoritmo aumenta linealmente con el tamaño de la entrada.

- **O(log n) Logarítmica**: El tiempo de ejecución del algoritmo aumenta logarítmicamente con el tamaño de la entrada. Esto significa que el tiempo de ejecución aumenta rápidamente al principio y luego se estabiliza.

- **O(n log n) Log lineal**: El tiempo de ejecución del algoritmo aumenta de forma logarítmica, pero se multiplica por una constante.

- **O(n²) Polinomial**: El tiempo de ejecución del algoritmo aumenta cuadráticamente con el tamaño de la entrada. Los algoritmos con esta complejidad deben evitarse a menos que el tamaño de la entrada sea pequeño.

- **O(2^n) Exponencial**: El tiempo de ejecución del algoritmo aumenta exponencialmente con el tamaño de la entrada. Estos algoritmos tienen una carga muy alta y deben evitarse en la mayoría de los casos.

- **O(n!) Factorial**: El tiempo de ejecución del algoritmo aumenta factorialmente con el tamaño de la entrada. Al igual que los algoritmos exponenciales, estos algoritmos tienen una carga muy alta y deben evitarse.

![Big O Complexity](./readme_img/big_o.jpg)

# Búsqueda Lineal

Este script realiza una búsqueda lineal en una lista de números aleatorios.

## Requisitos

- Python 3

## Ejecución

Para ejecutar este script, sigue estos pasos:

1. Abre una terminal.

2. Navega a la carpeta `scripts` donde se encuentra el script `busqueda_lineal.py`. Puedes hacerlo con el comando `cd`, por ejemplo:

    ```bash
    cd ruta/a/la/carpeta/scripts
    ```

3. Ejecuta el script con Python:

    ```bash
    python3 busqueda_lineal.py
    ```

4. El script te pedirá que introduzcas el tamaño de la lista y el número que quieres encontrar. Introduce estos valores cuando se te solicite.

El script generará una lista de números aleatorios del tamaño que hayas especificado, realizará una búsqueda lineal para encontrar el número que has introducido, e imprimirá la lista y el resultado de la búsqueda.