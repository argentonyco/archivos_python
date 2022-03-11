# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    
    # Abrir un archivo CSV
    csvfile = open(archivo, 'r')
    # Leer todos los datos y almacenarlos en una 
    # lista de diccionarios
    stock = list(csv.DictReader(csvfile))

    suma_producto = 0

    for producto in stock:
        cantidad_total = int(producto['tornillos'])
        suma_producto += cantidad_total
        
    print(f'En el stock hay {suma_producto} de tornillos\n')

    csvfile.close()    


def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    csvfile = open(archivo, 'r')

    propiedades = list(csv.DictReader(csvfile))

    cant_2_amb = 0
    cant_3_amb = 0
    sin_ambiente = 0
    for dpto in propiedades:
        cant_amb = dpto['ambientes']
        if cant_amb == '2':
            cant_2_amb += 1
        elif cant_amb == '3':
            cant_3_amb += 1
        else:
            cant_amb = ''
            sin_ambiente += 1

    print(f'Hay disponibles {cant_2_amb} propiedades de 2 ambientes y {cant_3_amb} propiedades de 3 ambientes')
    print(f'{sin_ambiente} no definidos')

        # suma_producto += cantidad_total

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
