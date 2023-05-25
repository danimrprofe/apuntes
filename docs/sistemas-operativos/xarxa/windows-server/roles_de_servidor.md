# Roles

Los roles son una forma útil y eficiente de implementar y administrar servicios en WS. Proporcionan una gran flexibilidad al permitir que los servidores sean configurados para una amplia gama de tareas.

Un **rol** es una combinación predefinida de varios servicios.

* Controlador de dominio
* Servidor DNS
* Servidor web IIS

Los roles estan formados por componentes más pequeños llamados **características**

WS puede ejecutar tantos roles como el hardware permita. Cada servidor debe tener suficiente capacidad para ejecutar los roles adecuadamente. Por lo tanto, se recomienda que cada servidor ejecute solo 1 o 2 roles. Si se requiere más capacidad, se puede considerar agregar más servidores para aumentar la capacidad.

Algunos de los roles están instalados por defecto, y otros se pueden agregar manualmente. Se pueden agregan roles y características de dos formas:

* Gráficamente mediante un asistente en la consola de administración de servidor
* Desde la consola de PowerShell
