
############################################## Funciones y alcances ######################################################/*
"""  * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */ """

def retornar_num(x,y) -> int: 
    cont= 0
    for num in range (1,101):
        if num %3 == 0 and num % 5 == 0:
            print(x+y)
        elif num % 3 ==0:
            print (x)
        elif num % 5 ==0:
            print (y)
        else:
            print (num)
            cont+=1
    return cont

print (retornar_num("fuzz","buzz"))



#######################################################

#funciones definidas por el usuario

 #funciones Simples
def greet ():
    print("Hola, python")
#llamar funcion
greet()


#funcion de retorno
def return_greet ():
    return "Hola, Python!!"
print(return_greet())


#funcion con argumento
def arg_greet(greet ,name):

    ##f=interpolacion
    print(f"{greet},{name}")

arg_greet("Hi","Michael")


#funcion con argumento predeterminado
#no tiene parametro le doy un parametro
def default_arg_greet(name="Python"):
    print(f"Hola,{name}")

default_arg_greet ("Michael")
default_arg_greet ()


#con argumento y retorno
def return_args_greet (greet,name):
    return f"{greet},{name}"

print(return_args_greet("hi","brais")) 


#funcion con retorno de varios valores tuplas de valores
def multiple_return_greet():
    return "hola","python"

#desacoplar
greet,name=multiple_return_greet() 
print(greet)
print(name)


#con un numero variable de argumentos
#guarda mas de un resultado ej for
def variable_arg_greet (*names):
    for name in names:
        print(f"Hola,{name}")

variable_arg_greet ("python","Michael","Asus","Perro")


#con un numero variable de argumentos con palabra clave
def variable_key_arg_greet (**names):
    for key,value in names.items():
        print(f"{value} ({key})")

variable_key_arg_greet (languaje="python",
                        name="Michael",
                        marca="Asus",
                        edad=25)



####Funcion dentro de otra funcion 
def outer_function():
    def inner_function():
        print ("Funcion interna: Hola, Python !!")

    inner_function()

outer_function()


#Funciones de lenguajes (BUILT-in)

#Retorna el numero de la cadena de texto
print(len("Michael"))

#Retorna tipo de datos
print (type("Michael"))

#Mayuscula
print ("Michael".upper())



###Variables locales y globales Ambito scope
##variable local solo es para un ambito global es para todo el ambito
##siempre restringir el ambito buenas practicas
global_variable = "pyhon"

print(global_variable)


def hello_python():
    local_var= "Hola"
    print(f"{local_var},{global_variable})")


print(global_variable)

hello_python()