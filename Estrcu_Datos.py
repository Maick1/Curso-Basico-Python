# /*
#  * EJERCICIO:
#  * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
#  *   en tu lenguaje.
#  * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea una agenda de contactos por terminal.
#  * - Debes implementar funcionalidades de búsqueda, inserción, actualización
#  *   y eliminación de contactos.
#  * - Cada contacto debe tener un nombre y un número de teléfono.
#  * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
#  *   y a continuación los datos necesarios para llevarla a cabo.
#  * - El programa no puede dejar introducir números de teléfono no númericos y con más
#  *   de 11 dígitos (o el número de dígitos que quieras).
#  * - También se debe proponer una operación de finalización del programa.
#  */

###### Estructuras de  Python
####Q son las estructura??

#Listas o array
#estrcutura ordenada donde se guardan Elementos
#nos sirve para manipular datos de la lista
#el orden es por insercion añade al final 
my_list =["Michael","Monica","Geordy","Ron"]
print (my_list)

#Agregar un usuario
my_list.append("Sofia")
print (my_list)

#Borrar
my_list.remove("Geordy")
print (my_list)

#Acceder a posicion
print (my_list[1])
#actualizar
my_list[1] = "Urion"
print (my_list)


##ordenar
my_list.sort() 
print (my_list)


####Tupla
#estructura donde se guarda mas de un dato pero son inmutables como se
#Crear no queremos cambiar puesto a q esta reservada en memoria

my_tuple= ("Veronica","Estefania","Garces","23")
#acceso en la tupla
print (my_tuple[1])
#sorted con tuple para q devuelva tuple y no lista
my_tuple = tuple(sorted(my_tuple))
print(my_tuple)
print (type(my_tuple))

print("----------------------------------------------------")

##Sets --> tipos de estructuras desordenada, buenas para guardar y recorrer datos
#no buenos para buscar datos
#Evita duplicados
my_set: set = {"Veronica","Estefania","Garces","23"}
print(my_set)

my_set.add("maick89911@gmail.com")
print(my_set)

my_set.remove("23")
print(my_set)

my_set = set(sorted (my_set)) #no se puede ordenar 
print("ordenar: ",my_set)

print(type(my_set))

print("******************************************************************")

###### Diccionario
#los diccionario son con clave, valor
my_dict : dict = { "Nombre":" Michael",
                  "Edad":"25", 
                  "Alias":"May",
}
#accedo al valor
print(my_dict["Edad"])

#inseerto valores
my_dict["Edad"]=26
print(my_dict)

#Actualizar Valor
my_dict["Nombre"]= "Manuel"
print(my_dict)

#Eliminar
del my_dict["Nombre"]
print(my_dict)

#ordenar de esta manera solo ordena claves
sorted (my_dict)
print("ordenar",my_dict)


#ordenar de manera correcta
my_dict = dict (sorted (my_dict.items()))
print(my_dict)


print (type(my_dict))


####################Ejercicio

def my_agenda():

    agenda = {}

    def insert_contact ():
        phone = input("Introduce el Telefono del Contacto: ")
        if phone.isdigit () and len (phone) > 0 and len (phone) <= 10:
            agenda[name] = phone
        else:
            print("Debes introducir # con 10 digitos. ")


    while True:

        print ("")
        print("1. Buscar Contacto")
        print("2. Insertar Contacto")
        print("3. Actualizar Contacto")
        print("4. Eliminar Contacto")
        print("5.Salir")

        #ingresar datos
        opcion= input ("\n Seleccione una opcion: ")

    ##es como el switch
        match opcion:   

            case "1":
                name = input("Introduce el Nombre del Contacto: ")
                if name in agenda:
                    print(f"El # de telefono de {name} es {agenda[name]}.")
                else:
                    print(f"El contacto{name} no existe. ")

            case "2":
                name = input("Introduce el Nombre del Contacto: ")
                insert_contact()

            case "3":
                name = input("Introduce el Nombre del Contacto a Actualizar: ")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"El contacto{name} no existe. ")


            case "4":
                name = input("Introduce el Nombre del Contacto a Eliminar: ")
                if name in agenda:
                    del agenda [name]
                    print ("Contacto Elminado...")
                else:
                    print(f"El contacto{name} no existe. ")

            case "5":
                print("Saldiendo de la Agenda")
                break
            case _:
                print("Opcion no valida. Elige una opcion del 1 al 5")
        



my_agenda()