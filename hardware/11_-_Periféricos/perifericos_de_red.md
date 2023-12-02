# Periféricos de red

![imagen](img/UD_10_-_Perif%C3%A9ricos_%28tema_completo%29115.jpg)

![imagen](img/UD_10_-_Perif%C3%A9ricos_%28tema_completo%29116.png)

![imagen](img/UD_10_-_Perif%C3%A9ricos_%28tema_completo%29117.jpg)

![imagen](img/UD_10_-_Perif%C3%A9ricos_%28tema_completo%29118.png)

![imagen](img/UD_10_-_Perif%C3%A9ricos_%28tema_completo%29119.jpg)

![imagen](img/UD_10_-_Perif%C3%A9ricos_%28tema_completo%29120.jpg)

![imagen](img/UD_10_-_Perif%C3%A9ricos_%28tema_completo%29121.png)

![imagen](img/UD_10_-_Perif%C3%A9ricos_%28tema_completo%29122.jpg)

![imagen](img/UD_10_-_Perif%C3%A9ricos_%28tema_completo%29123.jpg)

![imagen](img/UD_10_-_Perif%C3%A9ricos_%28tema_completo%29124.png)

![imagen](img/UD_10_-_Perif%C3%A9ricos_%28tema_completo%29125.jpg)

![imagen](img/UD_10_-_Perif%C3%A9ricos_%28tema_completo%29126.jpg)

## Necesidad

La necesidad de conectar ordenadores entre sí y compartir recursos, como impresoras y documentos, ha llevado al desarrollo de las **tarjetas de red** o NIC (Network Interface Card).

Las tarjetas de red, también conocidas como adaptadores de red, son componentes de hardware que se instalan en los ordenadores para permitirles conectarse a una red. Estas tarjetas son responsables de gestionar la comunicación entre el ordenador y el resto de dispositivos de la red.

Existen diversos tipos de tarjetas de red, que se adaptan al tipo de cable o arquitectura de red utilizada. Algunos de los tipos más comunes son:

- Ethernet: Es el tipo de red más utilizado actualmente. Utiliza cables de par trenzado y conectores RJ-45. Las tarjetas de red Ethernet son compatibles con estándares como 10/100/1000 Mbps (Fast Ethernet y Gigabit Ethernet) y se encuentran integradas en muchas placas base de ordenadores.
- Wi-Fi: Permite la conexión inalámbrica a una red mediante el uso de antenas y estándares como Wi-Fi 802.11. Las tarjetas de red Wi-Fi se utilizan en ordenadores portátiles y dispositivos móviles para acceder a redes inalámbricas.

Es importante destacar que las placas base de muchos ordenadores modernos ya integran un conector RJ-45 para conexión Ethernet, lo que significa que no es necesario agregar una tarjeta de red adicional en esos casos.

![imagen](img/UD_10_-_Perif%C3%A9ricos_%28tema_completo%29127.jpg)

## Tarjetas de red

Una tarjeta de red, también conocida como tarjeta de interfaz de red (NIC, por sus siglas en inglés), es un componente hardware que permite la comunicación entre un ordenador y una red local (LAN). Su función principal es transmitir y recibir datos a través de la red, permitiendo que el ordenador se comunique con otros dispositivos conectados a la misma red.

Existen diferentes tipos de tarjetas de red, pero una de las más comunes es la tarjeta de red Ethernet. Esta tarjeta se conecta a una ranura en la placa base del ordenador, lo que permite su integración en el sistema.

![imagen](img/UD_10_-_Perif%C3%A9ricos_%28tema_completo%29128.jpg)

## Puertos

La salida de conexión de una tarjeta de red se realiza a través del cableado adecuado. En la actualidad, el tipo de cable y conector más comúnmente utilizado es el cable trenzado con conector **RJ-45**.

El **cable trenzado** consiste en pares de cables de cobre trenzados entre sí para reducir las interferencias electromagnéticas. Estos cables se conectan a la tarjeta de red mediante el conector RJ-45, que es un conector estándar de ocho pines utilizado para redes Ethernet.

![imagen](img/UD_10_-_Perif%C3%A9ricos_%28tema_completo%29130.jpg)

El **conector BNC** (Bayonet Neill-Concelman) y el cable **coaxial** eran utilizados en el pasado, pero en la actualidad se consideran obsoletos para la mayoría de las aplicaciones de redes de área local (LAN). El cable coaxial se utiliza comúnmente en redes de cable de televisión, pero su uso en redes informáticas ha sido reemplazado en gran medida por el cable trenzado.

Las tarjetas de red suelen tener LEDs (diodos emisores de luz) que indican la actividad de la tarjeta. Estos LEDs pueden mostrar información como la conexión activa, la transmisión de datos o la presencia de errores. Esto proporciona una retroalimentación visual rápida sobre el estado de la tarjeta de red y su actividad.

![imagen](img/UD_10_-_Perif%C3%A9ricos_%28tema_completo%29129.png)

## Dirección MAC

La dirección MAC (Media Access Control) es un código identificador único de 48 bits (6 bytes) que corresponde de forma exclusiva a una tarjeta o interfaz de red. Esta dirección es asignada a nivel de hardware durante el proceso de fabricación y se conoce también como dirección física.

La dirección MAC es utilizada para identificar de manera única a cada dispositivo de red en el mundo. Cada tarjeta o interfaz de red tiene su propia dirección MAC individual, lo que permite distinguir un dispositivo de red de otros en una red local.

![imagen](img/UD_10_-_Perif%C3%A9ricos_%28tema_completo%29131.jpg)

## Formato

La dirección MAC está determinada y configurada por dos partes:

- Los primeros 24 bits de la dirección MAC corresponden al identificador del fabricante. Cada fabricante de tarjetas de red tiene un rango de direcciones MAC asignado, lo que permite identificar el origen del dispositivo.
- Los últimos 24 bits de la dirección MAC son asignados por el Instituto de Ingenieros Eléctricos y Electrónicos (IEEE, por sus siglas en inglés). Estos bits representan la parte de identificación única de la tarjeta de red.

La dirección MAC se representa en una codificación hexadecimal de 12 caracteres, divididos generalmente en pares. Por ejemplo, "00-16-E6-5E-7B-74" o "00:16:E6:5E:7B:74". También se pueden encontrar representaciones donde no hay separadores, como "0016E65E7B74". Estas representaciones dividen la dirección MAC en grupos de dos caracteres hexadecimales.

![imagen](img/UD_10_-_Perif%C3%A9ricos_%28tema_completo%29132.jpg)

## Velocidades

las tarjetas de red actuales son capaces de adaptarse a diferentes velocidades de red para garantizar la compatibilidad con otros dispositivos en la red. Esto se logra mediante la detección automática de la velocidad de la red y ajustando la velocidad de la tarjeta de red en consecuencia.

Las tarjetas de red más comunes en la actualidad son las que soportan **Ethernet, Fast Ethernet y Gigabit Ethernet**. Estos estándares ofrecen velocidades de **10 Mb/s, 100 Mb/s y 1 Gb/s (1.000 Mb/s)** respectivamente.

Algunas tarjetas de red pueden soportar múltiples velocidades, lo que les permite adaptarse a la velocidad de la red a la que están conectadas.

Esto es especialmente útil en entornos de red mixtos, donde puede haber dispositivos con diferentes velocidades de red. La tarjeta de red se ajustará automáticamente a la velocidad más baja compatible con el resto de la red para garantizar la comunicación adecuada.

![imagen](img/UD_10_-_Perif%C3%A9ricos_%28tema_completo%29133.gif)

## Tarjetas de red Wi\-Fi

* Características Wi\-Fi
  * _Ventajas: _ Instalación rápida y  económica
  * _Inconvenientes_ : menos seguras y velocidad menor
* Funciona transmitiendo la información
  * mediante tarjetas de red con una o varias  _antenas_
  * A través de  _routers_  o  _puntos_  <span style="color:#FFC000"> </span>  _de_  <span style="color:#FFC000"> </span>  _acceso_ \.
* Los datos pueden enviarse  _cifrados_  \(seguridad\)
* Tarjetas expansión red para Wi\-Fi formato  _PCI_
* Adaptadores de red Wi\-Fi en formato  _stick_  <span style="color:#FFC000"> </span>  _USB_
  * Facilidad de instalación y portabilidad\.
* Tarjetas expansión Wi\-Fi: también tienen dirección MAC\.

![imagen](img/UD_10_-_Perif%C3%A9ricos_%28tema_completo%29134.jpg)

![imagen](img/UD_10_-_Perif%C3%A9ricos_%28tema_completo%29135.png)
