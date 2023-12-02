# Agentes de reenvío

Las solicitudes de asignación de configuración automática de los parámetros de red mediante DHCP las inicia una máquina cuando arranca.

Se utiliza un mensaje de difusión a la subred, que es respondido por el o los servidores DHCP de la misma.
Los mensajes de difusión no se difunden en entornos enrutados.
En cada subred en que se utilice DHCP debería haber un servidor DHCP que escuche las solicitudes emitidas.

## Solución

Centralizar el servicio DHCP y hacer que un solo servidor proporcione automáticamente IP a clientes de varias redes.
La solución es utilizar agentes DHCP de retransmisión o reenvío (relay).
Agente DHCP de retransmisión o reenvío
Dispositivo de la red
Escucha las solicitudes DHCP que se producen en la red
Las encamina hacia un servidor DHCP que se encuentra en otra red para que éste las atienda.
Servidor DHCP dará una respuesta que enviará hacia el agente de reenvío y éste a su vez la trasladará al cliente que hizo la petición.

## ¿Cuando lo podemos utilizar?

Se puede utilizar un único servidor DHCP siempre que se añada en cada subred un **agente de retransmisión**
Este esté adecuadamente configurado.

El agente de retransmisión estará implementado en un router. El router realiza el encaminamiento entre la red con clientes DHCP y la red en la que se encuentra el servidor DHCP.

Si la organización tiene varias redes, puede tener varios agentes de retransmisión y un solo servidor DHCP centralizado.

También es posible implementar el agente de retransmisión en ordenadores con varios adaptadores de red que hagan funciones de encaminamiento entre cada una de las redes a las que pertenecen.

## ¿Cómo se configura un agente de retransmisión?

Para configurar un agente de retransmisión, primero hay que activarlo en el dispositivo de encaminamiento y específicar la red cliente y el servidor DHCP que atenderá las peticiones. Posteriormente, en el servidor DHCP hay que configurar las subredes a las que se da el servicio, indicando las direcciones IP que se van a asignar dentro de cada subred. Finalmente, los agentes de reenvío deben configurarse para que envíen los paquetes DHCP a su servidor correspondiente.