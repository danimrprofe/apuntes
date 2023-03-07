---
title: Pygame
footer: Daniel Moreno 🌐 <github.com/danimrprofe>
_footer: ""
paginate: true
_paginate: false
_class: invert
marp: true
---

## 1. Introducció

1.1. Característiques técnlques de I'aire comprimit
1.2. Magnituds i unitats

---

# Pressió

La pressió de l'aire comprimit es mesura en bar (abreviatura de barra), on 1 bar equival a 100.000 pascals (Pa). Altres unitats comunes inclouen lliures per polzada quadrada (psi) i kilopascals (kPa).

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

---

## 5. Actuadors pneumàtics

---

## Motors

5.1. Motors
5.2 . Cilindres
5.3. Aplicacions deis actuadors pneumàtics

---

## 6. Elements de distribució o vàlvules

6.1. La válvula 2/2
6.2. La válvula 3/2
6.3. La válvula 5/2

---

## 7. Altres vàlvules

---

## 8. Exemples de circuits

---

## 9. Hidràulica

---

### 1. Els líquids no es poden comprimir
Els sistemes hidràulics són similars als sistemes pneumàtics que hem estudiat a les miniunitats anteriors. Els dos utilitzen els mateixos tipus de components: cilindres i motors rotatius com ara actuadors, canonades i vàlvules que controlen el circuit, i compressors o bombes que transmeten energia als fluids.

---

Però també tenen importants diferències. La principal és que mentre que els sistemes pneumàtics utilitzen un gas (aire comprimit) per transmetre moviment i força, els sistemes hidràulics utilitzen un líquid, l'oli hidràulic, que és un tipus d'oli mineral (olis extrets del petroli).

---

Els líquids no són compressibles: si sotmetem a pressió un líquid tancat en un recipient, aquest no es comprimirà, cosa que sí passarà amb els gasos, com l'aire. Com veurem a les pàgines següents, això confereix molts avantatges als sistemes hidràulics en les seves aplicacions tecnològiques... I també algun desavantatge.

Els líquids, com l'aigua o l'oli, no es poden comprimir.

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

Aplicant el fenomen que hem vist a la pàgina anterior, els sistemes hidràulics poden generar una força enorme. Aquesta característica s'utilitza en tot tipus de màquines que requereixen gran potència, com excavadores, tractors, maquinària de la construcció, camions, grues, etc. En aquestes màquines, el cilindre de petit diàmetre (veure pàgina anterior) se substitueix per una bomba impulsada per un motor de combustió o un motor elèctric.

---

La ``pala`` d'aquesta excavadora utilitza un sistema hidràulic que és capaç de generar una força enorme.
En lloc d'utilitzar dos cilindres (un de petit i un de gran) per multiplicar la força, en aquesta màquina el cilindre petit se substitueix per una bomba hidràulica accionada per un motor.

---

### 5. Els cilindres hidràulics poden aturar-se en qualsevol punt del seu recorregut

Les imatges corresponen a dues grues, la funció de les quals és aixecar càrregues pesades de forma segura. Això és possible gràcies a l'ús de cilindres hidràulics, que poden aturar-se a qualsevol punt del recorregut, ja que l'oli que hi ha al seu interior no és compressible. Una grua de cilindres pneumàtics no serial segura ja que l'aire pot comprimir-se, per la qual cosa els cilindres es mourien bruscament en agafar o deixar una càrrega.

Els cilindres hidràulics d'aquesta grua poden aixecar molt de pes i aturar-se en qualsevol altura.
El braç d'aquesta grua funciona gràcies a diversos cilindres hidràulics.

---

### 6. Els actuadors hidràulics poden executar moviments de gran precisió

Els actuadors hidràulics (cilindres i motors rotatius) es poden moure amb precisió mil·limètrica, aturar-se en qualsevol punt del seu recorregut i exercir o suportar força en una posició estàtica. Això els fa molt útils en el disseny de tot tipus de màquines industrials, com els braços robòtics que apareixen en aquesta pàgina.

Molts robots industrials es mouen utilitzant actuadors hidràulics (cilindres i motors rotatius).

Els robots utilitzats en la fabricació en cadena de cotxes han de moure's amb gran precisió, per aquesta raó la majoria d'ells són hidràulics.

---

### 7. Funcionament dels sistemes hidràulics accionats per bomba

Alguns sistemes hidràulics funcionen gràcies a la força exercida per una persona (els frens dels automòbils, els gats hidràulics que utilitzen els mecànics per aixecar cotxes als tallers, etc.), tot i que la gran majoria estan accionats per una bomba connectada a un motor. En màquines industrials, com les premses, s'utilitza un motor elèctric i en vehicles pesants, com les excavadores o les grues, és el mateix motor de combustió del vehicle el que impulsa la bomba. Un dels circuits accionats per bomba més senzill és el que hi ha als camions amb bolquet, com el que pots veure en aquesta pàgina.

Cilindre
hidràulic

Detall del cilindre que aixeca el bolquet d'un camió. És un cilindre telescòpic, perquè ocupi poc espai quan està en repòs.

En aquesta animació pots veure l'estructura d'un sistema hidràulic impulsat per bomba. Una bomba hidràulica (una bomba d'engranatges) impulsa l'oli que prové d'un dipòsit. L'oli s'envia als actuadors, en el cas de l'exemple de sota és un cilindre. Una vàlvula distribuïdora controla el moviment del cilindre fent que l'oli circuli en un sentit o en un altre.

Per pujar el bolquet cal empènyer la palanca cap endavant. L'oli entra al cilindre per la part inferior i l'èmbol puja, aixecant el bolquet. En arribar al final, s'ha de posar la palanca al centre, posició que talla el flux d'oli al circuit de treball
de
l'oli
i fa que la vàlvula de seguretat permeti la
la circulació pel circuit principal.

---

### 8. Inconvenients de la hidràulica respecte de la pneumàtica

El principal inconvenient dels sistemes hidràulics respecte dels pneumàtics és que són circuits tancats.

L'oli no es pot escapar del circuit (sí, però, l'aire comprimit), cosa que provoca que els seus components siguin més difícils i cars de construir i, tinguin un manteniment més complex.

---

Moltes de les aplicacions hidràuliques són de gran potència, com aral l'excavadora de la foto. Com que ha de suportar majors pressions internes i esforços externs, els seus components han de ser molt més reforçats i per tant més cars, encara que això no és tant un desavantatge, sinó una conseqüència del tipus de tasca per a la qual estan dissenyats.

Fotografia d'un cilindre hidràulic. Els components hidràulics són més cars i requereixen un manteniment més complex que els que funcionen amb aire comprimit.
Els sistemes hidràulics de gran potència, com aquesta excavadora, s'han de construir de forma molt robusta perquè puguin resistir esforços enormes.
