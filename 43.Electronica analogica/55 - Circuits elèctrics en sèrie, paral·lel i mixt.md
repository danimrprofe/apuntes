# TEMA 55Circuits elèctrics en sèrie, paral·lel i mixtes

* Introducció
* C\.e\. en sèrie
  * Generadors
  * Resistències
  * Condensadors
  * Bobines
* C\.e\. en paral·lel
  * Generadors
  * Resistències
  * Condensadors
  * Bobines
* Associacions mixtes
  * Reduibles a conjunts sèrie\-paral·lel
  * No reduibles
* Mètodes generals d’anàlisi de circuits
* Règims de funcionament
  * AC\,DC i Transitori
* Fenòmens transitoris
  * Circuits RC i RL
* C\.e\. en règim senoidal permanent
  * Circuits amb R\, L o C
  * Circuits RC i RL sèrie
  * Circuits RLC sèrie
  * Circuits RLC paral·lel

# 1. Introducció (I)

* __Circuit elèctric__
  * Conjunt d'elements conductors connectats  manera que constitueixen un recorregut tancat a través del qual circula \(o pot  circular\) un corrent elèctric\.
* __Elements__  més comuns:
  * __Generador__  \(pila\, bateria\, etc\.\)\,
    * Subministra energia elèctrica al circuit\.
  * __Receptor__  \(motor\, bombeta\, resistència\, etc\.\)
    * Aprofita l'energia  elèctrica subministrada pel generador\, transformant\-la en altres tipus de  energia \(mecànica\, lluminosa\, calorífica\, etc\.\)\.
  * __Interruptor__
    * Obre/tanca el circuit\, perquè la transformació de energia es realitzi quan es demana\.
  * __Conductors__ \, generalment fils metàl\.lics
    * Uneixen el generador i el receptor\.
    * Tenen una determinada resistència\.
      * Es simbolitza concentrada en 1 zona del circuit
      * Considerant la resta del  conductor com a ideal\, és a dir\, sense resistència\.

* El corrent
  * Considerat en sentit convencional  com el  __moviment de càrregues positives__
  * Surt del generador  pel pol positiu i torna a ell pel negatiu
  * Conservant constant la seva intensitat al llarg de tot el  circuit
    * principi de conservació de la  càrrega elèctrica\)
* En aquest tema estudiarem
  * Com es comporten els circuits elèctrics al  combinar
    * Diferents generadors
    * També els receptors més simples: Resistències\, bobines i condensadors\.
* Components elèctrics
  * Es poden  __connectar__  de formes molt diferents
  * Destaquem l'associació  __en sèrie\, en paral\.lel i en forma mixta\. __
* Altres formes d'associació
  * Són les connexions en estrella i en triangle\.
  * Principalment en circuits  trifàsics

# 2. Circuits en sèrie

* Circuit sèrie
  * Es considera que 2 o més components estan associats en sèrie quan es connecten un a continuació d'un altre\, de manera que per tots ells circula la mateixa intensitat\.
* Associació en sèrie de resistències
  * Quan es connecten diverses resistències en sèrie
  * Resistència equivalent
    * Resistència única que consumeix la mateixa energia que les associades
    * I pot substituir\, sense que per això es produeixi modificació energètica alguna en el circuit\.
  * Resulta al connectar les resistències una a continuació d'una altra
  * De manera que a través de totes elles circuli la mateixa intensitat
  * Complint que la diferència de potencial entre els extrems de la resistència equivalent
    * És igual a la suma de les diferències de potencial entre els extrems de les resistències associades\, és a dir:

![](img%5C55%20-%20Circuits%20el%C3%A8ctrics%20en%20s%C3%A8rie%2C%20paral%C2%B7lel%20i%20mixt0.png)

  * Req = R1 \+ R2 \+ R3 \+ \.\.\.  = Er x i
  * __"En una associació de resistències en sèrie la resistència equivalent__  __és igual a la suma de les resistències associades "\.__

# 2.1. Resistències en sèrie. Divisor de tensió

* Consisteix en una associació en sèrie de resistències\.
* Cas típic
  * Resistència R proveïda d'un cursor lliscant \(de tipus potenciomètric\)
  * Connectada de manera que
    * El corrent I subministrat pel generador en arribar al punt C es ramifica\, i una partd'ella\, I1\, circula a través de la resistència de càrrega Rl\, \(qualsevol aparell consumidor d'energia elèctrica\)\, mentre que la part restant I2\, ho fa a través del tros de resistència variable comprès entre C i B\.
* Si el cursor està situat a l'extrem A\, una gran part del corrent passa a través de la resistència de càrrega\, i en ella la tensió serà màxima\. A mesura que el cursor es va desplaçant cap a l'extrem B\, la tensió en R\, va disminuint \(dividint\) fins arribar a anul\.lar\.
* D'aquesta manera
  * Situant adequadament el cursor
  * Es pot obtenir qualsevol valor de tensió a la càrrega\, comprès entre zero i el valor màxim esmentat\.
* Si en lloc del potenciòmetre s'empren 2 resistències fixes
  * Tensió del generador queda dividida en 2 tensions proporcionals al valor de cada resistència\.

# 2.2. Generadors en sèrie

* Resulta d'unir entre si i successivament els pols de signe contrari dels diferents generadors
* Força electromotriu \(F\.E\.\) total
  * Igual a la suma de les F\.E\. de cada un dels generadors
* Resistència interna \(Ri\) total
  * Igual a la suma de les Ri de tots ells\.
* Per tant\, aplicant la llei d'Ohm\, resulta:
  * Associant n generadors iguals en sèrie s'aconsegueix una forçaelectromotriu n vegades més elevada que amb un sol generador\.
  * Una bateria està formada per una associació en sèrie de piles elementals\.

# 3.2. Generadors en paral·lel

* És la que resulta d'unir d'una banda tots els pols positius i\, d'altra\,tots els negatius dels n generadors\.
* Cal evitar connectar els generadors en paral\.lel amb els pols invertits
* Produiria un corrent a través d’tots dos generadors molt inten
* La resistència interna d'un generador sol ser petita i\, molt probablement\, es destruirien tots dos generadors\.
* Si els generadors \(com passa en un cas pràctic ja que en cas contrari tots adquiririen la tensió de la fem més petita\)\) són tots iguals\,
* es dedueix fàcilment el valor de la intensitat que circula per la resistència R:
* No s'aconsegueix lliurar major tensió al receptor
* Encara que sí més intensitat
* Sobretot en el cas que la resistència exterior sigui petita\.
* Avantatge
  * Per cada generador passa una intensitat menor que si no hagués associació i d'aquesta manera es descarreguen més lentament\.

# 4. Circuit mixt

* Combinació de les dues associacions anteriors
* Quan en el mateix circuit hi ha
  * Associacions en  sèries acoblades en paral\.lel
  * Associacions en paral·lel connectades en sèrie\.
* Associació mixta de resistències
  * La resistència equivalent es calcula
    * Resolent perseparat cadascuna de les associacions senzilles formades
    * Fins arribar a una resistència única\.
  * Intensitat que circula per una de les resistències
    * Obtenir la diferència de potencial entre els seus extrems
    * Aplicar després la llei d'Ohm

# 6. Conclusions

* Connexió en  __sèrie__
  * Simplifica el cablejat dels circuits
  * Inconvenient
    * Si falla un dels components queda el circuit obert
    * Impedint el funcionament de tots els altres\, és pel que aquesta associació nos'utilitza pràcticament en instal\.lacions elèctriques\.
* Connexió en  __paral·lel__
  * Més adequada per a aquest tipus de sistemes
  * Xarxa de distribució lliura una tensió constant
  * Tensió de treball sempre la mateixa
    * S'estandarditza la fabricació dels components de la instal·lació\.
* En màquines elèctriques o els automatismes
  * S'utilitzen principalment associacions mixtes
  * Destacant les associacions  __estrella i triangle __ en les màquines elèctriques de corrent altern\.

# Règim transitori

* Règim  __transitori__ \, o només "transitori"
  * Resposta d'un circuit elèctric que s'extingeix en el temps
* Règim  __permanent__
  * Resposta que roman constant fins que es varia bé el circuit o bé l'excitació del mateix\.
* Transitori de tensió\,
  * Temps de càrrega del condensador\.
  * Un cop carregat\, la sortida ja no varia\.
  * No hi ha un punt on el règim canvia\, passant de transitori a permanent\, sinó que el transitori tendeix asimptòticament al règim permanent\.
  * A la pràctica es tria un valor arbitrari que depèn de l'aplicació de què es tracti\.
* Des del punt de vista de l'anàlisi circuital\,
  * Règim transitori
    * Ve donat per la solució homogènia de  __l'equació diferencial __ lineal que descriu el circuit
  * Règim permanent
    * S'obté de la solució de la  __particular__ \.
    * L'esmorteïment ens indica l'evolució del transitori\, que es pot aproximar monòtonament al règim permanent\, com en la figura 1\, o bé patir oscil lacions amortides\.
    * Aquest últim cas pot ser perillós ja que el nivell de tensió o corrent pot superar els nivells nominals de funcionament

* Es diu règim transitori\, o només "transitori"\, a aquella resposta d'un circuit elèctric que s'extingeix en el temps\, en contraposició al règim permanent\, que és la resposta que roman constant fins que es varia bé el circuit o bé l'excitació del mateix\.
* La figura mostra un transitori de tensió\, que dura el temps de càrrega del condensador\.
* Un cop carregat\, la sortida ja no varia\.
* No hi ha un punt on el règim canvia\, passant de transitori a permanent\, sinó que el transitori tendeix asimptòticament al règim permanent\. A la pràctica es tria un valor arbitrari que depèn de l'aplicació de què es tracti\. Figura 2\. Simulació d'un transitori de tensió amb sobreimpuls\.
* Des del punt de vista de l'anàlisi circuital\, el règim transitori ve donat per la solució homogènia de l'equació diferencial lineal que descriu el circuit\, mentre que el règim permanent s'obté de la solució de la particular\. L'esmorteïment ens indica l'evolució del transitori\, que es pot aproximar monòtonament al règim permanent\, com en la figura 1\, o bé patir oscil lacions amortides\. Aquest últim cas pot ser perillós ja que el nivell de tensió o corrent pot superar els nivells nominals de funcionament\, com es veu a la figura 2\. El generador produeix un to de 10 kHz i 10 Vp\, que s'inicia als 2 ms\.
* Des del punt de vista tecnològic\, els transitoris són de gran importància\.
  * Es produeixen en tots els circuits \(l'encesa ja és un transitori\)
  * I se solen extingir de forma natural sense causar problemes\, però hi ha casos on s'han de limitar ja que poden provocar un mal funcionament o fins i tot la destrucció d'algun component\.
  * Ha de prestar atenció als transitoris principalment en les següents situacions:
* Encendido\. Transitorios en las líneas de alimentación pueden destruir algún componente\. En los amplificadores operacionales o circuitos cmos puede presentarse el fenómeno de Latch\-up\.
* Conmutación de inductancias: Relés\, motores\, actuadores electromagnéticos\.\.\. Son peligrosos para el elemento de potencia que los gobierna\. Se suelen proteger con diodos\.
* Líneas de transmisión\. En líneas de transmisión incorrectamente adaptadas se producen reflexiones que\, en el caso de circuitos digitales\, se comportan como transitorios\. También estas líneas son susceptibles de captar ruidos de diversa procedencia que se acoplan a ellas llevando la señal fuera del margen de funcionamiento\. Algunas familias digitales incluyen  _clamp diodes_  para proteger las entradas de estos transitorios\.

