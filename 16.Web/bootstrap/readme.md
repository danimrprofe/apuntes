
- [Bootstrap](#bootstrap)
  - [1. ¿Qué es Bootstrap?](#1-qué-es-bootstrap)
  - [2. Cómo Incluir Bootstrap en tu Proyecto](#2-cómo-incluir-bootstrap-en-tu-proyecto)
  - [3. Clases en Bootstrap](#3-clases-en-bootstrap)
  - [4. Sistema de Cuadrícula (Grid System)](#4-sistema-de-cuadrícula-grid-system)
  - [5. Margin i Padding](#5-margin-i-padding)
  - [6. Text i Alineació](#6-text-i-alineació)
  - [7. Componentes Bootstrap](#7-componentes-bootstrap)
  - [8. Componente card](#8-componente-card)
  - [9. Componente nav](#9-componente-nav)
  - [10. Componente carroussel](#10-componente-carroussel)

# Bootstrap

![](img/2024-10-05-18-49-26.png)

## 1. ¿Qué es Bootstrap?

Bootstrap es un **framework** de código abierto que facilita el desarrollo de sitios web y aplicaciones
web modernas. Fue creado por Twitter y proporciona una colección de herramientas CSS,
JavaScript y HTML que permiten diseñar interfaces de usuario de manera rápida y eficiente.

Características principales:

- Sistema de cuadrícula (grid) responsiva.
- Componentes predefinidos como botones, formularios, barras de navegación, etc.
- Interactividad mediante plugins de JavaScript.

##  2. Cómo Incluir Bootstrap en tu Proyecto

Para que todas las caracterísitcas de Bootstrap funcionen, a nuestras páginas web les tendremos que agregar las etiquetas necesarias.

**1) Etiqueta meta viewport**

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

**2) Etiquetas de enlace CSS y Javascript**

A continuación añadimos los enlaces para CSS y código javascript de Bootstrap.

El enlace CSS hará referencia a la hoja de estilos de bootstrap.

```html
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
```

El enlace JS hará referencia al script Javascript de bootstrap. Lo podemos insertar eh `head` o bien al final del `body`.

```html
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
```

Así quedaría una página de ejemplo:

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

A partir de aquí, nuestra página adoptará ya ciertos estilos de bootstrap, como la fuente de letra del texto, entre otros.

Para todo lo demás, tendremos que incluir los códigos necesarios en los diferentes elementos de nuestra página.

## 3. Clases en Bootstrap

En Bootstrap, las ``clases predefinidas`` juegan un papel crucial para aplicar estilos de forma rápida y consistente. A menudo se usan en lugar de escribir estilos CSS personalizados, lo que acelera el proceso de desarrollo y asegura que el diseño sea consistente y responsivo.

Ejemplos:

```html
<div class="p-3">Contenido con padding</div>
<div class="col-sm-6 col-md-4">Columna</div>
```

Estos nombres de clases están definidos en Bootstrap, y podemos usarlos incluyéndolos en el ``atributo class ``de un elemento HTML.

**Combinación de clases**

En Bootstrap, puedes combinar varias clases en un solo elemento HTML para aplicar múltiples estilos o comportamientos de diseño.

En este ejemplo, se usan 3 clases sobre la misma capa:

```html
<div class="bg-warning p-3 m-4">
  Este es un bloque con fondo de advertencia, padding y margen.
</div>
```

Explicación de las clases:

- ``bg-warning``: Aplica un fondo de color de advertencia (amarillo).
- ``p-3``: Añade un padding (relleno) de 1rem alrededor del contenido.
- ``m-4``: Añade un margen de 1.5rem alrededor del bloque.

## 4. Sistema de Cuadrícula (Grid System)

El **sistema de cuadrícula** de Bootstrap se basa en una estructura de 12 columnas, lo que facilita crear diseños flexibles y responsivos.

En resumen, disponemos de 12 columnas que podemos repartir entre capas, con la condición de que sumen 12, con cualquier combinación posible.

Se usan clases de CSS como row y col .

**Ejemplo de una fila con dos columnas de igual ancho**

Aquí no aparece toda la página web, por lo que todo lo que a continuación aparece deberá estar dentro del `body` de nuestra página web.

- La capa container (o container-fluid) es necesaria para que bootstrap funcione.
- Dentro de ella, la capa con clase ``row`` actuará como contenedor de fila.
- Dentro de ella, dos columnas de igual ancho (6+6 = 12).

Estas columnas quedarán una al lado de la otra, con igual ancho. A partir de cierto ancho de pantalla, una pasará a colocarse debajo de la otra. Esto es un comportamiento ``responsivo``, que responde a las características de la pantalla en la que se está visualizando la página web. Esta característica se llama ``responsive design``, y viene incorporada en Bootstap.

```html
<div class="container">
  <div class="row">
    <div class="col-md-6">Columna 1 (50%)</div>
    <div class="col-md-6">Columna 2 (50%)</div>
  </div>
</div>
```

Podemos ajustar las columnas para diferentes tamaños de pantalla
utilizando clases como ``col-sm-* , col-md-* , col-lg-* ``, donde * es el número de columnas.

Las letras  ``sm, md o lg`` hacen referencia al punto de ancho a partir del cual cambia la disposición de las capas.

## 5. Margin i Padding

Bootstrap 5 proporciona classes per ajustar fàcilment el **marge** (m-) i el **farcment** o *padding* (p-). Les classes es basen en un sistema de nombres del 0 al 5, on cada número representa un increment del marge o del *padding* en unitats relatives.

- **m-**: ajusta el marge extern.
- **p-**: ajusta el *padding* o marge intern.

Exemples:

- `m-0`: sense marge.
- `m-3`: marge moderat.
- `m-5`: marge màxim.

A més, pots ajustar els marges o *padding* de maneres específiques per a cada costat:
- **m(t/b/l/r/x/y)**: per ajustar només la part superior (**t**), inferior (**b**), esquerra (**l**), dreta (**r**), horitzontal (**x**) o vertical (**y**).

Exemples:
- `mt-3`: marge només a la part superior.
- `px-4`: *padding* horitzontal (esquerra i dreta).

## 6. Text i Alineació

Bootstrap ofereix classes per ajustar fàcilment l'alineació del text:

- **text-left**: alinea el text a l'esquerra.
- **text-center**: alinea el text al centre.
- **text-right**: alinea el text a la dreta.

També hi ha altres utilitats per estilitzar i modificar el text:
- **text-uppercase**: converteix el text a majúscules.
- **text-lowercase**: converteix el text a minúscules.
- **text-capitalize**: capitalitza només la primera lletra de cada paraula.

Pots ajustar l'alineació del text de manera responsable segons la mida de pantalla:
- **text-sm-left**, **text-md-center**, **text-lg-right**, etc. Això permet canviar l'alineació del text a mesura que la pantalla canvia de mida.

## 7. Componentes Bootstrap

Un **componente Bootstrap** es un bloque predefinido de código que sigue los principios del framework Bootstrap para proporcionar estilos, comportamiento interactivo y funcionalidades de diseño responsivo.

Estos componentes están diseñados para ayudarte a crear **interfaces de usuario (UI)** modernas y atractivas de manera **rápida y fácil**, sin tener que escribir todo el código CSS o JavaScript desde cero.

## 8. Componente card

El ``componente Card`` de Bootstrap es una forma versátil y estilizada de mostrar información agrupada dentro de un contenedor. Puedes usar las tarjetas para mostrar contenido como texto, imágenes, listas de enlaces, botones y más.

```html
<div class="card" style="width: 18rem;">
  <div class="card-body">
    <h5 class="card-title">Título de la Tarjeta</h5>
    <p class="card-text">Texto de ejemplo dentro de una tarjeta de Bootstrap.</p> <a href="#" class="btn btn-primary">Ir a algún lugar</a>
  </div>
</div>
```

## 9. Componente nav

El **componente Nav** de Bootstrap se utiliza para crear menús de navegación. Este componente es versátil y te permite diseñar tanto menús horizontales como verticales, barras de pestañas y menús estilo "píldora".

Ejemplo:

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Navegación Horizontal</title>
  <!-- Incluye Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container mt-4">
    <ul class="nav">
      <li class="nav-item">
        <a class="nav-link active" href="#">Inicio</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Servicios</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Precios</a>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Deshabilitado</a>
      </li>
    </ul>
  </div>

  <!-- Incluye Bootstrap JS y Popper.js -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

## 10. Componente carroussel

El ``componente Carrusel`` en Bootstrap te permite mostrar una serie de imágenes, texto o contenido en formato de diapositivas que pueden desplazarse automáticamente o mediante controles de navegación.

Ejemplo:

```html

<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Carrusel de Bootstrap</title>
  <!-- Incluye Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

<div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
  <!-- Indicadores opcionales (puntos) -->
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Diapositiva 1"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Diapositiva 2"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Diapositiva 3"></button>
  </div>

  <!-- Contenido del carrusel -->
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="https://via.placeholder.com/800x400" class="d-block w-100" alt="Imagen 1">
      <div class="carousel-caption d-none d-md-block">
        <h5>Primera diapositiva</h5>
        <p>Texto descriptivo de la primera diapositiva.</p>
      </div>
    </div>
    <div class="carousel-item">
      <img src="https://via.placeholder.com/800x400" class="d-block w-100" alt="Imagen 2">
      <div class="carousel-caption d-none d-md-block">
        <h5>Segunda diapositiva</h5>
        <p>Texto descriptivo de la segunda diapositiva.</p>
      </div>
    </div>
    <div class="carousel-item">
      <img src="https://via.placeholder.com/800x400" class="d-block w-100" alt="Imagen 3">
      <div class="carousel-caption d-none d-md-block">
        <h5>Tercera diapositiva</h5>
        <p>Texto descriptivo de la tercera diapositiva.</p>
      </div>
    </div>
  </div>

  <!-- Controles de navegación izquierda/derecha -->
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Anterior</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Siguiente</span>
  </button>
</div>

<!-- Incluye Bootstrap JS y Popper.js -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>
```
