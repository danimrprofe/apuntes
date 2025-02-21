# **Transistors (I)**

![Circuit electrònic](img%5C57%20-%20Circuits%20electr%C3%B2nics3.png)

![Circuit electrònic](img%5C57%20-%20Circuits%20electr%C3%B2nics4.png)

## **1. Funcions del transistor**
Un transistor és un component electrònic que pot realitzar dues funcions principals:
- **Amplificar senyals elèctriques**: S'utilitza en circuits d'àudio, ràdio i electrònica en general.
- **Actuar com a interruptor**: Controla el pas de corrent en circuits digitals i de potència.

## **2. Tipus de transistors**
Els transistors més comuns es classifiquen en:
- **Bipolars (BJT - Bipolar Junction Transistor)**
- **De efecte de camp (FET - Field-Effect Transistor)**

## **3. Transistors bipolars**
Els transistors bipolars estan formats per **tres capes** de material semiconductor i tenen **tres terminals**:
1. **Base (B)**: Controla el flux de corrent.
2. **Col·lector (C)**: Rep el corrent d'entrada.
3. **Emissor (E)**: Expulsa el corrent cap al circuit.

### **3.1. Tipus de transistors bipolars**
- **NPN**
  - Té una capa de semiconductor **P** situada entre dues capes de semiconductor **N**.
  - La base s'activa aplicant un petit corrent positiu respecte a l'emissor.
  - Permet el pas de corrent del col·lector a l’emissor.
- **PNP**
  - Té una capa de semiconductor **N** situada entre dues capes de semiconductor **P**.
  - La base s'activa aplicant un petit corrent negatiu respecte a l'emissor.
  - Permet el pas de corrent de l’emissor al col·lector.

![Tipus de transistors](img%5C57%20-%20Circuits%20electr%C3%B2nics5.png)

# **Configuracions de transistors**

Els transistors poden connectar-se en diferents configuracions segons l'ús en el circuit.

## **1. Emissor comú**
- Configuració més utilitzada en circuits d’amplificació i interruptors.
- Proporciona **guany de tensió i corrent**.
- Té una **alta impedància d'entrada** i una **baixa impedància de sortida**.

## **2. Col·lector comú**
- També coneguda com a **seguidor d’emissor**.
- No proporciona guany de tensió, però **augmenta el guany de corrent**.
- Té **baixa impedància de sortida**, útil per adaptar impedàncies en circuits d'àudio i senyal.

## **3. Base comuna**
- Té **guany de tensió**, però **no de corrent**.
- S’utilitza en aplicacions d’alta freqüència i amplificadors de radiofreqüència.

# **Transistors (II)**

![Diagrama transistor](img%5C57%20-%20Circuits%20electr%C3%B2nics6.png)

## **Modes de funcionament del transistor bipolar**
Els transistors bipolars poden operar en tres modes diferents segons la tensió aplicada:

- **Tall**
  - No es subministra prou corrent a la base.
  - El transistor es comporta com un **interruptor obert** i bloqueja el pas de corrent entre col·lector i emissor.

- **Saturació**
  - La base rep suficient corrent perquè flueixi la màxima corrent entre col·lector i emissor.
  - El transistor es comporta com un **interruptor tancat**.

- **Activa**
  - La base rep un corrent inferior al de saturació.
  - Permet el control de la intensitat del corrent de sortida en aplicacions d'amplificació.

## **Guany d'un transistor**
El **guany de corrent (β)** es defineix com la relació entre el corrent del col·lector (**Ic**) i el corrent de la base (**Ib**):
\[
\beta = \frac{I_c}{I_b}
\]
