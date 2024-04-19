[🔙 Enrere](../) | [🏠 Pàgina principal](http://danimrprofe.github.io/apuntes/)

# kubernetes

Kubernetes permite definir y desplegar aplicaciones en contenedores de manera **automatizada**, gestionando la escalabilidad, el balanceo de carga, la recuperación ante fallos y la actualización de las aplicaciones.

## ¿Cómo se utiliza?

Para utilizar Kubernetes, se define un ``archivo de configuración`` (o varios archivos) que describe el estado deseado del sistema. Este archivo incluye información sobre los contenedores que se van a ejecutar, las políticas de escalado, la configuración de red, etc. Luego, Kubernetes se encarga de hacer que la infraestructura se ajuste al estado deseado.

A k8s le puedo escribir en un archivo **YAML**:

- Qué imágenes de docker quiero que coja
- Decirle que quiero 10 contenedores de estos, 5 de estos, y 3 de estos.
- Le digo que tengo 30 nodos (máquinas) a su disposición
- Le pido que ejecute todos los contenedores
- Él los distribuye sobre los nodos del cluster
- Se asegurará de que habrá el número que yo le diga de contenedores en marcha
- Puedo asignar recursos a los contenedores y hacer que se asegure que tiene los recursos que necesita.

## ¿Dónde se ejecuta?

Kubernetes se puede ejecutar en uno o más clouds, y puede gestionar los recursos de infraestructura de varias nubes al mismo tiempo. Además, Kubernetes es altamente escalable y se puede utilizar para gestionar infraestructuras pequeñas o grandes. También es altamente flexible y se puede integrar con otras herramientas y sistemas, lo que permite una gran variedad de casos de uso.

Con **Docker-compose** puedo desplegar varios contenedores sobre el mismo nodo
creando servicios.

Añade un nivel de abstracción más por encima de Docker.

## Nodos

Los nodos ``master`` son responsables de gestionar y coordinar la ejecución de los contenedores en los nodos ``worker`` o ``minions``. Los nodos ``worker`` son los encargados de ejecutar los contenedores y proporcionar la capacidad de cómputo para las aplicaciones que se ejecutan en ellos.

Los nodos pueden ser instancias EC2 de Amazon Web Services o Google Compute Instances de Google Cloud Platform, u otras opciones de proveedores de servicios en la nube o de infraestructura local.

## Minikube

**Minikube** es una herramienta que facilita la ejecución local de Kubernetes. Minikube ejecuta un clúster Kubernetes de un solo nodo dentro de una máquina virtual.

Proporciona una solución sencilla para usuarios que desean probar Kubernetes o desarrollar soluciones sobre él.
