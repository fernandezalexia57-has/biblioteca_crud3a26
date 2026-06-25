from configparser import Error

from dao.libro_dao import LibroDAO
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


def main():
    print("=== BIBLIOTECA UNIVERSITARIA ===")
    print("Menu de opciones")
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


if __name__ == "__main__":
    main()