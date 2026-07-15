import flet as ft

def libro_form():
    titulo_input = ft.TextField(
        label = "Titulo del libro: ",
        width = 400
    )

    autor_input = ft.TextField(
        label = "Autor del libro: ",
        width = 400
    )

    isbn_input = ft.TextField(
        label = "ISBN: ",
        width = 400 
    )

    mensaje = ft.Text(
        "",
        color = ft.Colors.GREEN
    )