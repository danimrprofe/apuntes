---
Fitxers
---

Un fitxer és un conjunt de **dades** **emmagatzemades** en un dispositiu de memòria (com el disc dur, SSD, o memòria flash) que es poden llegir, escriure i gestionar mitjançant un sistema operatiu.

Els fitxers permeten **organitzar** i **conservar** **informació** de manera persistenta perquè estigui disponible fins i tot després de tancar un programa o apagar l'ordinador.

---

## 2. Tipus de fitxers

Els fitxers poden ser:

De ``text``, quan contenen dades llegibles per humans (com ara **.txt**, **.csv**)

```
John Doe
Jane Smith
Alice Johnson
```

``Binaris``, quan emmagatzemen informació en format no llegible directament (com **.jpg**, **.exe**).

```
01010101101010101011101010101011
```

---
# TREBALL AMB FITXERS A PYTHON
---

### Estructura bàsica d'un fitxer

Un fitxer és una seqüència de bytes que es guarda en un dispositiu d'emmagatzematge. Té:

- un **nom**
- una **extensió**
- **permisos** d'accés
---

# Permisos d'accés

Els permisos d'accés a fitxers en Windows es gestionen per mitjà del sistema de seguretat de fitxers, que **permet establir qui pot llegir, escriure o executar un fitxer** o directori.
Aquests permisos es poden aplicar tant a **fitxers** individuals com a **carpetes** i es poden personalitzar per a **usuaris** i **grups** específics.

---
# Tipus de permisos d'accés

- **Lectura** (Read):
  - Permet llegir el contingut del fitxer o la llista de fitxers d'una carpeta.
  - No permet modificar ni executar el fitxer.
- **Escriptura** (Write):
  - Permet modificar el contingut d'un fitxer o afegir nous fitxers a una carpeta.
  - No permet llegir ni executar el fitxer.

---
# Tipus de permisos d'accés:
- **Execució** (Execute):
  - Permet executar fitxers que siguin programes o scripts.
  - Aquest permís s'afegeix en fitxers executables com ``.exe, .bat, .cmd``, o scripts com ``.ps1``.
- **Modificació** (Modify):
  - Permet llegir, escriure i eliminar fitxers, així com canviar-ne el contingut.
  - No permet canviar els permisos d'altres usuaris.
- **Control** **total** (Full Control):
  - Inclou tots els permisos: llegir, escriure, executar, modificar, eliminar, i també permet modificar els permisos d'altres usuaris.
  - És el permís més alt i permet la gestió completa del fitxer o carpeta.

Python ens permet treballar amb fitxers, utilitzant diferents funcions que ja venen implementades.
---

### Modes d'obertura d'arxius en Python

Per treballar amb un fitxer, primer cal obrir-lo en un mode específic (lectura, escriptura, afegir, etc.), i després tancar-lo per evitar pèrdues de dades o errors en el sistema.

1. **`'r'`**: **lectura** (default).  Obre el fitxer per llegir-lo. L'error es produeix si el fitxer no existeix.
2. **`'w'`**:  **escriptura**.  Crea un fitxer nou (si no existeix) o sobreescriu-lo si ja existeix.
3. **`'a'`**:  **afegir**.  Obre el fitxer per afegir contingut al final sense esborrar el que ja hi ha.
4. **`'x'`**:  creació **exclusiva**. Crea un fitxer nou, però genera un error si el fitxer ja existeix.

### Modes d'obertura d'arxius en Python

5. **`'b'`**:  **binari**. Específic per obrir fitxers en mode binari (per exemple, per llegir o escriure imatges).
6. **`'t'`**:  **text** (default). Utilitzat per treballar amb fitxers de text. No és necessari especificar-lo ja que és el mode per defecte.
7. **`'+'`**:  **lectura** i **escriptura**. Permet llegir i escriure al mateix temps (combinat amb altres modes, per exemple `'r+'` o `'w+'`).

---

## Exemples d'obertura d'arxius:

- `open('arxiu.txt', 'r')`: Només lectura.
- `open('arxiu.txt', 'w')`: Esborrar i escriure.
- `open('arxiu.txt', 'a')`: Afegir al final.
- `open('arxiu.txt', 'rb')`: Llegir en mode binari.

---

### Treball amb Python

Per a llegir un arxiu l'hem de obrir en **mode lectura**, utilitzant la funció `open()`:

```python
f = open("arxiu.txt", "r")
```

Una vegada obert, ja podem llegir-lo amb la funció `read()`:

```python
f = open("arxiu.txt", "r")
text = f.read()
```

Quan l'hem acabat de llegir, es important tancar el fitxer amb la funció `close()`:

```python
f = open("arxiu.txt", "r")
text = f.read()
f.close()
```

---
Imprimir contingut per pantalla
---

Si volem imprimir per pantalla tot el contingut de l'arxiu:

```python
f = open("arxiu.txt", "r")
text = f.read()
print(text)
f.close()
```

---

## Llegir línea per línia

También podemos ir leyendo línea por línea

```python
f = open("arxiu.txt", "r")
text = f.read()
print(text)
f.close()

for linea in f:
    print(linea)

archivo.close()
```

---

## Eliminar un archivo

Para borrar un archivo podemos utilizar la librería os. Para ello, al principio de nuestro archivo debemos importarla.

```python
# Eliminar un archivo llamado "test.txt"
import os
os.remove("archivo.txt")
```

---

## Mode escriptura

Si utilizamos el argumento ``w``, abriremos el archivo en modo escritura. De este modo:

- Si el archivo ya existe, se **sobrescribe** completamente, borrando el contenido previo.
- Si el archivo no existe, se crea un **nuevo archivo**.

```python
f = open("alumnes.txt", "w")
f.write("Daniel")
f.close()
```

---

## Mode annexar

Si utilizamos el argumento ``a``, abriremos el archivo en modo anexar. De este modo:

- Si el archivo ya existe, se añade nuevo contenido al final del archivo sin eliminar el contenido existente.
- Si el archivo no existe, se crea un nuevo archivo.

```python
# abrir el archivo
f = open('alumnes.txt', 'a')
f.write('Pepe')
```

---

Si volem afegir el contingut a una nova línia, haurem de fer servir el caràcter d'escapament ``\n``. Aquest farà que en el lloc on estigui col·locat es faci un bot de línia.

Esborrarem el contingut previ amb ``w``

```python
f = open('alumnes.txt', 'w')
file.write("Dani\nAna")
file.write("\n")
file.write("Pepe")
```

Ara tindrem un arxiu amb 3 línies.

---
Activitat 1
---
Crea un programa que et demani el nom, pes, edat i altura, i calculi el teu índex de masa corporal . A continuació, hauràs de guardar a cada línea les dades d'una persona.

$$
IMC = \frac{\text{pes (kg)}}{\text{altura (m)}^2}
$$

El resultat haurà de ser:

```
Dani (40) 75 kg 1.74 m IMC: 24.77
```

---

A continuació veurem com esborrar una línea, canviar el contingut o inserir línies al mig de l'arxiu.

---

## Borrar una línea concreta

Para borrar una línea específica, puedes leer todas las líneas, eliminar la línea que no quieres, y luego escribir de nuevo el archivo.

```python
f = open('alumnes.txt', 'r')
linies = f.readlines()
del linies[1]
f = open('alumnes.txt', 'w')
file.writelines(linies)
```

Línies és una llista, recorda, que els seus elements s'acceceixen amb un índex, i que el primer és el 0: ``línia[0]``, ``linia[1]``, etc.
Si tot va bé, ha d'haver desaparegut el segón nom.

---

## Modificar una línea concreta

Si deseas modificar una línea específica, puedes seguir un proceso similar, pero actualizando el contenido de la línea en memoria antes de escribirlo de nuevo.

```python
f = open('alumnes.txt', 'r')
linies = f.readlines()
linies[1] = "Lola\n"
f = open('alumnes.txt', 'w')
file.writelines(linies)
```

---

## Insertar una línea en una posición concreta

Si deseas insertar una línea en una posición específica, puedes insertar la nueva línea en la lista de líneas antes de escribir de nuevo el archivo.

```python
f = open('alumnes.txt', 'r')
linies = f.readlines()
linies.insert(1, "Joan\n")
f = open('alumnes.txt', 'w')
file.writelines(linies)
```
