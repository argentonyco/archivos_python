#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

import csv
from fileinput import close
import re


def ej1():
    # Ejercicios con archivos txt
    cantidad_lineas = 0

    '''
    Realizar un prorgrama que cuenta la cantidad de líneas
    de un archivo. Abra el archivo "notas.txt" en modo "lectura",
    lea linea a linea el archivo, y cuente la cantidad de líneas.
    Al finalizar el proceso, imprimir en pantalla la cantidad
    de líneas leaidas.

    Como práctica de funciones, puede realizar la función
    "contar_lineas" que reciba como parámetro el nombre del archivo
    y cumpla el objetivo especificado, retornando la cantidad
    de líneas encontradas.
    '''
    #fi = open('notas.txt', 'r')
    #fi = close()

    with open('notas.txt', 'r') as fi:
        for line in fi:
            cantidad_lineas += 1
            #print('Linea leidas:', line, end='')       
    
        print(f'Linea leidas primer ejemplo: {cantidad_lineas}')

def contar_lineas(archivo):
    cantidad_lineas = 0

    with open(archivo, 'r') as fi:
        for i in fi:
            cantidad_lineas += 1

        return cantidad_lineas


def ej2():
    # Ejercicios con archivos txt
    cantidad_lineas = 0
    '''
    Copy paste!!
    Deberá abrir dos archivo txt, uno para lectura (fi) y otro
    para escritura (fo) (un archivo nuevo).
    El archivo abierto para lectura (fi) debe ser el archivo
    "notas.txt"

    Debe leer "línea por línea" el archivo "nota.txt" y copiar
    "línea a línea" en el archivo para escritura (write)

    A su vez, mientras va escribiendo "línea a línea" debe
    contar la cantidad de línea que se copiaron e imprimir
    al final del proceso el valor.
    '''
    fo = open('Clon notas.txt', 'w')

    with open('notas.txt', 'r') as fi:
        for line in fi:
            copiar_linea = line
            pegar_linea(copiar_linea, fo)
            cantidad_lineas += 1
            

    # Recuerde cerrar los archivos al final ;)
    print(f'Se copiaron: {cantidad_lineas} lineas')
    fo.flush()
    fo.close()
    fi.close()

def pegar_linea(pegar_copiado, fo):
    fo.write(pegar_copiado)
    
def ej3():
    print("Cuenta caracteres")
    cantidad_letras = 0

    '''
    Realizar un prorgrama que cuenta la cantidad de caracteres
    (todo tipo de caracter, los espacios cuentan) de un archivo.
    Abra el archivo "text.txt" en modo "lectura", lea linea a
    linea el archivo, y cuente la cantidad de caracteres de cada línea.
    Debe realizar la sumatoria total de la cantidad de caracteres de todas
    las líneas para obtener el total del archivo e imprimirlo en pantalla
    '''
    fi = open('texto.txt', 'r')
    for line in fi:
        cantidad_letras += len(line)
        
    print(cantidad_letras)

def ej4():
    print("Transcribir!")
    cantidad_letras = 0
    '''
    Deberá abrir un archivo txt para escritura (un archivo nuevo)
    Luego mediante un bucle deberá pedir por consola que
    se ingrese texto. Todo el texto ingresado por consola
    debe escribirse en el archivo txt, cada entrada de texto
    deberá ser una línea en el archivo.
    El programa termina cuando por consola no se ingresa
    nada (texto vacio). En ese momento se termina el bucle
    y se cierra el archivo.
    Durante la realización del bucle y el ingreso de texto por
    consola, se debe ir contanto cuandos caracteres se ingresaron
    por consola, al fin de al terminar el bucle saber cuantos
    caracteres se copiaron al archivo.
    NOTA: Recuerde agregar el salto de línea "\n" a cada entrada
    de texto de la consola antes de copiar la archivo.
    '''
    fo = open('archivo_txt', 'a')

    texto_archivo = ''
    while texto_archivo == '':
        texto_archivo = input('Esperando texto:\n')
        
        if texto_archivo == '':
            print(f'Se copiaron {cantidad_letras} caracteres\n')
            break
        else:
            fo.write(f'{texto_archivo}\n')
            cantidad_letras += len(texto_archivo)

            texto_archivo = ''
        
    fo.flush()
    fo.close()

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #print('Cantidad de lineas leidas:', contar_lineas('texto.txt'))    
    #ej2()
    #ej3()
    ej4()
