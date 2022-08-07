
import numpy as np

n = 3 
while n%2 != 0:
    try:
        print("Ingrese un número impar: ")
        n = int(input())

        cuadro = np.zeros((n,n), dtype=int)
        mitad = n // 2
        fila = 0
        columna = mitad 
        i = 0
        j = 0
        a = 1
        while a != (n*n)+1:
            if cuadro[fila][columna]==0:
                cuadro[fila][columna]= a
            else: 
                fila = i + 1
                columna = j
                cuadro[fila][columna]= a
            
            i = fila
            j = columna
            a = a + 1
            fila = fila - 1
            columna = columna + 1

            if fila < 0 and columna==n:
                fila = n - 1
                columna = 0
            elif fila < 0:
                fila = n-1
            elif columna == n:
                columna = 0
        
        print(cuadro)
        break


    except:
        print("El número que ingreso no es primo....Por favor ingrese un número impar: ")
        n = 3
