---
title: Pygame
footer: Daniel Moreno 🌐 <github.com/danimrprofe>
_footer: ""
paginate: true
_paginate: false
_class: invert
marp: true
---

# 1. Introducció

---

# 1.1. Característiques técniques de I'aire comprimit

L’aire atmosfèric és un element de la natura que es pot fer servir com a agent de ``transport d’energia`` en els processos amb aplicacions industrials pneumàtiques, ja que aquest gas no és inflamable i es pot comprimir bé.

---

Com tots els gasos, l’aire es pot comprimir notablement a través d’una acció mecànica exterior que el pot fer agafar una ``pressió`` determinada.

---

# 1.2. Magnituds i unitats

---

# Pressió

La pressió de l'aire comprimit es mesura en ``bar`` (abreviatura de barra), on 1 bar equival a 100.000 pascals (Pa).
Altres unitats comunes inclouen lliures per polzada quadrada (psi) i kilopascals (kPa).

---

![bg contain](img/2023-03-08-11-35-45.png)

---

![bg contain](img/2023-03-08-11-36-56.png)

---

![bg contain](img/2023-03-08-11-38-41.png)

---

![bg contain](img/2023-03-08-11-40-28.png)

---

## 2. Circuit pneumàtic

![](img/2023-03-03-07-59-59.png)

---

## 3. Grup compressor

El grup compressor és un conjunt de components que treballen junts per comprimir i emmagatzemar aire comprimit. Aquests components inclouen:

![](img/2023-03-03-08-00-25.png)

![](img/2023-03-03-08-00-44.png)

---

# 3.1. El compressor:

El compressor és el cor del grup compressor i és lencarregat de comprimir laire. Hi ha diversos tipus de compressors, com els de pistó, els de cargol i els de paletes, cadascun amb els seus propis avantatges i desavantatges.

---

![bg contain](img/2023-03-08-11-42-26.png)

---

Una utilització pràctica del compressor seria per pintar:

![](img/2023-03-08-16-39-21.png)

---

![bg contain](img/2023-03-08-11-45-41.png)

---

# 3.2. El motor auxiliar:

El motor auxiliar és lencarregat de proporcionar lenergia necessària per fer funcionar el compressor. Pot ser elèctric, dièsel o benzina, depenent de l'aplicació i la disponibilitat d'energia.

---

# 3.3. El refrigerador:

El refrigerador és un component que s'utilitza per refredar l'aire comprimit després que s'ha comprimit. Això ajuda a reduir la temperatura de l'aire i eliminar la humitat, cosa que ajuda a prevenir la corrosió i altres problemes associats amb l'aire humit.

---

# 3.4. El dipòsit:

El dipòsit és el lloc on s'emmagatzema l'aire comprimit. Pot ser un tanc vertical o horitzontal i la mida dependrà de la quantitat d'aire que cal emmagatzemar per satisfer les necessitats de l'aplicació.

---

# 3.5. La unitat de manteniment:

La unitat de manteniment és un conjunt de components que sutilitza per mantenir laire comprimit net i sec. Inclou filtres dʻaire, reguladors de pressió i lubricadors dʻaire que ajuden a garantir la qualitat de lʻaire comprimit i prolonguen la vida útil del sistema.

---

## 4. Canonades

![bg contain](img/2023-03-08-11-45-41.png)

---

## Actuadors

---

# Cilindres

![](img/2023-03-08-11-51-54.png)

---

## 6. Vàlvules

Pel control dels actuadors pneumàtics, com els cilindres, és necessari disposar d’elements de comandament com són les ``vàlvules``.

![](img/2023-03-08-11-54-24.png)

---

Les vàlvules distribuïdores són les que envien l’aire comprimit a una o altra part de la instal·lacióperquè es faci l’avanç i el retrocés del cilindres pneumàtics en el moment desitjat.

---

# Nomenclatura

Per donar nom a les vàlvules es fa servir el nombre de vies (sortides i entrades) que té i el nombre de posicions que pot adoptar. Així parlem per exemple d'una vàlvula 4/2, que significa que té 4 vies i dues posicions.

---

# Representació

Per representar les vàlvules es fan servir rectangles per les posicions i fletxes o taps a les vies. Una vàlvula 4/2, es representarà amb dos rectangles i quatre punts d'entrada-sortida d'aire, així:

![](img/2023-03-08-08-07-53.png)

---

## 9. Hidràulica

---

### 1. Els líquids no es poden comprimir

Els sistemes hidràulics són similars als sistemes pneumàtics. Però també tenen importants diferències.

---

La principal és que mentre que els sistemes ``pneumàtics`` utilitzen un ``gas`` (aire comprimit) per transmetre moviment i força, els sistemes ``hidràulics`` utilitzen un ``líquid``, l'oli hidràulic, que és un tipus d'oli mineral (olis extrets del petroli).

Els dos utilitzen els ``mateixos tipus de components``: cilindres i motors rotatius com ara actuadors, canonades i vàlvules que controlen el circuit, i compressors o bombes que transmeten energia als fluids.

---

# Diferència gas i líquid

Els líquids no són compressibles: si sotmetem a pressió un líquid tancat en un recipient, aquest no es comprimirà, cosa que sí passarà amb els gasos, com l'aire.

Els líquids, com l'``aigua`` o l'``oli``, no es poden comprimir.

---

### 2. Frens hidràulics

Els frens dels automòbils, motos o bicicletes són un exemple de sistema hidràulic. En trepitjar el pedal de fre, un pistó exerceix força contra un líquid, el ``líquid de frens``. El fluid transmet la força fins als frens, situats a les rodes. A cada fre, un o diversos pistons reben la força i l'apliquen contra l'eix de la roda, per tal d'aturar-la o reduir-ne la seva velocitat.

A les rodes davanteres s'utilitzen ``frens de disc``, formats per un disc d'acer i pastilles de fre. A les rodes posteriors se solen utilitzar frens de tambor, compostos per sabates de fre i un tambor giratori solidari a la roda.

---

### 3. Un sistema hidràulic pot multiplicar la força, com una palanca

Els sistemes hidràulics, a diferència dels pneumàtics, són ``tancats``. El líquid que hi ha a l'interior no es perd. Això, unit al fet que en ser un líquid és incompressible, fa que un sistema hidràulic compost per un cilindre de superfície petita i un cilindre de superfície gran es comporti com una ``palanca``.

---

En fer una petita força al cilindre petit (a l'animació, representada pel pes d'una formiga), obtenim una gran força al cilindre gran (el pes de l'elefant). La força obtinguda es pot calcular utilitzant la fórmula que es mostra a sota. A canvi d'obtenir més força, el desplaçament que ha de realitzar el cilindre petit és molt més gran del que realitzarà el cilindre gran.

---

### 4. Els sistemes hidràulics poden generar forces enormes

Els sistemes hidràulics poden generar una força enorme. Aquesta característica s'utilitza en tot tipus de màquines que requereixen gran potència, com excavadores, tractors, maquinària de la construcció, camions, grues, etc.

En aquestes màquines, el ``cilindre`` de petit diàmetre se substitueix per una ``bomba`` impulsada per un ``motor`` de combustió o un motor elèctric.

---

# Excavadora

La ``pala`` d'aquesta excavadora utilitza un sistema hidràulic que és capaç de generar una força enorme.
En lloc d'utilitzar dos cilindres (un de petit i un de gran) per multiplicar la força, en aquesta màquina el cilindre petit se substitueix per una bomba hidràulica accionada per un motor.

---

![bg contain](img/2023-03-08-12-12-39.png)

---

### Els cilindres hidràulics poden aturar-se en qualsevol punt del seu recorregut

Les imatges corresponen a dues grues, la funció de les quals és aixecar càrregues pesades de forma segura. Això és possible gràcies a l'ús de ``cilindres hidràulics``, que poden aturar-se a ``qualsevol punt` del recorregut, ja que l'oli que hi ha al seu interior no és compressible.

---

![w:700px](img/2023-03-08-12-10-56.png)

Els cilindres hidràulics d'aquesta grua poden aixecar molt de ``pes`` i aturar-se en qualsevol ``altura``. El braç d'aquesta grua funciona gràcies a diversos cilindres hidràulics.

---

Una ``grua de cilindres pneumàtics`` no seria segura ja que l'aire pot comprimir-se, per la qual cosa els cilindres es mourien bruscament en agafar o deixar una càrrega.

---

Els actuadors hidràulics (cilindres i motors rotatius) es poden moure amb ``precisió mil·limètrica``

També poden ``aturar-se en qualsevol punt`` del seu recorregut i exercir o suportar força en una posició estàtica.

---

Això els fa molt útils en el disseny de tot tipus de màquines industrials, com els ``braços robòtics``.

![](img/2023-03-08-12-09-24.png)

Els robots utilitzats en la ``fabricació en cadena de cotxes`` han de moure's amb gran precisió, per aquesta raó la majoria d'ells són hidràulics.

---

# Gats hidràulics

Alguns sistemes hidràulics funcionen gràcies a la força exercida per una persona (els frens dels automòbils, els ``gats hidràulics`` que utilitzen els mecànics per aixecar cotxes als tallers, etc.), tot i que la gran majoria estan accionats per una bomba connectada a un motor.

![](img/2023-03-08-12-04-40.png)

---

# Premses hidràuliques

En màquines industrials, com les ``premses hidràuliques``, s'utilitza un motor elèctric i en vehicles pesants, com les excavadores o les grues, és el mateix motor de combustió del vehicle el que impulsa la bomba.

---

![](img/2023-03-08-12-05-17.png)

---

Detall del cilindre que aixeca el ``bolquet`` d'un camió. És un cilindre telescòpic, perquè ocupi poc espai quan està en repòs.

![w:500px](img/2023-03-08-12-06-05.png)

---

Una ``bomba hidràulica`` (una bomba d'engranatges) impulsa l'oli que prové d'un dipòsit. L'oli s'envia als actuadors, en el cas de l'exemple de sota és un cilindre. Una vàlvula distribuïdora controla el moviment del cilindre fent que l'oli circuli en un sentit o en un altre.

![](img/2023-03-08-12-07-44.png)

---

### 8. Inconvenients de la hidràulica respecte de la pneumàtica

El principal inconvenient dels sistemes hidràulics respecte dels pneumàtics és que són circuits ``tancats``.

L'oli no es pot escapar del circuit (sí, però, l'aire comprimit), cosa que provoca que els seus components siguin més difícils i cars de construir i, tinguin un manteniment més complex.

---

Moltes de les aplicacions hidràuliques són de gran potència, com aral l'excavadora. Com que ha de suportar majors pressions internes i esforços externs, els seus components han de ser molt més reforçats i per tant més cars, encara que això no és tant un desavantatge, sinó una conseqüència del tipus de tasca per a la qual estan dissenyats.

![](img/2023-03-08-12-03-43.png)
