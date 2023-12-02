# Cálculo de parámetros de redes

Para calcular la dirección de red, la dirección de broadcast y el número de direcciones de host disponibles en la dirección IP 192.168.1.0 con una máscara de subred de /24, podemos seguir los siguientes pasos:

Convertir la dirección IP y la máscara de subred a binario.

- La dirección IP 192.168.1.0 se convierte en 11000000.10101000.00000001.00000000.
- La máscara de subred /24 se convierte en 255.255.255.0, que en binario es 11111111.11111111.11111111.00000000.

Aplicar la máscara de subred a la dirección IP para obtener la dirección de red. Para hacer esto, simplemente realizamos una operación lógica AND bit a bit entre la dirección IP y la máscara de subred. El resultado es 192.168.1.0.

## Dirección de broadcast

Calcular la **dirección de broadcast** de la red. Para hacer esto, se toma la dirección de red y se agrega el complemento a uno de la máscara de subred. El resultado es ``192.168.1.255``.

## Direcciones de host para equipos

Calcular el número de **direcciones de host** disponibles. Para hacer esto, restamos uno al complemento a uno de la máscara de subred y se obtiene el resultado de 254 direcciones de host disponibles en la subred.

Es lo mismo que restar a las 256 direcciones de red posibles, las dos que identifican a la red y la de broadcast.

- Dirección de red: 192.168.1.0
- Dirección de broadcast: 192.168.1.255

Nos quedarían 254 (256-2) direcciones de host disponibles.

## Primera y última dirección IP asignables a equipos

La primera dirección IP asignable a un equipo dentro de una red es la dirección de red más uno. La última dirección IP asignable es la dirección de broadcast menos uno. Estas direcciones están fuera de los rangos de direcciones de host y están reservadas para uso específico en la red.

En el ejercicio anterior, la dirección de red es 192.168.1.0/24 y la dirección de broadcast es 192.168.1.255/24. Por lo tanto, la primera dirección IP asignable a un equipo sería 192.168.1.1 y la última sería 192.168.1.254.