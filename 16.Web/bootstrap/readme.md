
## 1. ¿Qué es Bootstrap?

Bootstrap es un **framework** de código abierto que facilita el desarrollo de sitios web y aplicaciones
web modernas. Fue creado por Twitter y proporciona una colección de herramientas CSS,
JavaScript y HTML que permiten diseñar interfaces de usuario de manera rápida y eficiente.

Características principales:

- Sistema de cuadrícula (grid) responsiva.
- Componentes predefinidos como botones, formularios, barras de navegación, etc.
- Interactividad mediante plugins de JavaScript.

##  2. Cómo Incluir Bootstrap en tu Proyecto

Creamos una archivo index.html en la carpeta raiz. Incluiremos la etiqueta `<meta name="viewport">` para que la página tenga comportamiento responsivo en dispositivos móviles.

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
  </head>
  <body>
    <h1>Hello, world!</h1>
  </body>
</html>
```

A continuación añadimos los enlaces para CSS y código javascript de Bootstrap:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
  </head>
  <body>
    <h1>Hello, world!</h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
  </body>
</html>
```

## 3. Sistema de Cuadrícula (Grid System)

El sistema de cuadrícula de Bootstrap se basa en una estructura de 12 columnas, lo que facilita
crear diseños flexibles y responsivos. Se usan clases de CSS como row y col .

Clases Responsivas: Puedes ajustar las columnas para diferentes tamaños de pantalla
utilizando clases como col-sm-* , col-md-* , col-lg-* , donde * es el número de columnas.

## 4. Componentes de Bootstrap

Bootstrap ofrece una amplia gama de componentes predefinidos que puedes utilizar sin necesidad
de diseñarlos desde cero. Algunos de los más comunes son:
Botones: Utiliza la clase btn para crear botones estilizados.

Barra de navegación: Un componente clave para la navegación de tu sitio.

Cards: Una manera fácil de mostrar contenido en cajas.

## 5. Utilidades de Bootstrap

Bootstrap también ofrece una serie de clases utilitarias que permiten aplicar estilos rápidos sin
necesidad de CSS personalizado. Algunas de las más utilizadas son:

html
<div class="container"> <div class="row"> <div class="col-md-6">Columna 1 (50%)</div>
<div class="col-md-6">Columna 2 (50%)</div> </div> </div>

Copiar código

html

<button class="btn btn-primary">Botón Azul</button> <button class="btn btn-
danger">Botón Rojo</button>

Copiar código

html
<nav class="navbar navbar-expand-lg navbar-light bg-light"> <a class="navbar-brand"
href="#">Mi Sitio</a> </nav>



```html
<div class="card" style="width: 18rem;">
 <div class="card-body">
 <h5 class="card-title">Título de la Tarjeta</h5>
 <p class="card-text">Texto de ejemplo dentro de una tarjeta de Bootstrap.</p> <a href="#" class="btn btn-primary">Ir a algún lugar</a>
</div>
</div>
```

Copiar código

18/9/24, 19:06 ChatGPT

https://chatgpt.com/c/66eb04f9-12f8-8005-a92c-98e7e8332be1 2/3

Margen y Padding: Usa las clases m- y p- seguidas de un número del 0 al 5 para ajustar el
margen y el relleno.

Texto y Alineación: Clases como text-center , text-left o text-right permiten alinear el
texto fácilmente.