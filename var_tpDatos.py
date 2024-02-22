
###################################Tipos de Datos. Variables, 

"""  * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).

 * - Crea una variable (y una constante si el lenguaje lo soporta).

 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */ """


# https://python.org

# Comentario en una línea

"""
Esto también es
un comentario
en varias líneas
"""

'''
Esto también es
un comentario
en varias líneas
'''

my_variable = "Mi variable"
my_variable = "Nuevo valor de mi variable"

MY_CONSTANT = "Mi constante"  # por convención

my_int = 1
my_float = 1.5
my_bool = True
my_bool = False
my_string = "Mi cadena de texto"
my_other_string = 'Mi otra cadena de texto'

print("¡Hola, Python!")

print(type(my_int))
print(type(my_float))
print(type(my_bool))
print(type(my_string))