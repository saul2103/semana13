# Restaurante App

**Estudiante:** Bryan Saul Iza Llano

Aplicación de escritorio desarrollada en Python con Tkinter para gestionar un sistema de ingreso de restaurante básico desde una interfaz gráfica.

## Descripción

La aplicación cuenta con un sistema de login, una vista principal y una estructura modular para separar la lógica de negocio, la persistencia de datos y la interfaz de usuario.

Permite:

- iniciar sesión con un usuario registrado
- cargar productos desde archivos JSON
- mostrar usuarios registrados en la interfaz
- navegar entre pantallas dentro de la misma ventana
- mantener los datos en archivos locales del proyecto

## Estructura del proyecto

```text
restaurante_app/
├── main.py
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
└── ui/
    ├── __init__.py
    ├── login_view.py
    └── main_view.py
```

## Componentes principales

### Modelos

- `Usuario`: representa a un usuario del sistema con identificador, nombre, usuario y contraseña.
- `Producto`: representa un producto con código, nombre y precio.

### Servicios

- `ArchivoServicio`: se encarga de leer y escribir archivos JSON en la carpeta de datos.
- `RestauranteServicio`: carga los datos desde JSON, valida credenciales y expone listas de usuarios y productos para la interfaz.

### Interfaz

- `loginview`: pantalla de inicio de sesión.
- `MainView`: pantalla principal con encabezado, menú y contenido dinámico.

## Datos iniciales

La aplicación incluye un usuario de prueba y algunos productos de ejemplo:

Usuario:
- usuario: `saul`
- contraseña: `saul123`

Productos:
- P001 - Ceviche
- P002 - Lomo saltado
- P003 - Jugo natural

## Cómo ejecutar

Desde la carpeta principal del proyecto, ejecuta:

```bash
python restaurante_app/main.py
```

## Consideraciones

- Los datos se almacenan en archivos JSON dentro de la carpeta `restaurante_app/datos`.
- La interfaz está construida con `tkinter` y usa ventanas y frames para cambiar entre pantallas sin abrir nuevas instancias de la aplicación.
- Actualmente la app está enfocada en login, listado de usuarios y listado de productos. Las opciones como "Prestamos" y "Ventas" están preparadas como funcionalidades pendientes.

## Requisitos

- Python 3.9 o superior
- Tkinter disponible en la instalación estándar de Python
