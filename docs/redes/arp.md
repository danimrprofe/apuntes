# ARP

ARP (Address Resolution Protocol) es un protocolo de comunicación utilizado en redes de ordenador para **determinar la dirección física de un dispositivo en una red local**. Funciona a nivel de la capa de enlace de datos del modelo OSI y se utiliza para traducir direcciones IP en direcciones MAC.

Cuando un dispositivo necesita enviar un paquete a otro dispositivo en una red local, primero consulta su tabla ARP para ver si ya tiene la dirección MAC correspondiente a la dirección IP destino. Si la dirección MAC no está presente en la tabla, el dispositivo envía un mensaje broadcast ARP en la red para solicitar la dirección MAC correspondiente. Cualquier dispositivo en la red que tenga la dirección IP destino responde con su dirección MAC, y el dispositivo origen actualiza su tabla ARP y utiliza la dirección MAC para enviar el paquete.

## L'ORDRE ARP

El comando ``arp`` es un comando de línea de comandos que se utiliza en sistemas operativos Windows y Linux. Este comando muestra la tabla ARP (Address Resolution Protocol) en el sistema, que contiene información sobre las asociaciones entre direcciones IP y direcciones MAC en una red local.

## Consulta

La opción "-a" indica que se desea ver todas las entradas en la tabla ARP. Cuando se ejecuta el comando "arp -a", se muestra una lista de direcciones IP y direcciones MAC correspondientes en la red local, además de información adicional, como la interfaz de red utilizada y el estado de la entrada en la tabla.

    arp -a

El resultat:

```
Interfaz: 192.168.1.2 --- 0xd
  Dirección de Internet          Dirección física      Tipo
  192.168.1.1           ec-f4-51-7c-7c-ce     dinámico
  192.168.1.255         ff-ff-ff-ff-ff-ff     estático
  224.0.0.2             01-00-5e-00-00-02     estático
  224.0.0.22            01-00-5e-00-00-16     estático
  224.0.0.251           01-00-5e-00-00-fb     estático
  224.0.0.252           01-00-5e-00-00-fc     estático
  239.255.255.250       01-00-5e-7f-ff-fa     estático
```

## Afegir una entrada a la taula

    arp -s 192.168.0.12 00:11:24:a4:03:bf

## Eliminar una entrada de la taula

    arp -d

## Comportament de la taula ARP

L’objectiu d’aquesta activitat és conèixer com evoluciona la taula ARP.

Ja sabeu que el protocol ARP permet obtenir l’adreça MAC que correspon a una IP, i a mesura que va recopilant adreces MAC les emmagatzema en una taula en memòria.

Responeu les preguntes que us plantegem a continuació:

1.	Acabem de connectar l’ordinador a la xarxa; si executeu per consola l’ordre arp -a, què succeeix?
2.	Ara feu un PING a un altre ordinador de la vostra xarxa local (per exemple: ping 192.168.0.14) què succeeix si executeu l’ordre anterior? Ens ofereix la mateixa informació?
3.	Quins passos hauria de fer si vull conèixer l’adreça MAC de l’encaminador al qual estic connectat?

## Taula arp

Explica, a partir de la informació de la comanda arp:

- Quines interfícies hi ha?
- Quines adreces corresponen a cada una?
- Que vol dir dinàmic o estàtic?
