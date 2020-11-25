# Notas

Un framework es un conjunto de herramientas en un paquete que pueden ser usadas para construir aplicaciones web.

Al principio de la web todos los contenidos eran texto plano, Text-based, conforme iba creciendo, las necesidades tambien cambiaban y se hacia necesario implementar bases de datos e interfaces graficas, se hace necesario poder ejecutar scripts en el servidor a traves de requests,
esto se hace muy dificil de mantener y escalar.

Luego nacen los frameworks de desarrollo web que permiten lidiar con elementos como protocolos HTTPS, conecxiones de bases de datos e interacciones con el HTML, los templates.

Django nace en el 2003 con la necesidad de generar sitios web de manera agil y escalables y seguros. algunas de las caracteristicas de Django son:
- ORM el *Object-relational mapping* el cual nos ayuda para hacer quieries en la base de datos
- URL routing que determina la logica a seguir dependiendo de la URL de un request
- HTML templating permite definir la logica de presentacion e insertar datos dinamicos en nuestro HTML

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
    - manage.py: Es un archivo de interfaz para django-admin que nos permite ejecutar varios comandos

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

### Creacion de Apps
Una app es un modulo de python que provee un conjunto de funcionalidades relacionadas entre si. Las apps son una combinacion de modelos,vistas,urls y archivos estaticos. Las apps tienen un proposito  particular y pueden ser reutilizables. 

Un proyecto es una coleccion de configuraciones y apps para un sitio web especifico

- Para crear una app en django se utiliza la siguiente instruccion, el nombre de la app siempre deberia ser en plural
```
python manage.py startapp nombre_app
```
- Esto crea un nuevo folder con el nombre de la app, y contiene:

    - apps.py: Declara toda la configuracion especifica de nuestra app.
    - models.py: Provee la capa de datos que Django usa para construir el esquema de la base de datos y los queries.
    - admin.py: DEfine una interfaz de administrador que nos permite ver y editar la data relacionada con la app.
    - \_init_.py: Declara la app como un modulo de python.
    - views.py: Define la logica y el control de flujo para manejar los request y responses HTTP.
    - test.py: Se usa para escribir los unit tests para las funcionalidades de la app.
    - migrations: Es un modulo de python que se encarga de grabar los cambios en la base de datos.

- En el archivo `apps.py` de nuestra app se crea una clase para la configuracion de la app, alli podemos configurar el nombre, que se da automaticamente al crear la app y el `verbose_name` que es el nombre que se mostrara.
```
class RockNRollConfig(AppConfig):
    name = 'rock_n_roll'
    verbose_name = "Rock ’n’ roll"
```
- Para instalar la palicacion se debe hacer en el archivo `settings.py` en el apartado de *intalled_apps* se debe poner con el mismo nombre con que se invocó.

Es buena opcion diferenciar las apps de django de las apps locales.

- Las vistas que se generan dentro del modulo se importan e invocan igualmente desde el archivo urls.py.

### Patrones de diseño
Cuando trabajamos con Frameworks de desarrollo debemos conocer como es la estructura o arquitectura que subyace.

Anteriormente con la logica programacion de los datos se mezclaban con la presentacion de los mismos, lo que generaba que muchas partes del codigo hicieran muchas cosas y se encontraran mezcladas, es un problema muy comun en como muestras los datos, como se traen los datos y como se actualizan.

Para solucionar esto estan los patrones de diseño, que son formas probadas de solucionar problemas comunes, para el desarrollo web existe el **MVC** *Model View COntroller*, que es una manera de separar los datos, la presentacion y la logica.

- Model: Define la estructura de los datos, el acceso y la validacion
- View: Como se muestran los datos
- Controller: Maneja la logica request y sabe que template mostrar

Django implementa algo similar, el **MTV** *Model Template View* y tiene cuatro elementos clave.

- Cuando la app de Django recibe una peticion web, usa el patron de URL para decidir a que vista debe para manaejarlo, esta recibe el *HTTP request* como un argumento y devuelve el *HTTP response* al servidor web para ser devuelto, El modelo define como se estructuran los datos y las consultas y la informacion es mostrada por los templates.

- URL patterns: Define que view mostrar segun el web request
- Model: Define la estructura de los datos, el acceso y la validacion
- Template: Logica de presentacion de los datos
- View: Trae los datos y los pasa al template

## Models
Los modelos crean la capa de datos de la aplicacion de Django, define la estructura de la base de datos y como se guardaran.
Tambien permiten hacer consultas e implementar el ORM (*Object Relational Mapper*) de Django.

Podemos conceptualizar los modelos como una tabla en una hoja de calculo cada campo es una columna y cada registro una fila.

Para crear las tablas, Django usa la tecnica ORM, una abstraccion del manejo de datos usando OOP, el ORM es un conjunto de clases de python que nos permiten interactuar con nuestra base de datos y definir su estructura.

Un modelo es una clase heredada de django.db.models.Model y define los campos de la base de datos y sus atributos.

### Tipos de campos mas usados
Textual data
- `CharField` Tipo caracter, debe tener siempre un atributo `max_length`.
- `TextField` Tipo caracter, sin longitud de texto limitada.
- `EmailField` Tipo caracter, para direccion de correo.
- `URLField` Tipo caracter, para direccion de sitios WEB.

Numeric data
- `IntegerField` Tipo numerico, para numeros enteros.
- `DecimalField` Tipo numerico, para numeros decimales.

Miscellaneous data
- `BooleanField` Tipo logico, para valores booleanos.
- `DateTimeField` Tipo fecha, para valores de hora y fecha.

Relational data
- `ForeignKey` Para relacionar un solo registro de un modelo con otro modelo.
- `ManyToMany` Para relacionar varios modelos con otros

### Atributos 
Los campos pueden tener varios atributos.
- `max_length=n` Longitud maxima del campo = n
- `blank=True/False` Si el campo puede ser, no requerido por defecto.
- `null=True/False` Es campo puede estar nulo
- `choices` Limita las opciones del campo por unas predefinidas

### Crear tablas
Para crear una tabla, la debemos crear como una clase, en la documentacion de django encontramos la informacion y las opciones de como configurar cada campo.

- Primero debemos importar `models` del modulo de `django.db`
```
from django.db import models
```
- Creamos nuestro modelo como una clase que hereda de `model.Models`.
```
class User(models.Model):
    #User Model
    GENDER_CHOICES=[('M', 'Male'), ('F', 'Female')]
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    cmodified = models.DateTimeField(auto_now=True)
```
Para poner una relacion se debe hacer un campo de relacion
```
    relation = models.ManyToManyField('modelo_relacionado')
```
En los campos integer el valor de *blank* es tomado como 0.

- Una vez construido el modelo, debemos enviar dichas migraciones a traves del comando
```
python manage.py makemigrations
```
Esto buscara nuestras migraciones y las reflejara en un archivo dentro de la carpeta `migrations`, luego hacemos migrate para aplicarlos.
```
python manage.py migrate
```
Cada que se modifique la tabla se deben seguir los pasos anteriores.


### Admin
El admin de Django nos permite crear un a interface administrativa para administar los datos de nuestra aplicación.

- Para acceder a dicho modulo debemos ingredar al archivo `admin.py` dentro de nuestra aplicacion e importar el modelo.
```
from .models import profile
```
- Para hacer una interfaz de nuestro modelo devemos crear una clase y heredar el modelo de admin.
```
class profileAdmin(admin.ModelAdmin):
    pass
```
Esta clase puede tomar varios atributos para cambiar su comportamiento
- Debemos registrar esta clase con el admin para definir el modelo con el que esta asociado. Para esto usamos le decorador `register`
```
@admin.register(Profile)
```
## Superusuario
Admin es un modulo de django que permite administrar los usuarios de la aplicacion, se accede a traves de un superusuario.

- Para crear un super usuario
```
python manage.py createsuperuser
```
- Definimos nuestro nombre de usuario, correo y contrasena
- Luego corremos el servidor y vamos a la ruta `/admin`

## Admin UI
El admin UI nos muestra nuestros modelos registrados, al acceder a ellos, encontramos cada uno de los registros, sus campos y valores.
Los registros son mostrados como objetos, esto no es muy util para administrarlos por lo que debemos configurar como deseamos verlos.

- Primero  importamos nuestro modelo
```
from users.models import Profile
```
- luego lo registramos en el admin
```
admin.site.register(Profile)
```
- Vamos al archivo `admin.py`, en la clase que estamos usando para registrarlos debemos poner el atributo `list_display` que nos permite definir los campos que deseamos ver.
```
class profileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
```
- Tambien podemos definir que campos nos serviran como link para llevarnos al usuario, o que campos son editables desde el admin. Un campo no puede ser link y editable.
```
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user','prof_register','picture']
    list_display_links = ('pk', 'prof_register',)
    list_editable = ('picture',)
```
Tambien podemos agregar una opcion de busqueda. Para acceder a los campos de user debemos invocarlos como `user__fist_name`
```
search_fields = ('user__fist_name', 'user__last_name', )
```
Cuando django muestra una instancia de modelo en el admin o la consola, por defecto solo usa el nombre del modelo, la palabra *object* y el id del campo.

- Para cambiar este metodo debemos ir ala archivo `models.py` de la aplicacion y dentro del modelo usar el siguiente sobreescribir el metodos.
```
def __str__(self):
    return self.first_name
```
Asi le decimos cual campo deseamos ver por defecto y como un string.

### Consultas con el ORM de Django

Para crear registros en nuestra base de datos django usa las clases del ORM, de este modo se hace una instanciacion de la clase.

- Para iniciar abrimos una consola de Django
```
python manage.py shell
```
-  Se importa el modelo para poder hacer las consultas
```
from post.models import User
```
El modelo de Django tiene un atributo llamado `Objects` con varios metodos.

#### Metodo .all
- Para obtener todas las instancias del modelo
```
User.objects.all
```
- Lo asignamos a una variable para poder trabajar con los resultados en forma de lista
```
users = User.objects.all()
```
- Para acceder a algun registro invocamos su indice
```
user = users[0]
```
- Ahora podemos acceder a cualquier campo de dicho registro.
```
user.name
```
Djanog siempre asing un campo Id a todos los registros y se puede acceder a el a traves de `.id`

#### metodo .get
- Podemos consultar una sola instancia atraves del metodo `.get` y consultar algun campo.
```
user = User.objects.get(email ='julio@email.com)
user.name
```
- El metodo get funciona para los datos unicos, pues cuando se ingresa un campo que no existe, o que pertence a varios registros genera un error.
- Para consultar datos relacionados
```
user.relacion.all()
```
#### metodo .create
- Se pueden hacer registros de dos formas. a traves del `.create`, una  instancia la clase, `objects` es la interfaz que nos permite crear o traer datos
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
## Extendiendo los modelos

Si bien los modelos pueden ser creados de manera directa, esto trae ciertas complicaciones a la hora de autenticar los registros, Django tiene modelos por defecto, que se pueden implementar para ser usados por la aplicacion.

- Para implementar los modelos que django trae por defecto debemos iniciar el shell de django e importar el modelo desde django.
```
from django.contrib.auth.models import User 
```
- Instanciamos el usuario nuevo
```
u = User.objects.create_user(username='Camilo', password='admin123')
```

### Modelo de usuarios
Django nos permite dos acciones para implementar su modelo de usuarios y extender su funcionalidad, por un lado, el modelo proxy, y por otro, extender la clase de usuario. ya existente.

#### Modelo Proxy
El modelo proxy nos permite extender la funcionalidad de algun modelo

- Para ello debemos importar el modelo desde django en nuestro `models.py` de la aplicacion.
```
from django.contrib.auth.models import User
``` 
- Instanciar la clase y crear los campos adicionales que deseemos.
```
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
```
`on_delete` es un campo obligatorio para cualquier campo relacional.

## Manejadores de URL y Vistas
Los patrones de URL son la primer parte del codigo de una aplicacion, en un nivel general, ellos deciden que vista debe manejar las peticiones.

En el archivo `urls.py` del proyecto tenemos una variable llamada `urlpatterns` y dentro de ella una lista de llamdos a la funcion  `path`

- Cuando llega una peticion django evalua cada deficion de `path` en orden de arriba a abajo y verifica que el primer argumento coincida con la peticion.
- Si coincide con la peticion, se pasa al segundo argumento, si no coincide, continua con la siguiente definicion, si no hay una coincidencia django retorna un error *404*.

### Estructura de un URL pattern

Los path se componene de tres elementos

- `path converter`: Un string que define que pattern se esta buscando.
- `view`: La vista que intentamos usar para este pattern
- `name`: Un nombre opcional que resulta util en los templates, e suna buena practica usarlos siempre.

#### Path converters
El path converter debe emparejar literalmente, por lo tanto la ruta debe iniciar con el nombre del `path converter`, todo lo que este dentro de los parentesis angulares indica un grupo de captura, esto puede coincidir con diferentes cadenas y es tratado como una variable.

Antes de `:` va un convertidor de tipo, lo que indica que estamos esperando un argumento de un tipo especifico, despues va el nombre dle argumento, y es como queremos llamarle a la varibale resultante.
`<tipo_dato:nombre_argumento>`, por ejemplo `<string:first_name>`
```
```
## Implementar URL Patterns
Para implementar los patrones de URL debemos ir a el archivo `urls.py`

- Debemos importar nuestras vistas de modulos, para poder referenciarlas en nuestros patrones
```
from users import views
```
- Luego iremos implementando nuestras url, comenzando por la url raiz, que sera el home.
```
path('', views.home, name='home'),
```
- Luego podemos poner uno para cada usuario.
```
path('user/<str:user_name>/', views.user_detail, name='user_detail')
```
Asi que si alguien visita users/cesar el request lo enrutara a la funcion user_detail

### HttpResponse
El httpResponse es una clase de django que nos permite devolver un objeto response de manera facil, sin tener que usar el `render`, pues este ultimo usa los `templates` para renderizar la informacion.

- Vamos a las `views` de nuestra aplicacion e importamos la clase `httpResponse` desde django para escribir una respuesta http.
```
from django.http import HttpResponse
```
Esta clase construye el objeto response que deseamos que la vista retorne
- Una vista puede ser una función o una clase que retorna un valor.
- Todas las vistas reciben un `request` y regresan una instancia de la clase `HTTpResponse` con el contenido deseado

```
def home(request):
    return HttpResponse('<p>Hola mundo</p>')

def user_detail(request, first_name):
    return HttpResponse(f'<p>user_detail visto con el id {first_name}</p>')
```
Los paths reciben el path al que van a responder y la vista que van a devolver.

```
path('home/',home)
```

## Tamplate system
Los Templates son la manera en que dajngo genera contenido HTML dinamico. Un template contiene la parte estatica deseada de HTML y una forma de introducir contenido dinamico a traves de  logica de programacion.

Cuando una vista llama la funcion `render`, esta pasa datos dentro del template, los temples definen como se muestra la informacion que es traida por las vistas.

La sintaxis de un template en django se compone de tres elementos:

- `{{ variable }}` el valor de la varible se muestra cuando se encierra en doble llaves
```
<h3>{{ user.first_name }}</h3>
```
-  `{% tag %}` La etiqueta de plantilla se usa para if's, for's y estructuras de control logico. Siempre se deben cerrar las estructuras de control.
```
{% for user in users %}
    <li>{{ user.first_name }}</li>
{% endfor %}
```
Algunas etiquetas de plantilla no se cierran y solo renderiza un string.

- `{{ variable|filter }}` Una variable puede tener un filtro de template, que toma un string como entrada y regresa un string como salida. Es usualmente usada para tomar un string y cambiar algun formato.
```
<ul>
    {% for user in users %}
        <li>
            <a href="{{ user.first_name }}">
                {{ user.first_name|capfirst }}
            </a>
        </li>
    {% endfor %}
</ul>
```
### Herencia de templates
Para reducir la repeticion Django implementa un *base template* que contiene todos los elementos comunes a cada template como los metadatos, o elementos globales de CSS o JavaScript.

- Para hacer esto se debe contar con un archivo .HTML que sirva de base y extender el contendio desde el mismo.
```
{% extends "base.html" %}
```
- Luego poner el contendio que vamos a extender entre *block tags*
```
{% block content %}
    <p> content </p>
{% endblock content %}
```
### Creacion de Templates
- Debemos crear una carpeta llamada `templates` en nuestro proyecto y dentro de dicha carpeta, el documento que llevara el HTML.

- Posterior a esto en el archivo `settings.py` debemos decirle a django como encontrar los templates, modificamos el apartado *DIRS* de *TEMPLATES*.
```
'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
``` 

Para usar los templates debemos importar el modulo `render` dentro de views.py
```
from django.shortcut import render
```
`render` es una funcion que toma el `request`, el nombre del `template`y el contexto, que puede ser por ejemplo, un diccionario.

```
def list_post(request):
    return render(request,'feed.html', {'posts': posts})
```
Luego en el archivo de HTML se agrega la estructura de presentación en HTML y con logica de progrmacion el contenido que va a cambiar.
 

### La M de MTV
Para aplicar las migraciones que aparecen al momento de correr el servidor de prueba, debemos ejecutar el comando.
```
python manage.py migrate
```
Esto nos permite manejar las migraciones.

En el archivo settings.py es donde podremos manejar el engine de nuestras bases de datos, el modelo en Django define la estructura de los datos, el acceso y la validacion de los mismos, para esto usa diferentes opciones para conectarse a multiples bases de datos como MySQL, PostgreSQL o SQLite, esta ultima viene configurada por defecto.


