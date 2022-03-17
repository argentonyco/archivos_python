#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

import csv
from multiprocessing.spawn import spawn_main
# from itertools import count

def ironman(categoria, disciplina):

    '''
    Para poder realizar este ejercicio deberán descargarse el
    dataset "2019 Ironman world championship results" del siguiente
    link:
    https://www.kaggle.com/andyesi/2019-ironman-world-championship-results/data#

    Una vez tengan descargado el archivo CSV lo pueden observar un poco.
    En principio le daremos importancia a las siguientes columnas:

    Division: Esta columna marca la divisón del corredor por experiencia o edad.
    Swim: Tiempo nadando
    Bike: Tiempo en bicicleta
    Run: Tiempo corriendo

    Queremos investigar las siguientes divisiones o categorias:
    - MPRO
    - M45-49
    - M25-29
    - M18-24

    De cada una de estas categorías de corredores deseamos que analices
    por separado el tiempo de Swim, Bike y Run. En cada caso (para los 3)
    se desea obtener
    1) El tiempo máximo realizado por un corredor en dicha categoria
    2) El tiempo mínimo realizado por un corredor en dicha categoria
    3) El tiempo promedio de dicha categoria

    Es decir, por ejemplo voy a investigar la categoria M45-49 en "Run"
    - Debo buscar de todos los M45-49 cual fue el mayor tiempo en Run
    - Debo buscar de todos los M45-49 cual fue el menor tiempo en Run
    - Debo buscar de todos los M45-49 el tiempo Run y calcular el promedio

    Para poder realizar este ejercicio necesitará muchas variables para almacenar
    los datos, puede organizarse como mejor prefiera, en listas, con diccionarios,
    lo que se sienta más comodo.

    Es valido recorrer todo el archivo para extrer la información ordenada
    y almacenarlas en listas según el criterio que escojan.

    NOTA:
    Recomendamos empezar de a poco, los primeros ensayos realizarlo
    con una sola categoría de edad en solo una sección (Bike, Run, Swim)
    de la carrera. Sería igual al ej4 la información recolectada y calculada.

    NOTA IMPORTANTE:
    En este ejercicio se pide calcular el promedio, el máximo y mínimo tiempo
    que realizaron los corredores en distintas etapas de la carrera.
    La dificultad radica en que el dato que el archivo nos provee está
    en el siguiente formado:

    hora:minutos:segundos, 0:47:27 --> (0 horas, 47 minutos, 27 segundos).

    No pueden utilizar este valor para calcular el promedio, el máximo
    y mínimo ya que está en formato texto, no está en formato numérico.
    Para poder realizar cálculos matemáticos sobre este dato deben primero
    llevarlo a un formato que les permita realizar cálculos.

    Normalmente en estos casos lo que se realiza es llevar este dato
    0:47:27 a segundos, es decir, calcular cuantos segundos le llevó
    al corredor completar esa etapa, ya que segundos es la unidad mínima
    presentada (horas, minutos, segundos).

    Para poder calcular la cantidad de segundos totales deberían operar
    de la siguiente forma:

    segundos_totales = horas * 3600 + minutos * 60 + segundos

    De esta forma están pasando de un formato texto horas:minutos:segundos a
    un número "segundos_totales" el cual pueden calcular
    promedio, máximo y mínimo
    
    Queda en sus manos pensar como extraer las "horas" "minutos" y "segundos"
    del formato "horas:minutos:segundos", 
    pueden realizar operaciones de texto ahí, o usar algún módulo externo
    de Python que resuelva este problema.

    '''

    archivo = '2019 Ironman World Championship Results.csv'

    with open(archivo) as csvfile:
        ironman = list(csv.DictReader(csvfile))

    lista_tiempos = []

    for row in ironman:
        _categoria = row['Division']
        if _categoria == categoria:
            tiempo_lista = row[disciplina]
            tiempo_segundos = conversion_tiempos(tiempo_lista)
            if tiempo_segundos == 0:
                continue
            else:
                lista_tiempos.append(tiempo_segundos)
        else:
            continue

    max_tiempo, min_tiempo, cantidad_tiempos = max_min_cantidad(lista_tiempos)

    promedio_tiempos = tiempo_promedio(lista_tiempos, cantidad_tiempos)

    print(f'El tiempo maximo en la categoria {categoria} fue de {segundos_a_segundos_minutos_y_horas(max_tiempo)} en la disciplina {disciplina}\n') 
    print(f'El tiempo minimo en la categoria {categoria} fue de {segundos_a_segundos_minutos_y_horas(min_tiempo)} en la disciplina {disciplina}\n') 
    print(f'El tiempo promedio de la categoria {categoria} fue de {segundos_a_segundos_minutos_y_horas(promedio_tiempos)} en la disciplina {disciplina}')
    
    
    
def max_min_cantidad(lista_tiempos):
    max_tiempo = max(lista_tiempos)
    min_tiempo = min(lista_tiempos)
    cantidad_tiempos = len(lista_tiempos)
    return max_tiempo, min_tiempo, cantidad_tiempos

def tiempo_promedio(lista_tiempos, cantidad_tiempos):
    promedio_tiempos = sum(lista_tiempos) // cantidad_tiempos
    return promedio_tiempos

def conversion_tiempos(tiempo):
    operacion_tiempo = tiempo

    '''Excepcion para los datos vacios'''
    if operacion_tiempo == '':
        operacion_tiempo = '00:00:00'

    h, m, s = operacion_tiempo.strip().split(':')
    tiempo_segundos = int(h)*3600 + int(m)*60 + int(s)
    return tiempo_segundos

def segundos_a_segundos_minutos_y_horas(segundos):
    horas = int(segundos / 60 / 60)
    segundos -= horas*60*60
    minutos = int(segundos/60)
    segundos -= minutos*60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"




if __name__ == '__main__':
    print("Ejercicios de práctica extra\n")

    print("""Elija la categoria y disciplina para investigar los resultados de los tiempos\n\n1 - MPRO
2 - M45-49
3 - M25-29
4 - M18-24\n""")
    user_categoria = input('Elija la categoria:\n')
    if user_categoria == '1':
        user_categoria = 'MPRO'
    elif user_categoria == '2':
        user_categoria = 'M45-49'
    elif user_categoria == '3':
        user_categoria = 'M25-29'
    elif user_categoria == '4':
        user_categoria = 'M18-24'
    
    print('''Elija la disciplina\n\n1 - Bike
2 - Swim
3 - Run\n''')

    user_disciplina = input('Elija la disciplina\n')

    if user_disciplina == '1':
        user_disciplina = 'Bike'
        input('Vamos por la disciplina Bike')
    elif user_disciplina == '2':
        user_disciplina = 'Swim'
        input('Vamos por la disciplina Swim')

    elif user_disciplina == '3':
        user_disciplina = 'Run'
        input('Vamos por la disciplina Run')


    ironman(user_categoria, user_disciplina)
