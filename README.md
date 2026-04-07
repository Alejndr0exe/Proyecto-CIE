# Centro de Ecología Integrativa (CEI) - Plataforma Web

Plataforma web oficial y sistema de gestión de contenidos desarrollado para el Centro de Ecología Integrativa de la Universidad de Talca. 

Este proyecto proporciona un portal dinámico para la difusión pública de investigaciones, áreas de estudio y noticias del centro, combinado con un panel de administración para la gestión interna de la información.

## 🚀 Características Principales

* **Portal Dinámico:** Interfaz de usuario responsiva para explorar áreas de investigación, publicaciones y perfiles del equipo.
* **Panel de Administración:** Sistema integrado (basado en Django Admin) que permite al personal del CEI agregar, editar y eliminar contenido web de manera autónoma.
* **Buscadores y Filtros:** Herramientas de ordenamiento y filtrado para facilitar el acceso a la base de datos de publicaciones y proyectos.

## 🛠️ Tecnologías Utilizadas

* **Back-end:** Python, Django
* **Front-end:** HTML5, CSS3, JavaScript, Bootstrap
* **Base de Datos:** Relacional (SQL)
* **Despliegue:** cPanel / Servidor Web

## ⚙️ Instalación y Configuración Local

Si deseas correr este proyecto en un entorno local, sigue estos pasos:

1. Clona el repositorio:
   ```bash
   git clone [https://github.com/Alejndr0exe/Proyecto-CIE](https://github.com/Alejndr0exe/Proyecto-CIE)

2. Crea y activa un entorno virtual:
    ```bash
    python -m venv venv
    # En Windows: venv\Scripts\activate
    # En macOS/Linux: source venv/bin/activate

3. Instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt

4. Realiza las migraciones de la base de datos:
    ```bash
    python manage.py migrate

5. Inicia el servidor de desarrollo:
    ```bash
    python manage.py runserver

El proyecto estará disponible en http://127.0.0.1:8000/.