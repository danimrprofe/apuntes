# Capas

Dentro de la etiqueta `<body>` de tu documento, agrega la etiqueta `<div>`. Esta etiqueta es la que servirá para crear la capa.

```html
<body>
    <div></div>
</body>
```

Dentro de la etiqueta `<div>`, agrega el contenido que quieras presentar. Puede ser cualquier cosa, desde un texto, una imagen, hasta otros elementos HTML. Es importante destacar que la etiqueta `<div>` se utiliza para agrupar contenido, no para presentarlo directamente.

```html
<div>
  Aquí va el contenido que quieras presentar
</div>
```

Finalmente, para darle estilo a la etiqueta `<div>` y que se vea como una capa, agrega algunas etiquetas de estilo.

Por ejemplo:

```html
<div style="background-color: #cccccc; width: 200px; height: 200px; padding: 10px; margin: 10px;">
  Aquí va el contenido que quieras presentar
</div>
```

Con esto, habrás creado una capa div en tu documento HTML.

## Ejemplo de página con capas

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        div {
            width: 100px;
            float: left;
        }
        div.cabecera{
            background-color:#da543c;
            border: 1px solid black;
            width: 100%;
        }
        div.menu{
            background-color: green;
            width: 30%;
        }
        div.principal{
            background-color: blue;
            width: 70%;
        }
    </style>
</head>
<body>
    <div class="cabecera">
        <h1>Esto es una capa</h1>
        <p>Esta capa va a ser roja</p>
    </div>
    <div class="menu">
        <h1>Esto es otra capa</h1>
        <p>Esta capa va a ser verde</p>
    </div>
    <div class="principal">
        <h1>Esto es otra capa</h1>
        <p>Esta capa va a ser verde</p>
    </div>
</body>
</html>
```