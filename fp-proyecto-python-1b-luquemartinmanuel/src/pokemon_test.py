# Lee la función lee_pokemon que lee los datos del pokemon.csv
'''
from pokemon import lee_pokemon

pokedex = lee_pokemon('fp-proyecto-python-1b-luquemartinmanuel\data\pokemon\pokemon.csv')
print(pokedex[:20])
'''
# Lee la función que filtra los pokemon por tipo

from pokemon import filtra_tipos

tipo_filtrado = filtra_tipos('fp-proyecto-python-1b-luquemartinmanuel\data\pokemon\pokemon.csv', 'Bug')
print(tipo_filtrado)