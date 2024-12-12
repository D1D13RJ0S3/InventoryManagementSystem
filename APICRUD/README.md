# Proyecto de Gestión de Inventario

Este proyecto es una API RESTful construida con **FastAPI** y **SQLAlchemy** (usando `SQLModel`) para gestionar el inventario de productos. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre productos y está diseñada para integrarse con una base de datos local SQLite. El proyecto se puede configurar para trabajar con cualquier base de datos SQL, preferiblemente postgresql y mysql ya que el proyecto viene con dependencias para la correcta conexion a las bases de datos anteriormente mencionadas, pero SQLite es la predeterminada por su simplicidad.

## Descripción

La API permite realizar las siguientes operaciones sobre los productos:

- **Buscar un producto por ID**: Obtener los detalles de un producto usando su ID único.
- **Añadir un nuevo producto**: Crear un nuevo producto proporcionando los detalles del producto.
- **Obtener todos los productos**: Recuperar una lista de todos los productos almacenados en la base de datos.
- **Eliminar un producto por ID**: Eliminar un producto existente usando su ID.
- **Actualizar un producto**: Modificar parcialmente los detalles de un producto.

## Tecnologías Utilizadas

- **FastAPI**: Framework web para construir APIs rápidas y eficientes.
- **SQLAlchemy / SQLModel**: ORM para interactuar con bases de datos SQL.
- **Pydantic**: Para la validación de datos de entrada/salida.
- **SQLite**: Base de datos utilizada para almacenar los datos de los productos.
- **Uvicorn**: Servidor ASGI para ejecutar la aplicación FastAPI.
- **Visual Studio Code (VSCode)**: Editor de código utilizado para el desarrollo.

## Requisitos Previos y Configuración de la Base de Datos

### Instalación de SQLite
1. **Instalar SQLite**:
   - Para Windows: Descárgalo desde el sitio web oficial de SQLite (https://sqlitebrowser.org/dl/) y elige la version standard.
   - Para macOS: Generalmente ya está preinstalado o puedes instalarlo mediante Homebrew con `brew install sqlite`.
   - Para Linux: Instálalo usando el gestor de paquetes, por ejemplo, `sudo apt-get install sqlite3`.

### Configuración de la Base de Datos
1. Crea una base de datos con sqlite
2. Navega a la carpeta `database` en el directorio del proyecto.
3. Abre el archivo `db_config.py`.
4. Localiza la variable `sqlite_file_name`.
5. Establece el `sqlite_file_name` con el nombre del archivo .db  que creaste para la base de datos SQLite, por ejemplo:
   ```python
   sqlite_file_name = "inventory.db"
   ```

## Cómo Ejecutar el Proyecto

### 1. Instalar Dependencias

Asegúrate de tener Python 3.12 instalado (recomendado por compatibilidad). Si no tienes Python 3.12, instálalo desde el sitio web oficial de [Python](https://www.python.org/downloads/release/python-3120/).

Crea un **entorno virtual** llamado `venv` e instala las dependencias necesarias siguiendo estos pasos:

1. Abre **Visual Studio Code (VSCode)** y abre la carpeta del proyecto.
2. Abre la **Terminal** dentro de VSCode (`Ctrl + ~`).
3. **Crea un entorno virtual e instala las dependencias** llamado `venv` y tambien de instalar todas las dependencias que hay en el archivo requirements.txt (asegúrate de usar Python 3.12):

   ```bash
   python3.12 -m venv venv
   pip install -r requirements.txt
   ```

### 2. Ejecutar el Proyecto con `start.bat`

Este proyecto incluye un archivo `start.bat` que simplifica la ejecución de la aplicación al automatizar la activación del entorno virtual y el inicio del servidor Uvicorn en el puerto 5000. Sigue estos pasos para ejecutar el archivo `start.bat` desde Visual Studio Code:

1. Abre **Visual Studio Code (VSCode)** y navega hasta la carpeta del proyecto.
2. Abre la **Terminal** en VSCode (`Ctrl + ~`).
3. Ejecuta el archivo `start.bat` ingresando el siguiente comando en la terminal:

   ```bash
   .\start.bat
   ```

