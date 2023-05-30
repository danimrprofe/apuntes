# Terraform

Terraform es una herramienta de infraestructura como código (IaC) desarrollada por HashiCorp. Está diseñada para permitir que los usuarios **describan** y predecir la infraestructura de una nube a través de un lenguaje de configuración declarativo.

## Ventajas para el desarrollo

Por ejemplo, usando Terraform podemos crear una infraestructura que se puede compartir con otros usuarios. Esto permite que los **equipos de desarrollo** puedan versionar y compartir los cambios hechos a la
infraestructura, lo cual facilita la colaboración.

## Ventajas para los devOps

Esto también permite que los equipos de **DevOps** puedan realizar cambios y actualizaciones en la infraestructura de manera rápida y sencilla.

## Infraestructura habitual

Una infraestructura moderna normalmente utiliza:

* Múltiples proveedores (AWS, Google Cloud, Digital Ocean,etc)
* Combinado con servicios externos: DNS, mail, monitorización, etc.

Cada proveedor utiliza sus propias herramientas.

## Con terraform

Terraform permite manejarlas todas desde un solo sitio, mediante código. Esto significa que los usuarios pueden crear, modificar y destruir recursos de nube con un código de configuración, que se puede almacenar en un repositorio de control de código como GitHub.

Por ejemplo, podemos:

* Crear máquinas en dos proveedores IaaS diferentes
* Registrar nombres en un proveedor de DNS
* Monitorizar en una compañía third-party
* Configurar una cuenta empresarial de Github y enviar logs de aplicación a un servicio apropiado.

Podemos, además, **delegar** las configuraciones a herramientas como **Chef**, **puppet**, y otras.

El estado de la infraestructura se puede describir, guardar, versionar y compartir.