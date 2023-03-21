[🔙 Enrere](../) | [🏠 Pàgina principal](http://danimrprofe.github.io/apuntes/)

# Expresiones regulares

Las **expresiones regulares**, también llamadas **regex** son un lenguaje de patrones utilizado para coincidir con cadenas de texto. Se utilizan a menudo para validar formularios de entrada, buscar y reemplazar texto y para realizar tareas similares de procesamiento de texto.

Las expresiones regulares se basan en un conjunto de **reglas** para la construcción de **patrones** de cadenas de texto.

Estos patrones se pueden utilizar para buscar **coincidencias** con cadenas de texto en un documento o para verificar si una cadena de texto cumple con un patrón determinado. Las expresiones regulares se pueden utilizar en muchos lenguajes de programación y herramientas de línea de comandos, como **grep** y **sed**.

## Ejemplo

En este ejemplo vamos a buscar todas las etiquetas `<img>` en varios archivos para reemplazarlas por formato markdown.

```bash
<img[^>]*src="([^"]+)"[^>]*>
```

Podremos reutilizar en la parte de reemplazar el argumento $1 que contendrá la ruta de la imagen

```bash
![imagen]($1)
```