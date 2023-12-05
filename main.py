from os import system   
system("cls")
import sqlite3
from colorama import Fore
          

print (Fore.GREEN + "TRABAJO FINAL" .center(60,"*"))
print("Alumno: Hugo Ezequiel Sanchez" .center(60))
print("Alumno: Malen Bruno" .center(60))
print("Alumno: Lourdes Brodsky" .center(60))
print("Alumno: Juan C. Gonzalez" .center(60))
print("Alumno: Norely Luna" .center(60))
print("Alumno: Domingo" .center(60))

def menu():
    print ("BIENVENIDOS AL CLUB" .center(60,"*"))
    print("[1] Ingresar socio")
    print("[2] Modificar socio")
    print("[3] Eliminar socio")
    print("[4] Consultar socio")
    print("[5] Listar socios")
    print("[6] Listar actividades")
    print("[7] Agregar actividades")
    print("[8] Borrar actividades")
    print("[0] Salir \n")
    opcion=int(input("Ingrese una opcion: "))
    return opcion

def ingresar_socio():
    conexion = sqlite3.connect("datos_final.bd")
    cursor=conexion.cursor()
    print ("AGREGAR SOCIO AL CLUB" .center(60,"*"))
    id_usuario = int(input("Ingrese id del cliente a cargar: "))
    nombre = input("Ingrese nombre de cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    edad = int(input("Ingrese la edad del cliente: ")) 
    sexo = input("Ingrese el sexo del cliente: ")
    telefono = int (input("Ingrese telefono del cliente: "))
    deporte = input("Ingrese el doporte a precticar por el cliente: ")
    cursor.execute("INSERT INTO usuarios (id_usuario,nombre,apellido,edad,sexo,telefono,deporte)VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}')"
                   .format(id_usuario,nombre,apellido,edad,sexo,telefono,deporte))
    conexion.commit()
    conexion.close()
    print("\n CLIENTE AGREGADO CORRECTAMENTE \n")
    
def consultar_socio():
    conexion = sqlite3.connect("datos_final.bd")
    cursor = conexion.cursor()
    print ("CONSULTA SOCIO" .center(60,"*"))
    id_consulta = input("Ingrese el id del usuario a consultar: ")
    base = "SELECT * from usuarios WHERE id_usuario = ?"
    cursor.execute(base,(id_consulta))
    resultado = cursor.fetchall()
    for r in resultado:
        print("\n",r,"\n")
    conexion.close()
    
    
def modificar_socio():
    conexion = sqlite3.connect("datos_final.bd")
    cursor = conexion.cursor()
    print ("EDITAR SOCIOS" .center(60,"*"))
    id_modificar = int(input("Ingrese el numero de id de usuario a modificar: "))
    id_usuarioActualizado = int(input("Actualice id del cliente: "))
    nombreActualizado = input("Actualice nombre de cliente: ")
    apellidoActualizaco = input("Actualice nuevo apellido del cliente: ")
    edadActualizada = int(input("Actualice la edad del cliente: ")) 
    sexoActualizado = input("Ingrese el sexo del cliente: ")
    deporteActualizado = input("Actualice el doporte a precticar por el cliente: ")
    telefonoActualizado = int (input("Actualice telefono del cliente: "))
    
    base_actualizada = "UPDATE usuarios SET id_usuario = ?, nombre = ?, apellido = ?,edad = ?,sexo = ?,deporte = ?, telefono = ? WHERE id_usuario = ?"
    cursor.execute(base_actualizada,(id_usuarioActualizado,nombreActualizado,apellidoActualizaco,edadActualizada,sexoActualizado,
                                     deporteActualizado,telefonoActualizado,id_modificar))
     
    conexion.commit()
    conexion.close()
    print("\n CLIENTE ACTUALIZADO CORRECTAMENTE \n")
    
    

def eliminar_socio():
    conexion = sqlite3.connect("datos_final.bd")
    cursor = conexion.cursor()
    print ("ELIMINAR SOCIOS" .center(60,"*"))
    id_eliminar = input("Ingrese el id del usuario a eliminar: ")
    base = "DELETE from usuarios WHERE id_usuario = ?"
    cursor.execute(base,(id_eliminar,))
    conexion.commit()
    conexion.close()
    print("\n Usuario liminado correctamente \n ")
    
    
def listar_socios():
    conexion = sqlite3.connect("datos_final.bd")
    cursor = conexion.cursor()
    print ("LISTADO DE SOCIOS" .center(60,"*"))
    base = "SELECT * FROM usuarios"
    cursor.execute(base)
    lista = cursor.fetchall()
    for listado in lista:
        print(listado)


def agragar_actividad():
    conexion = sqlite3.connect("datos_final.bd")
    cursor=conexion.cursor()
    print ("AGREGAR ACTIVIDAD AL CLUB" .center(60,"*"))
    id = int(input("Ingrese id de la actividad a cargar: "))
    deporte = input("Ingrese nombre de la actividad: ")
   
    cursor.execute("INSERT INTO deportes (id,deporte)VALUES('{0}','{1}')"
                   .format(id,deporte))
    conexion.commit()
    conexion.close()
    print("\n ACTIVIDAD AGREGADA CORRECTAMENTE \n")

def listar_actividades():
    conexion = sqlite3.connect("datos_final.bd")
    cursor = conexion.cursor()
    print ("LISTADO ACTIVIDADES DEL CLUB" .center(60,"*"))
    base = "SELECT * FROM deportes"
    cursor.execute(base)
    lista = cursor.fetchall()
    for listado in lista:
        print(listado)

def borrar_actividades():
    conexion = sqlite3.connect("datos_final.bd")
    cursor = conexion.cursor()
    print ("ELIMINAR ACTIVIDAD" .center(60,"*"))
    eleccion = int(input("\n Si desea eliminar actividad por id presione 1, si desea hacer por nombre presione 2  :"))
    if eleccion == 2:
        deporte_eliminar = input("\n Ingrese la activiad a eliminar: ")
        base = "DELETE from deportes WHERE deporte = ?"
        cursor.execute(base,(deporte_eliminar,))
    elif eleccion == 1 :
        deporte_eliminar = input("\n Ingrese id de la activiad a eliminar: ")
        base = "DELETE from deportes WHERE id = ?"
        cursor.execute(base,(deporte_eliminar,))
    conexion.commit()
    conexion.close()
    print("\n Actividad eliminada correctamente \n ")
               
def main():
    
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            ingresar_socio()
        elif opcion == 2:
            modificar_socio()
        elif opcion == 3:
            eliminar_socio()
        elif opcion == 4:
            consultar_socio()
        elif opcion == 5:
            listar_socios()
        elif opcion == 6:
            listar_actividades()
        elif opcion == 7:
            agragar_actividad()
        elif opcion == 8:
            borrar_actividades()
        else:
            print("Opcion incorrecta")
        opcion=menu()
    return 

main()