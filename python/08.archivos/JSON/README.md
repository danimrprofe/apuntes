
# Format **JSON**

``JSON`` (JavaScript Object Notation) és un format lleuger per a l’emmagatzematge i intercanvi de dades. És fàcilment llegible per humans i estructurat de manera que també és senzill de processar per les màquines. S’utilitza àmpliament en aplicacions web, APIs i bases de dades.

### Característiques principals de JSON

- Textual i **llegible**: utilitza una sintaxi clara basada en claus i valors.
- Lleuger: ocupa poc espai i no conté caràcters innecessaris.
- Independent del llenguatge: encara que es basa en **JavaScript**, es pot utilitzar amb **Python**, **Java**, **C#**, etc.
- Basat en estructures de dades: s'organitza amb objectes i llistes.

### Estructura bàsica de JSON

JSON es basa en dos tipus d’estructures fonamentals:

- Els ``objectes`` JSON són representats amb **{}** (claus).
- Les ``claus`` són sempre strings (text entre cometes dobles): **name, age**
- Els ``valors`` poden ser strings, nombres, booleans, arrays o altres objectes: **Lionel Messi, 35**.

```json
{
  "name": "Lionel Messi",
  "age": 35
}
```
Aquest objecte té dos parells clau-valor.

Les ``llistes`` o arrays JSON son representades amb **[]** (claudàtors) i contenen una llista ordenada de valors. Els valors poden ser de qualsevol tipus compatible amb JSON. Aquest objecte té un parell clau-valor, i el valor és una llista amb 3 elements.

```json
{
  "players": [
    {
      "name": "Lionel Messi",
      "position": "Forward",
      "team": "Paris Saint-Germain",
      "nationality": "Argentine",
      "age": 35
    },
    {
      "name": "Cristiano Ronaldo",
      "position": "Forward",
      "team": "Al Nassr",
      "nationality": "Portuguese",
      "age": 38
    },
    {
      "name": "Kylian Mbappé",
      "position": "Forward",
      "team": "Paris Saint-Germain",
      "nationality": "French",
      "age": 25
    }
  ]
}
```

### Treball amb Python

Python inclou un ``mòdul json`` per treballar amb fitxers JSON fàcilment
Guardar i carregar dades en format JSON.

### On es fa servir JSON?

- APIs Web: comunicació entre aplicacions i serveis.
- Bases de dades NoSQL: MongoDB utilitza JSON per emmagatzemar dades.
- Configuració d’aplicacions: molts programes utilitzen arxius .json per guardar configuracions.