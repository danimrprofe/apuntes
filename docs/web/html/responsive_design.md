# Responsive design

## Imagen adaptada a las dimensiones

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <picture>
        <source srcset="img/minionpequeño.png" media="(max-width: 600px)">
        <source srcset="img/minionmediano.jpg" media="(max-width: 1000px)">
        <source srcset="img/miniongrande.jpg">
        <img src="img/minionmediano.jpg" alt="Flowers" style="width:auto;">
    </picture>
</body>
</html>
```