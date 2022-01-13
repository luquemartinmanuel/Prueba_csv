# Proyecto del primer cuatrimestre de fundamentos de la programación

Autor: Manuel Antonio Luque Martín

Este proyecto tiene como objetivo analizar y manejar los datos del dataset llamado pokemon.csv que se encuentra en este mismo proyecto. El archivo csv es una modificación del encontrado en este enlace https://www.kaggle.com/terminus7/pokemon-challenge?select=pokemon.csv.

## Estructura del proyecto y sus carpetas

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **\<pokemon.py\>**: Contiene las funciones que trabajan con los datos del archivo pokemon.csv.
  * **\<pokemon_test.py\>**: Contiene funciones de prueba para utilizar las funciones del módulo pokemon.py.
* **/data**: Contiene el dataset o datasets del proyecto
    * **\<pokemon.csv\>**: Archivo del que se sacarán los datos para trabajar en el proyecto.
    
## Estructura del *dataset*

Cada fila del dataset presenta diversos datos de cada uno de los pokemon, ordenados por un sistema estandarizado denominado "orden de la pokedex". Cada una de las filas está dividida en 13 columnas, con la descripción siguiente:

* **\<#>**: de tipo \<int\>, es un identificador de tipo entero que representa la posición de cada pokemon en el previamente nombrado "orden de la pokedex".
* **\<Name>**: de tipo \<str\>, representa el nombre de cada pokemon.
* **\<Type 1>**: de tipo \<str\>, representa el primer tipo elemental de cada pokemon.
* **\<Type 2>**: de tipo \<str\>, representa el segundo tipo elemental de cada pokemon.
* **\<HP>**: de tipo \<int\>, representa la vida base del pokemon.
* **\<Attack>**: de tipo \<int\>, representa el ataque base del pokemon.
* **\<Defense>**: de tipo \<int\>, representa la defensa base del pokemon.
* **\<Sp. Atk>**: de tipo \<int\>, representa el ataque especial base del pokemon.
* **\<Sp. Def>**: de tipo \<int\>, representa la defensa especial base del pokemon.
* **\<Speed>**: de tipo \<int\>, representa la velocidad base del pokemon.
* **\<Generation>**: de tipo \<int\>, representa la generación a la que pertenece el pokemon.
* **\<Legendary>**: de tipo \<bool\>, indica si el pokemon pertenece a una clase determinada llamada "legendario" o no.
* **\<Date>**: de tipo \<datetime\>, representa la fecha en la que se creó el pokemon.

## Tipos implementados

Para trabajar con los datos se ha utilizado la siguiente tupla con nombre: 

pokemon = namedtuple('pokemon', 'num_pokedex, name, type1, type2, hp, attack, defense, spattack, spdefense, speed, generation, legendary, date_pkm')

En la que los tipos de cada uno de los campos son los siguientes:

pokemon(int, str, str, str, int, int, int, int, int, int, int, bool, datetime)

## Funciones implementadas

Las funciones de este proyecto están divididas en entregas y en bloques para cada uno de los módulos. El módulo principal y en el que se hará referencia a los bloques de cada entrega es pokemon.py.

###\<Entrega 1\>

  ###\<Bloque 0\>

    ###\<pokemon.py\>

    * **<lee_pokemon(fichero)>**: Esta función lee los datos del fichero csv y devuelve una lista de tuplas en la que cada una de las tuplas es una fila del fichero.

    ###\<pokemon_test.py\>

    * **<test_lee_pokemon(pokemon)>**: Esta función representa los datos obtenidos en la función lee_pokemon(pokemon), en este caso representa las tres primeras y las tres últimas filas y el número de pokemon distintos.

###\<Entrega 2\>

  ###\<Bloque 1\>

    ###\<pokemon_test.py\>

    * **<test_lista_pokemon(pokemon)>**: Esta función ejecuta en una lista todos los datos de los registros del archivo de datos.

  ###\<Bloque 2\>

    ###**<Apartados 1 y 2>**

    ###\<pokemon.py\>

    * **<filtra_tipos(pokemon, tipo)>**: Esta función obtiene como resultado una lista de los pokemon que entran dentro del criterio seleccionado en las categorías type 1 y type 2.

    * **<conjunto_campos(pokemon)>**: Esta función obtiene del archivo csv un conjunto con todos los valores de los campos type 1 y type 2.

    ###\<pokemon_test.py\>

    * **<test_filtra_pokemon(pokemon)>**: Esta función representa por pantalla una lista con los pokemon elegidos dentro de la variable "elemento".

    * **<test_conjunto_campos(pokemon)>**: Esta función genera un conjunto con todos los valores, sin repetir, de las columnas type 1 y type 2.

  ###\<Bloque 3\>

    ###**<Apartados 4 y 5>**

    ###\<pokemon.py\>

    * **<media_valores(pokemon, valor)>**: Esta función genera una variable cuyo valor es la media aritmética de todos los elementos de una columna del archivo de datos.

    * **<valores_sobre_media(pokemon, valor, media_redondeada)>**: Esta función genera una lista con el nombre de todos los pokemon cuyo valor en la columna seleccionada en la función anterior es superior a la media.

    * **<media_stats(pokemon, valor_limite)>**: Esta función suma todos los valores numéricos de estadística de los registros (HP, Attack, Defense, Sp. Atk, Sp. Def y Speed), les realiza la media aritmética y devuelve una lista con todos los pokemon cuya media de estadísticas supera un valor prefijado.

    ###\<pokemon_test.py\>

    * **<test_media_registros(pokemon)>**: Esta función presenta por pantalla el valor de la media en base a la estadística prefijada y la lista de pokemon que cumplen el requisito.

    * **<test_media_stats(pokemon)>**: Esta función presenta por pantalla el valor prefijado y presenta una lista con los pokemon cuyas estadísticas superan dicho valor.

###\<Entrega 3\>

  ###\<Bloque 4\>

    ###**<Apartado 1>**

    ###\<pokemon.py\>

    * **<maximo_valor(pokemon, valor)>**: Esta función obtiene el valor máximo de una de las categorias.

    ###\<pokemon_test.py\>

    * **<test_maximo_valor(pokemon)>**: Esta función presenta por pantalla el valor máximo de una categoría prefijada.

  ###\<Bloque 5\>

    ###**<Apartado 2>**

    ###\<pokemon.py\>

    * **<maximo_por_tipo(pokemon, tipo, valor, cantidad)>**: Esta función crea un diccionario filtrado por tipo con el nombre del pokemon por clave y por valor el número de la estadística seleccionada previamente

    ###\<pokemon_test.py\>

    * **<test_maximo_por_tipo(pokemon)>**: Esta función presenta por pantalla una cantidad fijada anteriormente de pokemon de ordenada desde el mayor de la característa fijada, filtrado por tipo y con el nombre del pokemon y el valor de dicha característica.

  ###\<Bloque 6\>

    ###**<Apartados 1 y 3>**

    ###\<pokemon.py\>

    * **<dicc_tipos(pokemon, filtro, valor)>**: Esta función obtiene un diccionario ordenado por tipo de pokemon con el nombre de los mismos y filtrado por una característica determinada de valor mayor al prefijado

    * **<dicc_filtro_tipos(pokemon, filtro, valor, tipo)>**: Esta función obtiene un diccionario con los pokemon de un tipo y con mayor valor al seleccionado en una categoría prefijada.

    ###\<pokemon_test.py\>

    * **<test_dicc_tipos(pokemon)>**: Esta función presenta por pantalla a modo de diccionario los pokemon con una característica mayor a la prefijada y ordenados por tipo.

    * **<test_dicc_filtro_tipos(pokemon)>**: Esta función presenta por pantalla el diccionario con el tipo de pokemon seleccionado por clave y con el nombre de los pokemon de ese tipo con mayor valor de la característica fijada.

  ###\<Bloque 7\>

  Este bloque se ha ido repartiendo por todo el documento dentro de los apartados llamados "pokemon_test.py".