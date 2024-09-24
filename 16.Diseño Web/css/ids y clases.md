# Identificadores y Clases en CSS

## 1. ¿Qué es un Identificador 1(ID)?

- Un identificador (ID) es un nombre único que se asigna a un solo elemento HTML para estilizarlo de manera exclusiva.
- Se define en HTML con el atributo id, y en CSS, se selecciona utilizando el símbolo #.

Ejemplo en HTML:
<div id="header">Encabezado</div>

Ejemplo en CSS:
#header {
  background-color: blue;
  color: white;
}

Reglas:
- Cada ID debe ser único en toda la página.
- Se utiliza para aplicar estilos específicos a un solo elemento.

## 2. ¿Qué es una Clase (class)?

- Una clase es un grupo de estilos que puede aplicarse a múltiples elementos en una página.
- Se define en HTML con el atributo class, y en CSS, se selecciona usando el símbolo .

Ejemplo en HTML:
<div class="box">Caja 1</div>
<div class="box">Caja 2</div>

Ejemplo en CSS:
```css
.box {
  background-color: lightgray;
  padding: 20px;
}
```

Reglas:
- Se puede usar la misma clase en múltiples elementos.
- Útil cuando varios elementos necesitan los mismos estilos.

## 3. Diferencias clave entre ID y Clase:

| Característica  | ID                      | Clase                                           |
| --------------- | ----------------------- | ----------------------------------------------- |
| Símbolo en CSS  | #nombreID               | .nombreClase                                    |
| Unicidad        | Un solo elemento por ID | Varios elementos pueden compartir una clase     |
| Uso recomendado | Estilos únicos          | Agrupar elementos que comparten el mismo estilo |

## 4. Uso de ID y Clases combinados

A veces es útil combinar ID y clases para lograr un estilo más específico.

Ejemplo en HTML:
<div id="main" class="container">Contenido principal</div>

Ejemplo en CSS:

```css
#main {
  font-size: 20px;
}

.container {
  padding: 15px;
  background-color: #f0f0f0;
}
```

En este caso, el div tiene un ID único para aplicar estilos exclusivos, pero también usa la clase container para compartir estilos con otros elementos.

## 5. ¿Cuándo usar ID y cuándo clases?

- Usa IDs cuando necesites identificar un único elemento.
- Usa clases cuando quieras aplicar el mismo estilo a varios elementos.
- En general, se recomienda preferir el uso de clases, ya que es más flexible y evita conflictos.
