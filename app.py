from configparser import Error

from dao.libro_dao import LibroDAO
from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario
from models.libro import Libro

def ver_libros():
    try:    
        libro_dao = LibroDAO()

        libros = libro_dao.obtener_todos()

        print("=== Libros en la base de datos ===")

        if len(libros) == 0:
            print("No hay libros registrados.")
        else:
            for libro in libros:
                print("----------------------------------------------")
                print(
                    f"ID: {libro.id}, Titulo: {libro.titulo},"
                    f"Autor: {libro.autor}, ISBN: {libro.isbn},"
                    f"Disponible: {'Si' if libro.disponible else 'No'}"
                )
                print("----------------------------------------------")
        print("\nConexion exitosa a la base de datos.")
    except Exception as e:
        print(f"Error: ")
        print(e)

def insertar_libro():
    titulo = input("Escribe el titulo del nuevo libro: ")
    autor = int(input("Escribe el id del autor: "))
    isbn = input("Escribe el isbn del nuevo libro: ")
    disponible = True
    try:
        libro_dao = LibroDAO()
        id = libro_dao.obtener_ultimo_id() + 1
        libro = Libro(id, titulo, autor, isbn, disponible)
        libro_dao.insertar(libro)
        print("Insercion realizada correctamente.")
    except Exception as e:
        print("Error al insertar un nuevo libro: ")
        print(e)

def actualizar_libro():
    print("Selecciona el libro a actualizar")
    try:
        libro_dao = LibroDAO()
        ver_libros()
        id = int(input("Escribe el id del libro a actualizar: "))
        titulo = input("Escribe el nuevo titulo del libro: ")
        autor = input("Escribe el nuevo id del autor: ")
        isbn = input("Escribe el nuevo isbn del libro: ")
        disponible = bool(input("Escribe el nuevo valor de disponible: "))
        libro = Libro(id, titulo, autor, isbn, disponible)
        libro_dao.actualizar(libro)
        print(f'El libro con ID {id} ha sido actualizado correctamente')
    except Exception as e:
            print("Error al actualizar un libro")
            print(e)

def eliminar_libro():
    try:
        libro_dao = LibroDAO()
        print("Lista de libros disponibles:")
        ver_libros()
        id = int(input("Escribe el id del libro a eliminar: "))
        libro_dao.eliminar(id)
        print(f"El libro {id} ha sido eliminado con exito")
    except Exception as e:
        print(f"Error al eliminar el libro {id}")
        print(e)

def menu_libros():
    print("1. Ver todos los libros")
    print("2. Insertar un nuevo libro")
    print("3. Actualizar un libro")
    print("4. Eliminar un libro")
    opcion = int(input("Seleciona una opcion (1-4): "))

    match opcion:
        case 1:
            ver_libros()
        case 2:
            insertar_libro()
        case 3:
            actualizar_libro()
        case 4:
            eliminar_libro()

#USUARIOS

def ver_usuarios():
    try:    
        usuario_dao = UsuarioDAO()

        usuarios = usuario_dao.obtener_todos()

        print("=== Usuarios en la base de datos ===")

        if len(usuarios) == 0:
            print("No hay usuarios registrados.")
        else:
            for usuario in usuarios:
                print("----------------------------------------------")
                print(
                    f"ID: {usuario.id}, Nombre: {usuario.nombre},"
                    f"Matricula: {usuario.matricula}, Carrera: {usuario.carrera},"
                    f"Correo: {usuario.correo}, Activo: {'Si' if usuario.activo else 'No'}"
                )
                print("----------------------------------------------")
        print("\nConexion exitosa a la base de datos.")
    except Exception as e:
        print(f"Error: ")
        print(e)

def insertar_usuarios():
    nombre = input("Escribe el nombre del nuevo usuario: ")
    matricula = input("Escribe la matricula del nuevo usuario: ")
    carrera = input("Escribe la carrera del nuevo usuario: ")
    correo = input("Escribe el correo del nuevo usuario: ")
    activo = True
    try:
        usuario_dao = UsuarioDAO()
        id = usuario_dao.obtener_ultimo_id() + 1
        usuario = Usuario(id, nombre, matricula, carrera, correo, activo)
        usuario_dao.insertar(usuario)
        print("Insercion realizada correctamente.")
    except Exception as e:
        print("Error al insertar un nuevo usuario: ")
        print(e)

def actualizar_usuarios():
    print("Selecciona el usuario a actualizar")
    try:
        usuario_dao = UsuarioDAO()
        ver_usuarios()
        id = int(input("Escribe el id del usuario a actualizar: "))
        nombre = input("Escribe el nuevo nombre del usuario: ")
        matricula = input("Escribe la nueva matricula del usuario: ")
        carrera = input("Escribe la nueva carrera del usuario: ")
        correo = input("Escribe el nuevo correo del usuario: ")
        activo = bool(input("Escribe el nuevo valor de activo: "))
        usuario = Usuario(id, nombre, matricula, carrera, correo, activo)
        usuario_dao.actualizar(usuario)
        print(f'El usuario con ID {id} ha sido actualizado correctamente')
    except Exception as e:
            print("Error al actualizar un usuario")
            print(e)

def eliminar_usuarios():
    try:
        usuario_dao = UsuarioDAO()
        print("Lista de usuarios disponibles:")
        ver_usuarios()
        id = int(input("Escribe el id del usuario a eliminar: "))
        usuario_dao.eliminar(id)
        print(f"El usuario {id} ha sido eliminado con exito")
    except Exception as e:
        print(f"Error al eliminar el usuario {id}")
        print(e)

def menu_usuarios():
    print("1. Ver todos los usuarios")
    print("2. Insertar un nuevo usuario")
    print("3. Actualizar un usuario")
    print("4. Eliminar un usuario")
    opcion = int(input("Seleciona una opcion (1-4): "))

    match opcion:
        case 1:
            ver_usuarios()
        case 2:
            insertar_usuarios()
        case 3:
            actualizar_usuarios()
        case 4:
            eliminar_usuarios()


def main():
    print("=== BIBLIOTECA UNIVERSITARIA ===")
    print("Menu de opciones")
    print("1.Menu de libros")
    print("2.Menu de usuarios")
    opcion = int(input("Selecciona una opcion (1-2): "))

    match opcion:
        case 1:
            menu_libros()
        case 2:
            menu_usuarios()


if __name__ == "__main__":
    main()