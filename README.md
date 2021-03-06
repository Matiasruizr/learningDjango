# learningDjango

Al inicio de la web todo era texto plano (HTML), con el tiempo se necesitaban cosas más complejas ahi nace CGIscript con el objetivo de que a través de un request, se ejecute un script dentro del servidor, pero esto fue generando problemas con la escabilidad.y por ende difícil de mantener, de esta necesidad nace PHP.

Luego nacen los frameworks para poder resolver tareas comunes, como:
  Protocolos HTTP.
  Conexiones a bases de datos.
  Interacciones con el HTML(templates).
  Django
  Nace en 2003, con la necesidad de hacer web’s con la filosofía de hacer las cosas de manera agíl.

Poder hacer sitios escalables.
URLs bien diseñadas.
HTTP request y responses.
-ORM, que es conectar a na DB a traves de una interfaz python.

# Características.
  Rápido desarrollo.
  Listo para todo.
  Seguro contra ataques.
  Versátil.
  
  
 # Ventajas
  Es desarrollado en Python.
  -DRY(Don’t repeat yourself).
  Comunidad Open Source.
  
  CGI Scripts Common Gateway Interface (Interfaz de entrada común).
ORM Object-Relational mapping (Mapeo objeto relacional).


Estructura de Archivos:

El archivo vacío init.py indica que la carpeta es un módulo de python.
El archivo settings.py define todas las configuraciones del proyecto.
BASE_DIR: Define la ubicación donde se está corriendo el proyecto.
SECRET_KEY: Es usado para el hashing de las contraseñas y las sesiones que se almacenan en la BD.
DEBUG: Define si el proyecto está en desarrollo para realizar debugging.
ALLOWED_HOSTS: Define que hosts están permitidos para que interactuen en nuestro proyecto.
INSTALLED_APPS: Aplicaciones ligadas al proyecto. Por defecto agrega la app de administrador, autenticación, contentypes (conexión a la BD), sesiones, mensajes y archivos estáticos.
MIDDLEWARE:
ROOT_URLCONF: Ubicación del principal de urls.
TEMPLATES:
WSGI_APPLICATION: Ubicación del principal de deployment.
DATABASES: Configuración y conexión a la BD.
AUTH_PASSWORD_VALIDATORS: Validadores de contraseñas. Si se está usando la app de autenticación, que la contraseña pase por las validaciones definidas:
Los valores de la contraseña no sean similares a los valores del usuario.
Que tenga una mínima longitud.
Validar la contraseña con un diccionario de contraseñas comunes.
Que la contraseña no sea numérica.
LANGUAGE_CODE: Lenguaje o idioma que está utilizando la aplicación.
TIME_ZONE: Se define el sistema horario en donde está corriendo la aplicación.
USE_I18N: Librería para traducción de textos.
USE_L10N: Librería para traducción de textos.
USE_TZ: Librería de timezone.
STATIC_URL: Define la ubicación de los archivos estáticos como css, js, img.
El archivo urls.py define el punto de entrada para todas las peticiones que lleguen al proyecto.
El archivo wsgi.py es utilizado para el deployment a producción.
El archivo manage.py es uno que no se debe tocar y permite ejecutar todos los comandos que se hayan definido en las applicaciones instaladas del proyecto (entre ellas las del comando django-admin).
Cuando se ejecuta python3 manage.py por cada [nombre_app] se visualizarán los diferentes comandos que se pueden ejecutar por cada aplicación instalada del proyecto (auth, contenttypes, django, sessions, staticfiles).

# Entonces, que es Django?
Es una interfaz para conectar URL con lógica, usando python

# Creando una primera aplicación en Django
Creamos un proyecto con django-admin 
Para crear una primera App en Django, podemos crearla usando python manage.py startapp nombreapp
Podemos iniciar un proyecto con python manage.py runserver


# Trabajando con APIS
  Para trabajar con api importamos json
    import json
  
  creamos una variable como la siguiente, a la cual podemos pasar variables, o arrays

     data = {
          'status' : 'ok',
          'numbers': numbers,
          'message': 'Integers sorted succesfully.'
      }
    
   Finalmente desde la respuesta transformamos esta "data" en json con json.dumps y mostramos esto como contenido tipo 'apllication/json'
   
       return HttpResponse( json.dumps(data, indent= 4), content_type='application/json')
       
       
   # Template system
   Podemos utilizar html con python incrustado:
   simplemente en un proyecto creamos la carpeta templates y agregamos el html
   desde nuestras vistas tenemos que retornar el template! y pasarle por ese mismo return render() todos las variables, listas, etc que utilizemos en esa vista.
   Ejemplo:
      return render(request,'feed.html', {'posts': posts})
      
   Para usar codigo python en este html simplemente escribimos {% %}
   Y en caso de imprimir un valor {{ }}
   
   # MTV => MVC:
   Django utiliza un patron de diseño llamado MTV
    Views + Urls => Controller
    Templates => View
    Models => Model
          **Patrones de diseño: Solucion reutilizable a un problema comun **
   
   
   # Conectar a BDD
     DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'mydatabase',
          'USER': 'mydatabaseuser',
          'PASSWORD': 'mypassword',
          'HOST': '127.0.0.1',
          'PORT': '5432',
      }
  }
  https://docs.djangoproject.com/en/2.0/ref/settings/#databases
  
  # Crear un Modelo
    class User(models.Model):
      email = models.EmailField()
      password = models.CharField()

      first_name =  models.CharField()
      last_name =  models.CharField()

      bio =  models.TextField()

      birthdate =  models.DateField()

      create = models.DateTimeField()
      modified = models.DateTimeField()
      
  
  Referencias tipos de datos https://docs.djangoproject.com/en/2.0/ref/models/fields/
  
  Creamos la migracion con python manage.py makemigrations
  Aplicamos la migracion con python manage.py migrate
  
  # ORM
  Podemos crear objetos y manejar datos desde el sheell de django:
  python manage.py shell
  
  
  Podemos instanciar una clase
    matias = User()
    matias.first_name = 'Matias'
    matias.last_name = 'Ruiz'
    matias.save() ** Sin esto no queda guardado en la BdD!
  
  Consultas frecuentes con ORM:
  https://docs.djangoproject.com/en/2.0/topics/db/queries/
  
  
  
  
  
  
 # Glosario
 Glosario
ORM: Object-relational mapping. Es el encargado de permitir
el acceso y control de una base de datos relacional a través de
una abstracción a clases y objetos.

Templates: Archivos HTML que permiten la inclusión y ejecución
de lógica especial para la presentación de datos.

Modelo: Parte de un proyecto de Django que se encarga de estructurar
las tablas y propiedades de la base de datos a través de clases de Python.

Vista: Parte de un proyecto de Django que se encarga de la
lógica de negocio y es la conexión entre el template y el modelo.

App: Conjunto de código que se encarga de resolver una parte
muy específica del proyecto, contiene sus modelos, vistas, urls, etc.

Patrón de diseño: Solución común a un problema particular.


# Admin de Python
Creamos un usuario con python manage.py createsuperuser

Ahora accedemos desde url/admin/ con las credenciales creadas anteriormente
  
