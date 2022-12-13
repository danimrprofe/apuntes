# La impressora 3D





![](img%5CImpressora%203D2.png)

## La Impresora que tenim és una Prusa I3 Pro W.

![](img%5CImpressora%203D1.jpg)

El llit es pot escalfar fins 110ºC . Es pot canviar en la configuració. La temperatura s'haurà d'ajustar a el tipus de plàstic utilitzat, ja que cada un té una temperatura diferent de fusió.

![](img%5CImpressora%203D3.jpg)

## Tipus de filament

Sembla que suporta filaments PLA i ABS.

- Diàmetre de __filament __ 1.75 mm,
- Diàmetre de __boca __ 0.3 mm.

![](img%5CImpressora%203D4.jpg)

## Què accessoris tenim per treballar amb la impressora

![](img%5CImpressora%203D5.jpg)

_Al departament tenim:_

Un lector de targetes USB per a targetes SD

Dues targetes SD, de 256 MB i de 8 GB. La de 8 GB no m'ha funcionat, l'altra si. La de 256 ja venia amb diversos arxius d'altres anys.

Laca per fer a sobre del llit calenta parell que l'objecte adherència millor i no es deixi anar a meitat de la impressió

Una rasqueta per arrencar restes de plàstic del llit calent.

![](img%5CImpressora%203D6.jpg)

## Posada en marxa

A la dreta de la màquina hi ha un  __botó d'encesa__  per posar en marxa la impressora.

Per manejar-la, hi ha un panell LCD amb una rodeta per desplaçar-nos per les diferents opcions i prémer-la quan vulguem entrar en una o acceptar.

El primer que he fet és provar que funciona, i per això he anat a prepari> autohome, i el extrusor s'ha col·locat en el punt inicial.

## Calibració

Necessitem calibrar la impresora abans de començar a imprimir per primer cop.

Aturar els  __motors stepper __ al menú LCD

En primer lloc cal  __calibrar l'eix Z__  i mirar que les dues barres estan a la mateixa altura amb un  __peu de rei__

A continuació __ calibrar les quatre cantonades __ del llit amb extrusor posant el foli al mig i girant les claus fins que fregui però passi el paper.

![](img/2022-12-13-18-59-07.png)

## Crear un model STL

Per a imprimir un objecte amb una impressora 3d necessitem el seu disseny digital en un format d’ <span style="color:#448C79"> __arxiu anomenat stl__ </span>  , que és l’estàndard per a la impressió 3d.

![](img%5CImpressora%203D11.png)

La majoria de programes de disseny 3d permeten guardar o exportar els nostres dissenys al format .stl.

Podem fer els dissenys amb programes com ara  _[Tinkercad](https://www.tinkercad.com/)_ .

També podem descarregar models de  _[Thingiverse ](https://www.thingiverse.com/)_ o altres repositoris d’objectes online

![](img%5CImpressora%203D12.png)

## Laminar l’objecte

Carreguem l’arxiu de l’objecte (STL) que volem imprimir en un programa anomenat laminador o slicer

El laminador dividirà l’objecte en fines capes horitzontals segons uns paràmetres, que defineixen les característiques físiques i d’impressió de cada una.

El resultat de tot aquest procés de laminat és un arxiu tipus g-code que conté tot un seguit d’ordres que la impressora 3d és capaç d’executar a fi d’imprimir el nostre objecte

Jo he utilitzat el programari cura:

[Pàgina web de cura](https://ultimaker.com/es/software/ultimaker-cura)

![](img%5CImpressora%203D13.png)

## Falda

La falda ens netejarà l’extrusor al començar

![](img%5CImpressora%203D15.png)

## Opcions d'impressió

Opcions més habituals a seleccionar per imprimir:

- 0.2 mm de definició
- Parets: 3 i 1.2 mm (3 parets de 0.4)
- Velocitat d’impressió: 40 mm/s
- Farcit: 20%
- Marcar generar soporte

## Carregar el model a imprimir

Ens caldrà un arxiu GCODE de la figura que volem imprimir.

Per a això, l'haurem de haver passat de l'ordinador a la targeta SD, i després insertar la tarjeta SD darrere de la pantalla LCD a l'esquerra (costa una mica trobar-lo)

![](img%5CImpressora%203D16.png)

## Imprimir

Després que tot l'ajust estigui bé, anar a  __autohome__

![](img/2022-12-13-19-00-25.png)

També podem preencalentir el plàstic prèviament sense començar a imprimir res. En aquest cas el llit i l'extrusor s'encalentiran fins assolir les temperatures fixades.

![](img%5CImpressora%203D8.png)

## Imprimir un model des de la tarjeta SD

Trieu el fitxer de la targeta SD per començar a imprimir.Triam el fitxer **gcode** que hem carregat a la tarjeta SD des de l’ordinador

En aquest moment, començaran a escalfar-se l’extrussor i el llit i, en arribar a la temperatura dessitjada, començarà la impressió.

![](img/2022-12-13-19-02-28.png)

## Components de la impressora i friquisme

![](img%5CImpressora%203D21.jpg)

## Extrusor complet amb ventilador lateral

Vista de l’extrusor un cop desmuntat. A ma esquerra el  __ventilador __ que refreda la part del tub on va el filament abans d’entrar al heater. Això es fa per evitar que es fongui la part de filament superior i el filament es pugui empènyer amb més facilitat

![](img%5CImpressora%203D22.jpg)


![](img%5CImpressora%203D23.jpg)

Entrada de filament

## Vista del mecanisme de extrusió

Aquí es pot veure un cop desmuntat  __l’__  __extrusor__  __ __ (va fixat amb un pern per sota), per on entra el filament, les rodes dentades el fiquen cap a dins.

El mecanisme dret permet amb un pern alliberar la roda dentada per a poder ficar el filament a ma fent pressió

![](img%5CImpressora%203D24.jpg)

Encalentidor o heater

Boquilla o nozzer

## Encalentidor i boquilla

L’entrada té un interior de tefló, i l’encalentidor encalenteix el tros de filament abans de l’entrada a la  __boquilla extrusora__  (nozzle).

El cable vermell duu corrent per encalentir, i el blanc el termistor que mesura la temperatura.

Rosca per fixar a la base

![](img%5CImpressora%203D25.jpg)

![](img%5CImpressora%203D26.jpg)

Boquilla o nozzer

Entrada de filament

![](img%5CImpressora%203D27.png)

cables de corrent per encalentir

Encalentidor o heater

![](img%5CImpressora%203D28.jpg)

## Problemes: obstrucció

Per tal de retirar material, vam haver de treure la peça i posar la impresora en mode  __preheat ABS__ , el que fa encalentir el heater a 240º.

Si no llevem la ventilació, la part que no està coberta pel heater es refredaria i el plàstic interior obstruit no arribaria a fondre.

Amb un cable elèctric rigid vam aconseguir fer pressió i que sortís per l’altre banda tot el plàstic que hi havia.

## Problemes: termistor

La impressora té dos sensors de temperatura ( __termistors__ ). Aquests varien la seva resistència en funció de la temperatura.

![](img%5CImpressora%203D29.jpg)

Les dues temperatures que ens interessen són la del heater i la del hot bed.

- Un termistor va aferrat sota el llit calent amb cinta i en mesura la temperatura.
- L’altre va enganxar al heater i també en mesura la temperatura.

Si qualsevol dels termistors detecta una temperatura anormalment alta, l’impressora donarà un error en pantalla per a evitar accidents.

## Biblioteques d’objectes

Es poden descarregar models ja fets d’internet de diverses fonts:

- Thingiverse:  _[http://www.thingiverse.com/](http://www.thingiverse.com/)_
- Youmagine: _[ https://www.youmagine.com/](https://www.youmagine.com/)_
- Instructables: http://www.instructables.com/
- Myminifactory: http://www.miminifactory.com/
- Shapeways: https://shapeways.com/
- 3DHubs: https://www.3dhubs.com/
- http://www.123dapp.com/Gallery/content/all
- http://apps.microsoft.com/windows/en-us/app/3d-builder/75f3f766-13b3-45e9-a62f-29590d5781f2
- https://3dwarehouse.sketchup.com/?redirect=1

## Disseny d’objectes

_[Blender](https://www.blender.org/)_ , programa professional molt complet. També permet crear animacions amb els objectes dissenyats. Tutorial.

_[Autodesk 123D](https://www.autodesk.com/solutions/123d-apps)_

_[SketchUp ](https://www.sketchup.com/)_ programa pensat per ser utilitzat de forma intuïtiva i flexible, fent que sigui fàcil el seu aprenentatge. Tutorial.

_[Tinkercad](https://www.tinkercad.com/)_  programa gratuït en línia creat per Autodesk. Materials de formació a Ateneu.

## Crear un modelo 3D desde una imagen vectorial e imprimirlo

Podemos crear una imagen .SVG, o directamente importar una a tinkercad.

Dentro de tinkercad,podremos cambiar el tamaño de los modelos importados, recolocarlos, etc.
Tendremos que exportar el archivo a un formato .STL que pasarle al programa Cura
Por último, en cura, generaremos un archivo .Gcode, que será el que pasemos a la impresora utilizando la tarjeta de memoria

