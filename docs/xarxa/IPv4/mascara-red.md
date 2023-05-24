# Máscara de red

La máscara:

- Establece frontera entre la parte de red y la parte de host de una dirección IP
- Permite dividir el campo de host para crear subredes
- Bits parte red y subred = 1 y Bits parte de host = 0

El router debe realizar un AND lógico binario entre la dirección IP de destino del paquete IP que llega y la máscara de red

- Clase A: 255.0.0.0
- Clase B: 255.255.0.0
- Clase C: 255.255.255.0
- Clase D i E: no tienen

![imagen](2019-05-08-08-46-40.png)

## Representación de la máscara

La máscara de red se puede representar:

1. En formato IP decimal (255.255.255.0)
2. Con la notación / en la que se especifican los bits de red (/24)

## Utilización de la máscara

![imagen](2019-05-08-08-47-12.png)