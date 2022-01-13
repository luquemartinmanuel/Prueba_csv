# Importa los datos de pokemon.py y el csv pokemon.csv

from pokemon import *

if __name__ == "__main__":
    fichero = "data\pokemon.csv"
    pokemon = lee_pokemon(fichero)


# Lee la función que representa los 3 primeros y 3 últimos pokemon por pantalla,
# junto con la lista de tcuantos pokemon hay en el csv


def test_lee_pokemon(pokemon):
    print(f"Los tres primeros pokemon son:\n", pokemon[:3])
    print(f"Los tres últimos pokemon son:\n", pokemon[-3:])
    print("El total de pokemon en la lista es de {}".format(len(pokemon)))


# Esta función genera una lista con todos los datos del registro de la lista de datos


def test_lista_pokemon(pokemon):
    print("La lista de datos de los registros es:\n {}".format(pokemon))


# Lee la función que filtra los pokemon por tipo


def test_filtra_pokemon(pokemon):
    elemento = "Ice"
    print("Los pokemon de tipo {}:\n {}".format(elemento, (filtra_tipos(pokemon, elemento))))


# Lee la función que filtra el csv por campos


def test_conjunto_campos(pokemon):
    print("Los tipos de pokemon son:\n {}".format(conjunto_campos(pokemon)))


# Lee la función que calcula los pokemon cuyo valor definido supere a la media


def test_media_registros(pokemon):
    valor = "HP"
    valor_lista = 4
    print("La media de los valores de ", valor, "es: {}.".format(media_valores(pokemon, valor_lista)))
    media = media_valores(pokemon, valor_lista)
    print("Los pokemon que superan la media de ", valor, " son: \n {}".format(valores_sobre_media(pokemon, valor_lista, media)))


# Lee la función que devuelve la lista de pokemon cuya media de stats superan un valor límite predefinido


def test_media_stats(pokemon):
    limite = 100
    print("Los pokemon cuyos stats superan el valor límite {} son: \n{}".format(limite, media_stats(pokemon, limite)))


# Lee la función que devuelve el número máximo de el valor definido


def test_maximo_valor(pokemon):
    valor = "ataque"
    valor_lista = 5
    print("El valor máximo de ", valor, "es:\n {}".format(maximo_valor(pokemon, valor_lista)))


# Lee la función que devuelve una lista con los mayores valores de un parámetro


def test_maximo_por_tipo(pokemon):
    valor = "velocidad"
    valor_lista = 9
    tipo = "Water"
    cantidad = 6
    print("Los", cantidad, "pokemon con mayores valores de", valor, "del tipo", tipo, "y su valor son:\n {}".format(maximo_por_tipo(pokemon, tipo, valor_lista, cantidad)))


# Lee la función que devuelve un diccionario agrupado por registros filtrado por los valores de un parámetro


def test_dicc_tipos(pokemon):
    filtro = "ataque"
    filtro_lista = 5
    valor = 150
    print("Los pokemon con", filtro, "mayor o igual a", valor, "ordenados por su tipo son:\n {}".format(dicc_tipos(pokemon, filtro_lista, valor)))


# Lee la función que devuelve un diccionario agrupado por registros filtrado por registros y por valores de un parámetro


def test_dicc_filtro_tipos(pokemon):
    filtro = "ataque"
    filtro_lista = 5
    valor = 150
    tipo = "Fighting"
    print("Los pokemon de tipo", tipo, "con", filtro, "mayor o igual a", valor, "son:\n{}".format(dicc_filtro_tipos(pokemon, filtro_lista, valor, tipo)))


test_lee_pokemon(pokemon)
test_lista_pokemon(pokemon)
test_filtra_pokemon(pokemon)
test_conjunto_campos(pokemon)
test_media_registros(pokemon)
test_media_stats(pokemon)
test_maximo_valor(pokemon)
test_maximo_por_tipo(pokemon)
test_dicc_tipos(pokemon)
test_dicc_filtro_tipos(pokemon)