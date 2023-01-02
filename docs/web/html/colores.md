# Color en HTML

Tenemos colores predefinidos en HTML con nombre (red, blue), pero también los podemos definir nosotros. Para ello se puede usar el sistema RGB, que nos permite afinar más el color que queramos.

```html
<p style="color:red;">Esto es rojo</p>
<p style="color:#FF0000;">Esto también es rojo</p>
```

## ¿Cómo podemos especificar un color en concreto?

El color es un código hexadecimal, formado por tres pares de dígitos, precedidos del símbolo #, que pueden ser números y letras entre [ 0 1 2 3 4 5 6 7 8
9 A B C D E F ].

Con estos dígitos el par de menor valor será el 00 y el de mayor valor
será el FF

Los colores primarios son:

| código RGB | color    |
| ---------- | -------- |
| #FF0000    | Rojo     |
| #00FF00    | Verde    |
| #0000FF    | Azul     |
| #FFFFFF    | Blanco   |
| #000000    | Negro    |
| #FFFF00    | Amarillo |

Oscurecer un color. Para hacer un color más oscuro, hay que reducir el
número de su componente, dejando los otros dos invariables. Así, el rojo #FF0000 se puede hacer más oscuro con #AA0000, o aún más oscuro con #550000.

Aclarar un color. Para hacer que un color tenga un tono más suave (más
pastel), se deben variar los otros dos colores haciéndolos más claros, aumentando
su componente, (número más alto), en una cantidad igual. Así, podemos convertir el
rojo en rosa con #FF7070.