---
# Format CSV
---

Els fitxers ``CSV`` (Comma-Separated Values) són fitxers de text on les dades es separen per comes o altres delimitadors. Són útils per emmagatzemar taules de dades i intercanviar informació entre aplicacions.

```csv
name,age
Lionel Messi,35
Cristiano Ronaldo,38
Kylian Mbappé,25
```

---

# Guardar dades en un fitxer CSV

Hi ha un mòdul de Python per treballar amb fitxers CSV.

```python
import csv

dades = [
    ["Nom", "Edat", "Ciutat"],
    ["John", 28, "New York"],
    ["Alice", 30, "Los Angeles"],
    ["Bob", 25, "Chicago"]
]

with open('treballadors.csv', mode='w', newline='') as file:
    escriptor_csv = csv.writer(file)

    for linia in dades:
        escriptor_csv.writerow(linia)
```
---
# Llegir des d'un fitxer

```python
import csv

with open('treballadors.csv', mode='r', newline='') as arxiu:
    lector_csv = csv.DictReader(arxiu)

    # Read each row as a dictionary
    for row in lector_csv:
        print(row)
```