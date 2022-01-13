
# Proyecto de trabajo con csv


import csv
from collections import namedtuple
from datetime import datetime


# Bloque 1: Lectura de los ficheros y devolución de los datos del archivo pokemon.csv


pokemon = namedtuple('pokemon', 'num_pokedex, name, type1, type2, hp, attack, defense, spattack, spdefense, speed, generation, legendary, date_pkm')

def lee_pokemon(fichero):

    pokemon_list = []
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter = ",")
        next(lector)
        for e in lector:

            num_pokedex = int(e[0])
            name = str(e[1])
            type1 = str(e[2])
            type2 = str(e[3])
            hp = int(e[4])
            attack = int(e[5])
            defense = int(e[6])
            spattack = int(e[7])
            spdefense = int(e[8])
            speed = int(e[9])
            generation = int(e[10])
            legendary = bool(e[11])
            date_pkm = datetime.strptime(e[12], "%d-%m-%y")

            
            pokemon_list.append(pokemon(num_pokedex, name, type1, type2, hp, attack, defense, spattack, spdefense, speed, generation, legendary, date_pkm))
    
    return pokemon_list


# Bloque 2: 

# 1. Filtrar la lista con los registros por alguno/s de los campos (que se cumpla determinada condición)

#     En este caso se filtrará por los campos Type 1 y Type 2 que definen el tipo del pokemon


def filtra_tipos(pokemon, tipo):
       filtro  = []
       for e in pokemon:
            if e.type1 == tipo or e.type2 == tipo:
                filtro.append(e.name)

       return filtro


# 2. Obtener un conjunto con alguno de los campos.

#     Se obtendrá del csv un conjunto de valores con los tipos de los pokemon 

def conjunto_campos(pokemon):
        conjunto = set()
        for e in pokemon:
            conjunto.add(e.type1)
            conjunto.add(e.type2)

        return conjunto

# Bloque 3

# 4. Calcular un valor como resultado de aplicar una función matemática a determinado campo de los registros 
# que cumplen una condición.

def media_valores(pokemon, valor):
    media_total = []
    for e in pokemon:
        media_total.append(e[valor])
    cantidad_pokemon = len(pokemon)
    suma = sum(media_total)
    media = suma / cantidad_pokemon
    media_redondeada = round(media, 0)
    return media_redondeada

def valores_sobre_media(pokemon, valor, media_redondeada):
    sobre_media = []
    for e in pokemon:
        if e[valor] > media_redondeada:
            sobre_media.append(e.name)
    return sobre_media

# 5. Cualquier otro que al alumno se le ocurra relacionado con los tipos de este bloque.
#   
#   En este caso se creará una función que sume todos los valores de stat de los pokemon.
#   Es decir HP, Attack, Defense, Sp. Atk, Sp. Def, Speed, los sumará, hará la media de los valores y devolverá
#   aquellos valores que sean iguales o superiores al parámetro fijado en "pokemon_test.py"

def media_stats(pokemon, valor_limite):
    lista_pokemon = []
    for e in pokemon:
        stats = []
        stats.append(e.hp)
        stats.append(e.attack)
        stats.append(e.defense)
        stats.append(e.spattack)
        stats.append(e.spdefense)
        stats.append(e.speed)
        suma = sum(stats)
        media = suma / 6
        if media >= valor_limite:
            lista_pokemon.append(e.name)
    return lista_pokemon

# Bloque 4

# 1. Obtener el registro (o algunos campos del registro) que contiene el valor máximo o mínimo 
# de un campo determinado.

def maximo_valor(pokemon, valor):
    lista_valores = []
    for e in pokemon:
        lista_valores.append(e[valor])
    lista_valores.sort()
    return lista_valores[-1]

# Bloque 5

# 2. Obtener una lista de registros (o algunos campos del registro) ordenada con los n registros 
# con mayor (o menor) valor en un campo determinado, de los registros que cumplen determinada condición. 
# Donde “n” es un parámetro que debe recibir la función.

def maximo_por_tipo(pokemon, tipo, valor, cantidad):
    diccionario_pkm = {}
    for e in pokemon:
        if e.type1 == tipo or e.type2 == tipo:
            diccionario_pkm[e.name] = e[valor]
    diccionario_pkm_ord = sorted(diccionario_pkm.items(), key=lambda item: item[1], reverse=True)
    return diccionario_pkm_ord[:cantidad]

# Bloque 6

# 1. Obtener un diccionario que permita agrupar, los registros que cumplen determinada condición, por algún 
# campo (clave). A cada clave se le hará corresponder una lista con los registros que contienen esa clave.

# En este caso, la condición es un filtro que solo añade los que tienen un valor mayor al preestablecido
# en una categoría tambíen establecida anteriormente.

def dicc_tipos(pokemon, filtro, valor):
    diccionario_tipos = {}
    for e in pokemon:
        if e[filtro] >= valor:
            if e.type1 in diccionario_tipos:
                diccionario_tipos[e.type1].append(e.name)
            else:
                diccionario_tipos[e.type1] = [e.name]
            if e.type2 in diccionario_tipos:
                diccionario_tipos[e.type2].append(e.name)
            else:
                diccionario_tipos[e.type2] = [e.name]
    return diccionario_tipos

# 3. Obtener un diccionario que permita agrupar, los registros que cumplen determinada condición, por algún 
# campo (clave) y que haga corresponder a cada clave una lista con los registros que cumplen determinada 
# condición.

# En este caso, la condiciones son iguales al apartado anterior añadiendo un filtro por tipo de pokemon.

def dicc_filtro_tipos(pokemon, filtro, valor, tipo):
    dict_tipos = {}
    for e in pokemon:
        if e.type1 == tipo or e.type2 == tipo:
            if e[filtro] >= valor:
                if tipo in dict_tipos:
                    dict_tipos[tipo].append(e.name)
                else:
                    dict_tipos[tipo] = [e.name]
    return dict_tipos