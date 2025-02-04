# Resistències (I)

Els **resistors** s'intercalen en un circuit per ajustar el valor de la intensitat del corrent que hi circula. Poden ser de dos tipus:

## Resistors Fixes

- El valor d'un resistor fixe ve indicat per un **codi de colors** que permet identificar la seva resistència.

## Resistors Variables

Els **resistors variables** permeten ajustar el seu valor entre 0 i un valor màxim. El valor es modifica mitjançant un **cursor** que es pot moure. Es poden classificar en:

- **Lineals**: La variació de la resistència és proporcional al moviment del cursor.
- **Angulars**: La resistència canvia segons l'angle del cursor.

Els resistors variables més habituals en electrònica són els **potenciòmetres**.

# Resistències. Codis de Colors

![Imatge de Circuits Electrònics](img%5C57%20-%20Circuits%20electr%C3%B2nics0.png)

## Codis de Colors

Els codis de colors en les resistències es componen de diverses bandes que indiquen el valor i la tolerància de la resistència.

### 1. Codis de 3 bandes de color a un extrem
- **Valor de la resistència**:
  - El valor es determina multiplicant el nombre representat per les dues primeres bandes de color per la potència de 10 indicada per la tercera banda.

### 2. Tolerància de la resistència
- **Tolerància**:
  - Indica la màxima diferència entre el valor nominal i el valor real de la resistència.
  - Es pot identificar per una banda extra de color en l'altre extrem de la resistència. Els colors comuns per a la tolerància són:
    - Or
    - Plata
    - Marró
    - Vermell

![](img%5C57%20-%20Circuits%20electr%C3%B2nics1.png)

# Resistències Variables

Les resistències variables són aquelles que poden modificar el seu valor en funció d'algun paràmetre extern.

## 1. Resistències dependents de la llum
- **LDR (Light Dependent Resistor)**:
  - Les LDR canvien la seva resistència segons la intensitat de la llum que les incideix. Quan hi ha més llum, la seva resistència disminueix.

## 2. Resistències dependents de la temperatura
- Aquestes resistències varien el seu valor en funció de la temperatura a la qual estan exposades.
  - **Termistores**: Un tipus de resistència que varia segons la temperatura, amb dues classes:
    - NTC (Coeficient de temperatura negatiu): La resistència disminueix quan la temperatura augmenta.
    - PTC (Coeficient de temperatura positiu): La resistència augmenta quan la temperatura augmenta.




# La resistència i el potenciòmetre

1. La resistència electrònica o resistor Si obres un aparell electrònic, és probable que trobis als circuits uns petits elements cilíndrics amb anells de colors a la seva superfície. Aquests components són resistors de carbó i la seva missió és oferir resistència al pas del corrent elèctric.

FIN
Codi de colors
Terminals de connexió
Símbol elèctric del resistor.
Resistors en un circuit electrònic.
Resistor de carbó.

Es fabriquen resistors amb diferents valors de resistència: 100 2 (ohms), 2 200 2, etc. Els anells de colors impresos al resistor indiquen el seu valor de manera codificada.

Els resistors es col·loquen als circuits per limitar el valor del corrent que circula per un circuit o per un dels seus components. També s'utilitzen per limitar la tensió elèctrica. En travessar una resistència, els electrons experimenten una pèrdua d'energia, i això es tradueix en una caiguda de la tensió elèctrica.

# 2. Resistències de pel·lícula de carbó

Hi ha molts tipus de resistors, un dels més utilitzats són els de pel·lícula de carbó. S'anomenen així perquè el material que produeix resistència elèctrica és una fina capa de carbó, que es diposita en forma d'hèlix a sobre d'un casquet de ceràmica. El corrent ha de travessar l'hèlix de carbó per passar entre els dos terminals, de manera que, com més llarga sigui l'hèlix, més resistència oferirà.
Casquet de ceràmica
Com
Hèlix de carbó
Interior d'un resistor de pel·lícula de carbó.


# 3. Exemple 1: limitació del corrent

A l'exemple següent, en introduir un resistor en sèrie obtenim una reducció del corrent que circula pel circuit, passen menys electrons pel cable cada segon. Els electrons que aconsegueixen passar a través de la resistència tenen, a més, menys energia. Amb el resistor al circuit, l'energia que rep la bombeta és menor (passen menys electrons i amb menys energia) i, per tant, brilla menys.
Clica sobre el resistor per inserir-lo al circuit.
Sense resistor, circula molt
corrent pel circuit i la bombeta brilla
intensament. Clica el resistor per inserir-lo al circuit.
+
L'amperímetre detecta molt corrent elèctric
Amperímetre
10+
Piles en sèrie (3 V)
Circulen molts electrons, la intensitat és gran
← La bombeta brilla
intensament
Bombeta
Cable ampliat

# 4. Exemple 2: protecció de components electrònics

El circuit de sota consisteix en un LED alimentat per dues piles cilíndriques. Els LED són components electrònics molt sensibles a l'excés de corrent i de tensió. Per evitar que es cremin, els LED es connecten en sèrie amb un resistor que limita la intensitat i la tensió del corrent que els hi arriba.
419
LED
LED
El resistor connectat en sèrie protegeix el LED
impedint que passi massa corrent
NENNUNINN
Aquest circuit no disposa de resistor de protecció per al LED. En pocs minuts el LED
s'espatllarà per l'excés de corrent


# 5. Codi de colors

Alguns tipus de resistències electròniques tenen indicat el seu valor amb anelles de colors pintades a la superfície. El codi de colors que s'utilitza permet als professionals identificar-les fàcilment. Normalment està format per quatre anelles:

- les dues primeres indiquen les xifres inicials; la tercera és un factor multiplicador i la quarta, la tolerància, indica possibles desviacions del valor ja que la fabricació no és perfecta. L'animació de la dreta et permet conèixer el valor d'una resistència electrònica sense necessitat de saber de memòria el codi de colors. Només has de fer clic sobre els colors
corresponents de cada anella. A la part superior podràs veure el valor numèric de la resistència.
1a xifra 2a xifra


0Q ± 1%
Factor multiplicador
X1
x10
x100
x1000
x10000
x100000
x1000000
Valor de la resistència (en ohms)
Tolerància
±1%
±2%
±5% color or
+10% color plata
Clica sobre els colors

# 6. El potenciòmetre

Els potenciòmetres, també anomenats resistències ajustables, són resistències variables. A diferència de les resistències de carbó, que tenen un valor fix, el valor de la resistència dels potenciòmetres es pot ajustar entre zero ohms i un valor màxim. A sota pots veure un dels tipus de potenciòmetre més utilitzats, els de tipus rotatori. Al seu interior hi ha una pista d'un material resistiu, carbó per exemple. L'electricitat entra al potenciòmetre per una plaqueta metàl·lica que frega la pista resistiva. Utilitzant un tornavís podem girar la plaqueta i fer que toqui en un punt o un altre de la pista. Com més longitud de pista resistiva travessi l'electricitat, major serà la resistència del potenciòmetre.
PINER
SPAR
Potenciometre en una placa de prototips.
Pista resistiva
Cable
de entrada
Plaqueta metàl·lica
Z
Símbol elèctric del potenciòmetre
Osca per introduir un tornavís i girar la plaqueta metàl·lica
<<
Connexions
Cable
de sortida
Interior d'un potenciometre rotatori. Les fletxes grogues indiquen el camí que recorre el corrent elèctric.

# 7. Exemple 1: control de la velocitat d'un motor elèctric

En aquest circuit s'ha col·locat un potenciòmetre rotatori intercalat entre dues piles i un petit motor elèctric. Aquest potenciòmetre té un eix i un comandament que ens permet girar-lo fàcilment amb la mà, sense necessitat de fer servir un tornavís. Movent el comandament del potenciòmetre podem fer que arribi més o menys potència elèctrica al motor, la qual cosa farà que el motor giri més o menys ràpidament i amb més o menys força. Un circuit semblant el podem trobar en trens i cotxes elèctrics de joguina.
719
Comandament
Eix
El motor elèctric girarà més
o menys ràpidament en funció de la posició del
potenciòmetre
Potenciometre
rotatori
Piles
Motor elèctric
tecno 12-18 Llibre de text digital
Un potenciometre es pot utilitzar per controlar
la velocitat de gir d'un petit motor elèctric.
< Capitol

# 8. Exemple 2: volum d'un altaveu

Un altre tipus de potenciòmetre molt comú és el de tipus lliscant. Funciona igual que els rotatoris, la diferència és que la pista resistival és recta i no en forma d'anell. En el circuit de sota pots veure com s'utilitza un potenciòmetre lliscant per controlar el volum d'un altaveu. El volum del so que emet l'altaveu serà més baix com més quantitat de pista resistiva travessi el senyal elèctric que produeix l'aparell de música.
Equip de música
min
PLAY
VOL max
Control del volum
mín
Cursor
Pista resistiva
màx
Pista
conductora de coure
Potenciometre lliscant.
444
Potenciometre lliscant usat per controlar el volum d'un altaveu. Les fletxes grogues indiquen el camí que recorre el corrent elèctric.
El volum de l'altaveu depèn de la posició del potenciòmetre


# Qüestionari

1. Què és un resistor? Quina unitat s'utilitza per mesurar el seu valor?
2. Dibuixa un resistor de pel·lícula de carbó i indica les seves parts. Després explica com funciona. 3. Quina és la funció dels resistors als circuits electrònics?
4. A l'exemple de la pàgina 3/9, què passa en connectar un resistor en sèrie al circuit? Per què? 5. Per què s'utilitza un resistor al circuit de l'exemple de la pàgina 4/9?
6. Quin és el valor de la resistència d'aquests resistors?
7. Indica el codi de colors de les següents resistències:
1.000 ± 1%, 450.000 ±10%, 2.500 ±5% i 220 Q ±2% Exemple: 220 Q± 5% serà: vermell-vermell-marró-or
8. Què és un potenciòmetre? Quin és el seu símbol?
9. Quants tipus de potenciòmetres surten a la miniunitat? Posa un exemple d'ús de cadascun d'ells.
