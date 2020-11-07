## Notas
Al principio de la web todos los contenidos eran texto plano, Text-based, conforme iba creciendo, las necesidades tambien cambiaban y se hacia necesario implementar bases de datos e interfaces graficas, se hace necesario poder ejecutar scripts en el servidor a traves de requests,
esto se hace muy dificil de mantener y escalar.

Luego nacen los frameworks de desarrollo web que permiten lidiar con elementos como protocolos HTTPS, conecxiones de bases de datos e interacciones con el HTML, los templates.

Django nace en el 2003 con la necesidad de generar sitios web de manera agil y escalables y seguros.

### Inicialización del entorno de desarrollo

- Descargar python y verificar version:

```
python --version
```

- Instalar virtualenv para crear entornos virtuales:

```
pip install virtualenv
```

- Crear entorno virtual con virtualenv:
El entorno virtual es un folder donde se instalan todas las dependecnias para que las mismas nos se instalen en el entorno global, esto para evitar problemas de compatibilidad.

```
mkdir entornos
cd entornos
virtualenv init 
```

- Para activar el entorno se usa el archivo activate, como resultado aparece (init) al principio de la linea de comandos:

```
cd init/Scripts

# desde cmd o powershell:
./activate

# desde bash o linux:
source ./activate
```

- Para listar las dependencias (O paquetes instalados en el entorno) usamos el comando:

```
pip freeze
```

### Configuración del proyecto

- Instalar django en nuestro entorno:

```
pip install django -U
```

- Crear el proyecto desde el repositorio:

```
mkdir Proyecto
cd Proyecto
django-admin startproject ProyectoDjango
```
- Esto creara varios archivos:
    - \_init_.py : Declara el proyecto como un modulo de python
    - settings.py : Es el archivo mas importante pues declara toda la configuracion de nuestro proyecto
    - urls.py : Es el archivo de entrada para todas las peticiones que lleguen al proyecto.
    - wsgi.py : Es el archivo usado para implementacion y la interfaz wsgi para el servidor de produccion.
    - manage.py: Es un archivo de interfaz para django-admin

- Se pueden guardar las dependencias instaladas en un archivo .txt:

```
pip freeze > dependencies.txt
```

- Para arrancar el proyecto:

```
cd Proyecto/ProyectoDjango
python manage.py runserver
```

## El archivo seetings
 - BASE_DIR: Declara el lugar donde esta corriendo el proyecto

- SECRET_KEY: Se usa para las contraseñas y las sesiones que se almacenan en la base de datos

- DEBUG: Marca si nuestro proyecto está en desarrollo, `True`. Si esta en produccion es importante que esté en `False`

- ALLOWED_HOSTS: Que host tienen permitido interactuar con nuestro proyecto,

- INSTALLED_APPS: Que aplicaciones estan ligadas con el proyecto

- ROOT_URLCONF: Define el archivo principal de urls

