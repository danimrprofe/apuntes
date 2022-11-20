# Introducción a mongoDB

**Mongodb** es una base de datos NoSQL que se utiliza para almacenar y recuperar datos de forma rápida y sencilla. No requiere un esquema predefinido, por lo que es ideal para aplicaciones en las que los datos pueden cambiar con frecuencia.

# Características

Se trata de una base datos NoSQL, por lo que no se realizan consultas utilizando lenguaje SQL.

Mongodb se ejecuta en un servidor y se puede acceder a él a través de una conexión de red. Los datos se almacenan en formato JSON, lo que hace que sea muy fácil de leer y escribir.

* No se definen esquemas como en las BD relacionales
* Las BD se crean en el momento que se inserta el primer registro
* No soporta joins del lado del servidor

# Cómo se guardan las cosas

* `MongoDB` permite almacenar `datos estructurados` en forma de `documentos`.
* Los `documentos` se almacenan dentro de `colecciones`, las cuales a su vez pertenecen a una `base de datos`.
* Estos documentos tienen una estructura JSON
* Los documentos se pueden comparar con los `registros` en una base de datos relacional.
* * No se definen IDs para cada documento, sino que se autogeneran cuando se introduce un documento nuevo
* Las `colecciones` se pueden comparar con las `tablas` en una base de datos relacional.
* Las `base de datos` se pueden comparar con las `bases de datos` en una base de datos relacional.

Ejemplo:

* Base de datos: `tienda`
* Colección: `productos`
* Documento: 

```json
    {
        "_id" : ObjectId("5b078ebb6f5a7f36d8916a7f"),
        "nombre" : "TV LED",
        "descripcion" : "TV LED de 50 pulgadas",
        "precio" : 500,
        "categoria" : "electronica",
        "tags" : [ 
            "tv", 
            "led"
        ]
    }
```

Permite acceder a los datos utilizando librerías javascript.

En cuanto a los documentos:

* No todos los documentos tienen porqué tener los mismos campos, por lo que se pueden agregar documentos con campos nuevos en cualquier momento.
* Los campos pueden estar anidados, por lo que un campo puede contener a su vez más de un campo.

# Instalación

Se puede descargar un instalable para Windows, y se puede instalar o no como un servicio. En función de la decisión que tomemos deberemos agregar al path las rutas a los ejecutables de MongoDB que son, principalmente:

* mongod: se trata del servicio, el engine de mongo, que gestionará la BD
* mongo: shell de mongoDB que nos permitirá comunicarnos con la BD y realizar operaciones sobre ella
