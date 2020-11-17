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

## El archivo urls

Mediante los paths tu defines las URL a la que estas esperando responder algo, este es el primer argumento de la funcion `path()`, el segundo argumento es la vista que va a resolver el llamado.

Una vista puede ser una función o una clase que retorna un valor.

Para escribir una respuesta http importamos una clase desde django

```
from django.http import HttpResponse
```
Todas las vistas reciben un request y regresan una instancia de la clase HTTpResponse con el contenido deseado

```
def hello_world(request):
    return HttpResponse("Hola mundo")
```

Los paths reciben el path al que van a responder y la vista que vana  devolver.

```
path('hello-world/',hello_world)
```
## Vistas
### El objeto request
Dajngo usa los objetos `request` y `response` para pasar estados a traves del sistema.

La manera en que django procesa una peticion es la siguiente:

- Evalua el valor de la variable `ROOT_URLCONF` en el archivo `settings.py`
- Luego busca una variable llamada `urlpatterns` dentro del `urls.py` hasta que haga match con la url solicitada
- Cuando encuentra la url deseada, pasa la funcion con dos argumentos, una instancia de `httpResponses` y los demas argumentos de la funcion
- Si ninguna url coincide, manda una excepcion

Creamos un archivo llamado `views.py`para manejar las vistas de manera separada.

### pdb
Podemos acceder a un debgugger de python que se llama pdb, podemos invocarlo a traves del comando. Nos permite poner un debugger ene la consola cada vez que se ejecute un codigo antes de llegar a el.
```
import pdb; pdb.set_trace()
```
A traves del pdb podemos tener acceso a los objtos que testemos manejando en ese momento. por ejemplo al objeto request

- `request`:Nos da el tipo del objeto
- `request.META`: Devuelve la informacion META o header
- `request.methods`: Los metodos del request
- `request.GET`: Devuelve los argumentos del objeto get, con esto podemos tomar los argumentos que estan pasando por la URL y hacer operaciones.

### Tomar argumentos de la URL

Podemos tomar argumentos de la URL y hacer operaciones con ellos.

```
numbers = request.GET['numeros']
return HttpResponse(numbers)
```
Podemos devolver los argumentos de la URL en el formato deseado, por ejemplo en formato JSON

```
return HttpResponse((numbers), content_type='application/json')
```
#### Path converters

Con path converters podemos tomar argumentos de la url y convertirlos a un tipo de dato especifico en el archivo urls.py para ello usamos `<tipo_dato:nombre_argumento>`, por ejemplo `<string:name>`

### Creacion de Apps
Una app es un modulo de python que provee un conjunto de funcionalidades relacionadas entre si. las apps son una combinacion de models,vistas,urls y archivos estaticos. Las apps hacen algo en particular y pueden ser reuzables.
Un poryecto es una colecciones de configuraciones y apps para un sitio web especifico

Para crear una app en django se utiliza la siguiente instruccion, el nombre de la app siempre deberia ser en plural
```
python manage.py startapp nombre_app
```
Esto crea un nuevo folder con el nombre de la app, y contiene:

- migrations: Es un modulo de python que se encarga de grabar los cambios en la base de datos.
- \_init_.py: Declara la app como un modulo de python
- admin.py: Registra los modelos en el administador de django
- apps.py: Declara toda la configuracion de nuestra app
- models.py: Guarda los modelos de nuestros datos
- test.py: Es para pruebas
- views.py: maneja las vistas

En el archivo apps.py se crea una clase para la configuracion de la app, alli podemos configurar el nombre, que se da automaticamente al crear la app y el `verbose_name` que es el nombre que se mostrara.
```
class RockNRollConfig(AppConfig):
    name = 'rock_n_roll'
    verbose_name = "Rock ’n’ roll"
```
Para instalar la palicacion se debe hacer en el archivo settings.py en el apartado de *intalled_apps* se debe poner con el mismo nombre con que se invocó

Es buena opcion diferenciar las apps de django de las apps locales.

Las vistas que se generan dentro del modulo se importan e invocan igualmente desde el archivo urls.py.

### Tamplate system
Los Templates son la manera en que dajngo genera contenido HTML dinamico. Un template contiene la parte estatica deseada de HTML y una forma de introducir contenido dinamico a traves de  logica de programacion.

Los temples definen como se muestra la informacion que es traida por las vistas

Debemos crear una carpeta llamada `templates` dentro de nuestr app y dentre de dicha carpeta, el documento que llevara el HTML

Para usar los templates debemos importar el modulo `render` dentro de views.py
```
from django.shortcut import render
```
`render` es una funcion que toma el `request`, el nombre del `template`y el contexto, que puede ser por ejemplo, un diccionario.

```
def list_post(request):
    return render(request,'feed.html', {'posts': posts})
```
Luego en el archivo de HTML se agrega la estructura de presentacion en HTML y con logica de progrmacion el contenido que va a cambiar.
 
### Patrones de diseño
Anteriormente con la logica programacion de los datos estaba mezclada con la presentacion de los mismos, lo que generaba que muchas partes del codigo hicieran muchas cosas y se encontraran mezcladas, es un problema muy comun en como muestras los datos, como se traen los datos y como se actualizan.

Para solucionar esto estan los patrones de diseno, que son forma probadas de solucionar problemas comunes, para el desarrollo web existe el **MVC** *Model View COntroller*, que es una manera de separar los datos, la presentacion y la logica.

- Controller: Maneja la logica request y sabe que template mostrar
- Modelo: Define la estructura de los datos, el acceso y la validacion
- Vista: Como se muestran los datos

Django implementa algo similar, el **MTV** *Model Template View* 

- Modelo: Define la estructura de los datos, el acceso y la validacion
- Template: Logica de presentacion de los datos
- Vista: Trae los datos y los pasa al template

## Modelos
### La M de MTV
Para aplicar las migraciones que aparecen al momento de correr el servidor de prueba, debemos ejecutar el comando.
```
python manage.py migrate
```
Esto nos permite manejar las migraciones.

En el archivo settings.py es donde podremos manejar el engine de nuestras bases de datos, el modelo en Django define la estructura de los datos, el acceso y la validacion de los mismos, para esto usa diferentes opciones para conectarse a multiples bases de datos como MySQL, PostgreSQL o SQLite, esta ultima viene configurada por defecto.

Para crar las tablas, Django usa la tecnica ORM (Object Relational Mapper) una abstraccion del manejo de datos usando OOP, el ORM es un conjunto de clases de python que nos permiten interactuar con nuestra base de datos y definir su estructura.

Por ello para crear una tabla, la debemos crear como una clase, en la documentacion de django encontramos la informacion y las opciones de como configurar cada campo.

```
class User(models.Model):
    #User Model
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    cmodified = models.DateTimeField(auto_now=True)
```

Una vez construido el modelo, debemos enviar dichas migraciones a traves del comando
```
python manage.py makemigrations
```
Esto buscara nuestras migraciones y las reflejara en un archivo dentro de la carpeta `migrations`, luego hacemos migrate para aplicarlos.
```
python manage.py migrate
```
Cada que se modifique la tabla se deben seguir los pasos anteriores.

### El ORM de Django
Para crear registros en nuestra base de datos django usa las clases del ORM, de este modo se hace una instanciacion de la clase.
- Se debe abrir una consola de Django
```
python manage.py shell
```
-  Se importa el modelo
```
from post.models import User
```
- Se pueden hacer registros de dos formas. a traves del CREATE, una  instancia la clase, `objects` es la interfaz que nos permite crear o traer datos
```
cesar = User.objects.create(
    email='hola@gmail.com', 
    password='1234', 
    first_name='Cesar', 
    last_name='Navarro'
    )
```
O a traves de la instanciacion individual de cada campo, para guardar esto siempre se debe ejecutar la instancia `.save()`
```
julio = User()
julio.email = 'julio@email.com'
julio.password = '1234'
julio.first_name = 'Julio'
julio.last_name = 'Navarro'

julio.save()
```
- Para modificar se hace instanciando el campo y guardadno los cmabios con `.save()`
```
julio.last_name = 'Morales'

julio.save()
```
- Para borrar un registro se ejecuta la instancia `.delete()`
```
julio.delete()
```
- Para obtener un registro
```
user = User.objects.get(email ='julio@email.com)
```
### Extendiendo los modelos
Si bien los modelos pueden ser creados de manera directa, esto trae ciertas complicaciones a la hora de autenticar los registros, Django tiene modelos por defecto, que se pueden implementar para ser usados por la aplicacion.

- Para implementar los modelos que django trae por defecto debemos iniciar le shell de django e importar el modelo desde django.
```
from django.contrib.auth.models import User 
```
- Instanciamos el usuario nuevo
```
u = User.objects.create_user(username='Camilo', password='admin123')
```
### Superusuario
Admin es un modulo de django que permite administrar los usuarios de la aplicacion, se accede a traves de un superusuario.

- Para crear un super usuario
```
python manage.py createsuperuser
```

