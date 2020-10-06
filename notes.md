## Notas

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
pip install django
```

- Crear el proyecto desde en el repositorio:

```
mkdir Proyecto
cd Proyecto
django-admin startproject ProyectoDjango
```

- Se pueden guardar las dependencias instaladas en un archivo .txt:

```
pip freeze > dependencies.txt
```

- Para arrancar el proyecto:

```
cd Proyecto/ProyectoDjango
python manage.py runserver
```
