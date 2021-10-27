'''
Proyecto de trabajo con csv

'''

import csv
from collections import namedtuple

'''

Bloque 1: Lectura de los ficheros y devolución de los datos del archivo pokemon.csv

'''

def lee_pokemon(fichero):

    pokemon = []
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter = ",")
        next(lector)
        for linea in f:
            num_pokedex, name, type1, type2, hp, attack, defense, spattack, spdefense, speed, generation, legendary, date = linea.split(',')
            
            num_pokedex = int(num_pokedex)
            hp = int(hp)
            attack = int(attack)
            defense = int(defense)
            spattack = int(spattack)
            spdefense = int(spdefense)
            speed = int(speed)
            generation = int(generation)
            legendary = bool(legendary)

            tupla = (num_pokedex, name, type1, type2, hp, attack, defense, spattack, spdefense, speed, generation, legendary, date)
            pokemon.append(tupla)
    
    return pokemon

'''

Bloque 2: 

1. Filtrar la lista con los registros por alguno/s de los campos (que se cumpla determinada condición)

    En este caso se filtrará por los campos Type 1 y Type 2 que definen el tipo del pokemon

'''

def filtra_tipos(fichero, tipo):
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter = ",")
        next(lector)
        filtro  = []
        for linea in f:
            num_pokedex, name, type1, type2, hp, attack, defense, spattack, spdefense, speed, generation, legendary, date = linea.split(',')
            if type1 == tipo or type2 == tipo:
                filtro.append(name)

    return filtro

'''

2. Obtener un conjunto con alguno de los campos.

    Se filtrará el csv por alguno de sus campos, en este caso el campo Name
'''
'''
def lista_campos(fichero, campo):
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=",")
        next(lector)
        campos = []
        for linea in f:
            num_pokedex, name, type1, type2, hp, attack, defense, spattack, spdefense, speed, generation, legendary, date = linea.split(',')
            valor = str(campo)
            if valor in campos:
'''
