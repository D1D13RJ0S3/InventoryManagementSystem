# Ovedisa Inventory System Management

## Descripcion
Esta aplicacion esta diseñada para gestionar inventarios con una interfaz moderna y sencilla. Incluye funcionalidades como un dashboard interactivo, gestion de productos y una pagina informativa sobre los desarrolladores.

## Estructura del Proyecto

### Archivos Principales:
- **App.svelte:** Componente principal que coordina las paginas y el sidebar.
- **Sidebar.svelte:** Menu lateral para navegar entre las distintas paginas.
- **WelcomePage.svelte:** Pantalla de bienvenida con opcion para entrar al dashboard.
- **Dashboard.svelte:** Muestra una grafica interactiva y un resumen del inventario.
- **InventoryPage.svelte:** Gestion de productos del inventario (crear, actualizar, eliminar).
- **AboutUs.svelte:** Informacion sobre los desarrolladores del proyecto.

### Scripts
- **`npm run dev`**: Inicia la aplicacion en modo desarrollo con recarga en vivo.
- **`npm run build`**: Genera los archivos optimizados para produccion.
- **`npm start`**: Sirve la aplicacion como una SPA. (Single Page Application)

## Dependencias

### Principales:
- **Svelte:** Framework principal del proyecto.
- **SvelteKit:** Framework para crear aplicaciones web con Svelte


### Desarrollo:
- **Serve:** Servidor para producción (`npm start`).
- **Sirv-cli:** Servidor ligero utilizado en modo desarrollo.
- **Rollup:** Bundler utilizado para construir la aplicación.

## Requisitos Previos

### Instalar Node.js
- Descargar e instalar Node.js especificamente la version 22.12.0 desde [nodejs.org](https://nodejs.org/dist/v22.12.0/node-v22.12.0-x64.msi)
- Verificar que Node.js se instalo correctamente ejecutando `node -v` en la consola del equipo
- Instalar npm en la carpeta frontend ejecutando `npm install` en la consola


## Uso 
### Modo Desarrollo
2. Iniciar modo desarrollo: `npm run dev`
### Modo Produccion (No se actualiza automaticamente si se hace un cambio)
3. Ejecutar primero: `npm run build`
4. Ejecutar seguidamente: `npm start` 

## Estilo
El diseño esta basado en una combinacion de un sidebar y un contenedor principal con colores neutros para resaltar el contenido.
