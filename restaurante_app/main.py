import tkinter as tk
from pathlib import Path

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import loginview
from ui.main_view import MainView


class RestauranteApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Restaurante App - tkinter")
        self.root.geometry("600x500")
        self.root.minsize(560, 460)

        # Prepara los servicios que usara en la vista principal y en el login.
        ruta_base = Path(__file__).resolve().parent
        archivo_servicio = ArchivoServicio(ruta_base / "datos")
        self.restaurante_servicio = RestauranteServicio(archivo_servicio)

        self.vista_actual = None
        self.mostrar_login()

    def cambiar_vista(self, nueva_vista):
        # Cambia la vista actual por la nueva vista.
        if self.vista_actual is not None:
            self.vista_actual.pack_forget()

        self.vista_actual = nueva_vista
        self.vista_actual.pack(fill="both", expand=True)

    def mostrar_login(self):
        # Muestra la vista de login.
        vista = loginview(self.root, self.restaurante_servicio, self.mostrar_interfaz_principal)
        self.cambiar_vista(vista)

    def mostrar_interfaz_principal(self, usuario_actual):
        # Muestra la vista principal de la aplicacion, luego de un acceso exitoso.
        vista = MainView(self.root, self.restaurante_servicio, usuario_actual, self.mostrar_login)
        self.cambiar_vista(vista)

    def ejecutar(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = RestauranteApp()
    app.ejecutar()
