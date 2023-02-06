# Formato dirección IPv4

La dirección IPv4 es una dirección de 32 bits que está dividida en dos partes: Network ID (Net ID) y Host ID. La jerarquía de direcciones en IPv4 es de dos niveles, lo que optimiza el enrutamiento de paquetes en la red.

- El Network ID (Net ID) es un prefijo que identifica una red específica.
- El Host ID identifica un host específico dentro de esa red.

Es importante tener en cuenta que dos redes diferentes no pueden tener el mismo Network ID y dos hosts dentro de la misma red no pueden tener el mismo Host ID.

## IP e interfaces

Las direcciones IP no se pueden repetir dentro de la misma subred o red. Esto significa que cada dirección IP es única para cada interfaz de red en cada host. Estas reglas garantizan que los paquetes de datos puedan ser entregados de manera eficiente y precisa a su destino correcto.