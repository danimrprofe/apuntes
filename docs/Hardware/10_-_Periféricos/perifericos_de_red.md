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

* Local Area Network \( _Red de área local_ \)
* Red se establece mediante:
  * _Cable_
  * Componentes  _hardware_  \(comunican ordenadores\)
* Tarjeta de red
  * Comunica un ordenador con una red local
  * _Ranura_  <span style="color:#FFC000"> </span>  _PCI_  <span style="color:#FFC000"> </span> \(Placa base\) o integrada en  <span style="color:#FFC000">placa </span>  _base_

![imagen](img/UD_10_-_Perif%C3%A9ricos_%28tema_completo%29128.jpg)

## Puertos

La salida de conexión de una tarjeta de red se realiza a través del cableado adecuado. En la actualidad, el tipo de cable y conector más comúnmente utilizado es el cable trenzado con conector **RJ-45**.

El **cable trenzado** consiste en pares de cables de cobre trenzados entre sí para reducir las interferencias electromagnéticas. Estos cables se conectan a la tarjeta de red mediante el conector RJ-45, que es un conector estándar de ocho pines utilizado para redes Ethernet.

![imagen](img/UD_10_-_Perif%C3%A9ricos_%28tema_completo%29130.jpg)

El **conector BNC** (Bayonet Neill-Concelman) y el cable **coaxial** eran utilizados en el pasado, pero en la actualidad se consideran obsoletos para la mayoría de las aplicaciones de redes de área local (LAN). El cable coaxial se utiliza comúnmente en redes de cable de televisión, pero su uso en redes informáticas ha sido reemplazado en gran medida por el cable trenzado.

Las tarjetas de red suelen tener LEDs (diodos emisores de luz) que indican la actividad de la tarjeta. Estos LEDs pueden mostrar información como la conexión activa, la transmisión de datos o la presencia de errores. Esto proporciona una retroalimentación visual rápida sobre el estado de la tarjeta de red y su actividad.

![imagen](img/UD_10_-_Perif%C3%A9ricos_%28tema_completo%29129.png)

## Dirección MAC

* _Media Access Control _ address
  * Código identificador de  _48 bits _ \(6 bytes\)
  * Corresponde de forma única a una  _tarjeta o interfaz de red\. _
* _Características_
  * Individual, cada dispositivo tiene su propia dirección
  * Únicas a nivel mundial
  * Escritas en el hardware en su momento de fabricación\.
  * Se conoce también como dirección física

![imagen](img/UD_10_-_Perif%C3%A9ricos_%28tema_completo%29131.jpg)

* MAC determinada y configurada por
  * _IEEE_  \(los últimos 24 bits\)
  * _Fabricante_  \(los primeros 24 bits\)
* Las direcciones MAC
  * Codificación  _hexadecimal_  \(12 caracteres\)
  * Se suelen ordenar por parejas:
  * XX\.XX\.XX\.XX\.XX\.XX  _00–16–E6–5E–7B–74_
* No necesaria para montar una red doméstica ni configurar conexión a Internet\.
* Se puede “modificar”, pero al arrancar el equipo, la MAC volverá siempre a su estado original\.

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
