# Agregació de xarxes

Obtenir la super xarxa / es que resumeix les xarxes indicades a continuació:

## Conjunt A

- 195.100.16.0/24
- 195.100.17.0/24
- 195.100.18.0/24
- 195.100.19.0/24
- 195.100.20.0/24
- 195.100.21.0/24
- 195.100.22.0/24
- 195.100.23.0/24

La primera etapa es identificar el prefijo de red común a todas las direcciones IP. En este caso, el prefijo común es 195.100.16.0/20.

Luego, se puede crear una superred utilizando ese prefijo común. La dirección de la superred sería 195.100.16.0/20.

## Conjunt B

- 10.2.4.0/24
- 10.2.5.0/24
- 10.2.6.0/24
- 10.2.7.0/24
- 10.2.8.0/24
- 10.2.9.0/24
- 10.2.10.0/24
- 10.2.11.0/24
- 10.2.12.0/24
- 10.2.13.0/24
- 10.2.14.0/24
- 10.2.15.0/24
- 10.2.16.0/24

## Conjunto C

Para crear una superred a partir de las siguientes redes, se puede utilizar la técnica de **agregación de direcciones IP**.

- 192.168.0.0/24
- 192.168.1.0/24
- 192.168.3.0/24
- 192.168.4.0/24
- 192.168.5.0/24

La primera etapa es identificar el prefijo de red común a todas las direcciones IP. En este caso, el prefijo común es ``192.168.0.0/16``.

Luego, se puede crear una superred utilizando ese prefijo común. La dirección de la superred sería 192.168.0.0/16. Esta dirección describirá todas las direcciones IP dentro de ese rango, incluyendo las direcciones IP individuales 192.168.0.0/24, 192.168.1.0/24, 192.168.3.0/24, 192.168.4.0/24 y 192.168.5.0/24.

**Conclusión:**

De esta manera, la superred 192.168.0.0/16 es una forma más eficiente de describir y manejar un grupo de direcciones IP en una red de computadoras.

## Conjunto D

- 172.16.0.0/16
- 172.17.0.0/16
- 172.18.0.0/16
- 172.19.0.0/16

## Conjunto E

- 10.0.0.0/24
- 10.0.1.0/24
- 10.0.4.0/24
- 10.0.7.0/24
- 10.0.8.0/23
- 10.0.10.0/23

## Conjunt F

- 10.1.0.0/24
- 10.1.1.0/24
- 10.1.2.0/24
- 10.1.3.0/24
- 10.1.4.0/24
- 10.1.5.0/24
- 10.1.6.0/24
- 10.1.7.0/24

## Conjunto G

- 192.168.0.0/23
- 192.168.2.0/23
- 192.168.4.0/22
- 192.168.8.0/21
