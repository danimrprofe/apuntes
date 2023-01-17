# MongoDB

## Introducción

**Mongodb** es una base de datos NoSQL que se utiliza para almacenar y recuperar datos de forma rápida y sencilla. No requiere un esquema predefinido, por lo que es ideal para aplicaciones en las que los datos pueden cambiar con frecuencia.

## Características

NoSQL se ha convertido en una de las principales opciones para los desarrolladores que buscan una base de datos **flexible** y **escalable**.

Esto se debe a algunas características únicas que ofrece NoSQL, como un diseño sin esquemas, una mayor escalabilidad y una mejor capacidad de respuesta.

En primer lugar, una base de datos NoSQL **no requiere un esquema** predefinido para almacenar los datos. Esto significa que los desarrolladores pueden agregar nuevos campos a un documento sin tener que redefinir el esquema de la base de datos. Esto facilita la creación de aplicaciones en las que los requisitos de datos cambian constantemente.

Además, la escalabilidad es una de las principales ventajas de NoSQL. Esto se debe a que la base de datos se distribuye en varios servidores, lo que permite a los desarrolladores escalar la capacidad de almacenamiento y procesamiento de datos de forma sencilla. Esto significa que una base de datos NoSQL puede crecer sin afectar el rendimiento.

Por último, una base de datos NoSQL también ofrece una mejor capacidad de respuesta. Esto se debe a que los datos se almacenan en formato JSON, lo que hace que sea muy fácil de leer y escribir. Esto significa que los datos se pueden recuperar y almacenar de forma más rápida, lo que mejora el rendimiento de la aplicación.

## Cómo se guardan las cosas

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

## Instalación

Se puede descargar un instalable para Windows, y se puede instalar o no como un servicio. En función de la decisión que tomemos deberemos agregar al path las rutas a los ejecutables de MongoDB que son, principalmente:

* mongod: se trata del servicio, el engine de mongo, que gestionará la BD
* mongo: shell de mongoDB que nos permitirá comunicarnos con la BD y realizar operaciones sobre ella
