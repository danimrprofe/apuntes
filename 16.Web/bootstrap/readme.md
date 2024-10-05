
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
necesidad de CSS personalizado.

## Ejemplo de una fila con dos columnas de igual ancho

```html
<div class="container">
  <div class="row">
    <div class="col-md-6">Columna 1 (50%)</div>
    <div class="col-md-6">Columna 2 (50%)</div>
  </div>
</div>
```

## Ejemplo del componente card

```html
<div class="card" style="width: 18rem;">
 <div class="card-body">
 <h5 class="card-title">Título de la Tarjeta</h5>
 <p class="card-text">Texto de ejemplo dentro de una tarjeta de Bootstrap.</p> <a href="#" class="btn btn-primary">Ir a algún lugar</a>
</div>
</div>
```

## Margin i Padding

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

## Text i Alineació

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
