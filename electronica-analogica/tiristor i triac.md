# Semiconductors en circuits de control de potència

## TIRISTOR

* Se podría definir a un tiristor
  * Como un diodo que\, mediante la incorporación de otra patilla\, podemos controlar el paso de corriente a través del mismo\.
  * De aquí se deduce que un tiristor se comportaría como un diodo; sólo dejaría pasar la corriente en un sentido\.
  * Pero con la variación respecto a éste de que
    * Aplicándole una tensión en la tercera pata que hemos introducido\, éste conduciría
    * Si a esta patilla no le aplicamos tensión éste no conduciría\.
* Diferencia con transistor
* En el tiristor
  * Si hay tensión  _pasa toda la corriente_
  * Si no la hay\, en su tercera patilla\, no se dispara
  * No hay término medio como en el transistor\.
* Podría decirse que un tiristor es un interruptor controlado\.
* Hay otras tres formas de disparar un tiristor
  * Por variación brusca de tensión entre ánodo y cátodo
  * Por aumento de tensión entre ánodo y cátodo
  * Por aumento de temperatura
* Obtenido por primera vez en  __1\.957__ \, en los Estados Unidos\, por la empresa  __General Electric__ \.

![](img%5C57%20-%20Circuits%20electr%C3%B2nics7.png)

## Triac

* Component electrònic equivalent a dos  __SCR__
  * Units en anti\-paral·lel \(en paral·lel\, però cadascun en un sentit\)
  * Amb les seues  _portes_  unides entre si\.
* Diferencia amb tiristor convencional
  * TIRISTOR és unidireccional y el TRIAC es bidireccional
* Això produeix
  * __Commutador electrònic bidireccional__  pot conduir corrent en qualsevol direcció quan és disparat \(engegat\)\.
  * Pot ser disparat per un voltatge positiu o negatiu aplicat en la  _porta_ \.
  * Una vegada activa\, t continua conduint fins que el corrent que el recorre disminueix per sota d'un valor límit
  * Commutador molt apropiat per a circuits AC
    * Permet control de molta potència
    * Amb una intensitat de l'escala de microampers\.
* Aplicant un pols d'activació en un cicle AC
  * Controla % de corrent que passarà pel triac cap a la càrrega \( _control de fase_ \)\.
* Triacs de baixa potència s'usen en aplicacions com
  * Control de llum
  * Control de velocitat per a ventiladors elèctrics i altres motors elèctrics
  * Control computeritzat modern en moltes aplicacions domèstiques\.

![](img%5C57%20-%20Circuits%20electr%C3%B2nics8.png)

![](img%5C57%20-%20Circuits%20electr%C3%B2nics9.png)