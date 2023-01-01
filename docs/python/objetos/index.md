# Objetos

## Clases y objetos

Las clases y los objetos son los elementos básicos de la programación orientada a objetos. Una clase es una plantilla para crear objetos. Un objeto es una instancia de una clase.

- Una **clase** define las propiedades y los comportamientos de un conjunto de objetos. Por ejemplo, una clase definiría los atributos y los métodos de todos los objetos "perro" creados a partir de la misma.
- Un **objeto** es una instancia de una clase. Por ejemplo, el perro Spot es un objeto de la clase "Perro". Spot tendrá todas las propiedades y comportamientos definidos para todos los perros, como la capacidad de ladrar y correr.

# Crear clases

En Python, las clases se definen utilizando la palabra clave **class**, seguida del nombre de la clase. Los objetos se crean a partir de esa clase usando la sintaxis de nombre_de_clase(argumentos).

# Método init es el constructor de la clase

```python
Class Persona:
  def __init__(self):
    print("Soy una persona")
```

# Para crear objetos a partir de una clase

```python
peter_parker = Persona()
```

# A partir de una clase se puede crear otra que la incluya

```python
Class Superheroe(Persona):
  def __init__(self):
    super().__init__()
    print("Tengo superpoderes")
```

# Crear objetos

A partir de una clase podemos crear tantos objetos (instancias de una clase) como queramos:

```python
spiderman = Superheroe()
superman = Superheroe()
```

## Ejemplo con pokemon

```python
class Pokemon:
    def __init__(self, nombre, tipo, nivel):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel

    def atacar(self):
        print(f"{self.nombre} ha usado un ataque de {self.tipo}")

    def subir_nivel(self):
        self.nivel += 1
        print(f"{self.nombre} ha subido al nivel {self.nivel}")

pikachu = Pokemon("Pikachu", "Trueno", 5)
pikachu.atacar()
pikachu.subir_nivel()
```