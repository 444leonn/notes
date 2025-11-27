---
base: "[[Organizacion del Computador.base]]"
Fecha: 2025-11-10T08:04:00
Descripción: • Arquitectura Von-Neumann
Diapos:
  - 2a73f454-0dd6-8090-8d5d-c69357d90aec
  - 2a73f454-0dd6-808a-bedc-d0403b0448bd
---
# Arquitectura de una Computadora

![[image 62.png]]

## Bus del Sistema

- **Bus de Datos**: trasporta la información que se está trasmitiendo
- **Bus de Direcciones**: determina hacia donde está siendo enviada dicha información.
- **Bus de Control**: describe aspectos de la forma en que se está llevando a cabo la mencionada
trasferencia de información.

# Arquitectura de Von-Neumann

John Von Neumann fue un matemático húngaro-estadounidense que realizó contribuciones fundamentales en física cuántica, análisis funcional, teoría de conjuntos, teoría de juegos, ciencias de la computación, economía, análisis numérico, cibernética, hidrodinámica, estadística y muchos otros campos.
Se le considera uno de los matemáticos más importantes del siglo XX.

![[diagrama-von-neumann.png]]

## Registros

- **Acumulador ***ACC*: Es el registro más utilizado para almacenar datos tomados de la memoria.
- **Registros de Direcciones de Memoria** (*MAR*): Contiene la dirección de la ubicación a la que sepuede acceder desde la memoria. MAR y MDR (Memory Data Register) juntos facilitan lacomunicación de la CPU y la memoria principal.
- **Registros de Datos de Memoria** (*MDR*): Contiene datos que se escriben o se leen desde laubicación direccionada.
- **Registros de Propósito General**: Estos están numerados como R0, R1, R2....Rn-1, y se utilizan paraalmacenar datos temporales durante cualquier operación en curso.
- **Contador de Programa** (*PC*): El contador de programa (PC) se utiliza para realizar un seguimientode la ejecución del programa. Contiene la dirección de memoria de la siguiente instrucción que seva a obtener.
- **Registro de Instrucciones **(*IR*): El IR contiene la instrucción que está a punto de ejecutarse. Lainstrucción de la PC se obtiene y se almacena en IR. Tan pronto como la instrucción se coloca enIR, la CPU comienza a ejecutar la instrucción y la PC apunta a la siguiente instrucción que se vaa ejecutar.
- **Puntero de Pila** (*SP*): El Stack Pointer apunta a la parte superior de la pila, que es una parte dela memoria utilizada para almacenar llamadas a funciones y otras operaciones.
- **Registro de Flags** (*banderas*): también conocido como registro de estado o registro de códigode condición, es un tipo especial de registro en la unidad central de procesamiento (CPU) deuna computadora que se utiliza para indicar el estado de la CPU o el resultado de varias operaciones.

# Unidad Central de Procesamiento

Es un componete del Hardwaredentro de una computadora.

Su función es interpretar las instrucciones de un programa informático mediante la realización de las operaciones básicas aritméticas, lógicas, y externas (procedentes de la unidad de entrada/salida).

## Componentes

- **Unidad aritmético-lógica** (*ALU, Arithmetic Logic Unit*): realiza operaciones aritméticas y lógicas.
- **Unidad de control** (*CU*): maneja la información entre los registros de la CPU y conecta con la ALU las instrucciones extraídas de la memoria.
- **Registros internos**: no accesibles (de instrucción, de bus de datos y bus de dirección) y accesibles de uso específico (contador programa, puntero pila, acumulador, flags, etc.) o de uso general.

![[image 64.png]]

### Memoria Principal (RAM)

La memoria principal denominada **RAM** (Random Access Memory, o Memoria de Acceso Aleatorio) *es la encargada de almacenar* todo tipo de datos, instrucciones o información en el CPU *mientras está en proceso de funcionamiento*.

Pero cuando se apaga pierde todo el tipo de información ya almacenada lo que contribuye que este tipo de memoria sea volátil.

En la RAM se cargan todas las instrucciones que ejecuta la unidad central de procesamiento (CPU) y otras unidades del ordenador, además de contener los datos que manipulan los distintos programas.

A la memoria RAM se la llama de <u>*acceso aleatorio*</u> porque se puede leer o escribir en una posición de memoria con igual tiempo de espera para cualquier posición, no requiriendo un orden para acceder (acceso secuencial) a la información de la manera más rápida posible

### Memoria Secundaria

La memoria secundaria o también conocida como memoria auxiliar o almacenamiento secundario, es el conjunto de dispositivos y soportes de almacenamiento de datos que conforman el subsistema de memoria de la computadora, junto con la memoria principal.
Este tipo de memoria *es de almacenamiento masivo y permanente (no volátil)*, con mayor capacidad para almacenar datos e información que la memoria primaria que es volátil, aunque la memoria secundaria es de menor velocidad.


T**ipos de Memoria Secundaria:**

- Magnética (disco duro, cinta magnética).
- Óptica (CD, DVD, BD).
- Magneto-óptica (Floptical, Minidisc).
- Estado sólido o memoria Flash (memoria USB o pendrive, tarjetas de memoria: SD, MiniSD, microSD, MS, MMC, entre otras).

### Entradas / Salidas (E/S)

Son aquellos periféricos de un computador que *permiten interactuar con la computadora, convirtiéndolo en un sistema bidireccional*, es decir, que permite tanto que sea ingresada información desde un sistema externo, como emitir información a partir de ese sistema.

Un periférico de E/S es el que se utiliza para ingresar (E) datos a la computadora, y luego de ser procesados por la unidad central de procesamiento (CPU), genera la salida (S) de información. Su función es leer o grabar, permanente o virtualmente, todo aquello que se haga con la computadora, para que pueda ser utilizado por los usuarios u otros sistemas.

Debe poder, como mínimo, direccionar los diferentes periféricos con los que puede establecer comunicación, establecer un sistema de comunicación entre el procesador y los controladores, y sincronizar los dispositivos de manera que no se produzcan inconsistencias o errores. Además, debería ser capaz de convertir los datos entre diferentes formatos, controlar el estado de los periféricos, llevar la cuenta de las transmisiones y tener un sistema de detección de errores.

### Buses

La función del bus es *permitir la conexión lógica entre los diferentes subsistemas que
componen el computador*.

En su mayoría los buses están formados por conductores metálicos por los cuales se transmiten señales eléctricas que son enviadas y recibidas con la ayuda de circuitos integrados que manejan un protocolo que les permite transmitir datos útiles.

Además de los datos el bus transmite otras señales digitales como son las direcciones y señales de control.

Todos los buses de computador tienen funciones especiales como las interrupciones que permiten que un dispositivo periférico acceda a una CPU o a la memoria usando el mínimo de recursos.

Una interrupción es un evento que hace que el microprocesador deje de realizar lo
que está haciendo y pase a ejecutar otra tarea. Al finalizar retorna a su actividad inicial.

La estructura de Buses se refiere a un sistema de vías de comunicación utilizadas para conectar varios componentes dentro de un ordenador, incluyendo la CPU, la memoria y los dispositivos de entrada/salida.

Los buses permiten la transferencia de datos, direcciones y señales de control entre estos componentes, garantizando un funcionamiento fluido y un uso eficiente de los recursos.

**Clasificación:**

-  *Bus de Datos*: Transporta datos entre la CPU, la memoria y los dispositivos de E/S.
- *Bus de Dirección*: Transmite la ubicación física (dirección) de los datos a los que la CPU debe acceder.
- *Bus de Control*: Transfiere señales de control para coordinar el funcionamiento global del sistema. 

En particular, cuanto más grande el bus de datos mayor es la capacidad de transporte de bits de datos dentro del microprocesador para comunicarse con la memoria o dispositivos de E/S.

Por otro lado, en el caso del bus de direcciones, a mayor capacidad, mayor capacidad de almacenamiento de memoria en el dispositivo. Esto en su conjunto, trae aparejado el aumento de performance de un procesador, cuestión que está ligada al diseño de la arquitectura del mismo.

## Secuencia de Instruccion

Hace referencia a los pasos que lleva a cabo la unidad de control en la ejecución de un programa

![[diagrama.svg]]

# Ley de Moore

La Ley de Moore, formulada por Gordon Moore en 1965, predice que la cantidad de transistores en un microprocesador se duplicará aproximadamente cada dos años, lo que resulta en un aumento exponencial en la potencia de procesamiento y una reducción de los costos de fabricación.

Esta observación ha sido un motor del progreso tecnológico, aunque se enfrenta a límites físicos y se han adaptado las arquitecturas (como los procesadores multinúcleo) para continuar su impulso.

# Arquitectura x86

El Intel 8086 pertenece al grupo de microprocesadores de 16 bits diseñados por Intel entre principios de 1976 y mediados de 1978.

- Tiene un bus de datos de 16 bits y memoria de 1MB
- Fuente de alimentación de +5v.
- La velocidad de reloj de la CPU es de 5MHz a 10MHz.
- Es un circuito integrado de 40 pines.
- Tiene ocho registros depropósito general, incluido el puntero de pila, el puntero base, el índice de origen y el índice de destino, registro de cuatro segmentos y un contador de programas.
- Tiene registro de 9 banderas (Flags).
- Corresponde a la arquitectura CISC (Complex Instruction Set Computing).

![[image 65.png]]

## Estructura

4 Registros de Proposito General:

- Acumulador (AX)
- Base (BX)
- Contador (CX)
- Datos (DX)
![[image 66.png]]

Otros Registros:

<!-- Column 1 -->
- Registros de índice: Source y Destination Index(SI / DI).

<!-- Column 2 -->
![[image 67.png]]

<!-- Column 1 -->
- Registros de punteros: Stack y Base Pointer (SP / BP).

<!-- Column 2 -->
![[image 68.png]]

<!-- Column 1 -->
- Registros de Segmento: utilizados para cálculo de direcciones.

<!-- Column 2 -->
![[image 69.png]]

- Registro de Flags

## Modos de Direccionamiento

Existen diversas formas de acceder a la dirección de los datos que se utilizan en las operaciones del microprocesador.

Cuando un micro como el 8086 ejecuta una instrucción, opera sobre datos que están alojados en la memoria.

Para acceder a ellos existen diversas técnicas que se denominan modos de direccionamiento

### Program Memory Addressing Mode

Este modo implica manejo de direcciones de memoria durante la ejecución de programa, acorde al registro PC que se va incrementando a medida que se ejecuta el mismo.

Ejemplo. JMP AX.

### Data Memory Addressing Mode

Este modo está relacionado con la operación de transferencia de datos, es decir, los datos se transfieren desde la memoria a registros internos del procesador o de un registro a otro.

Ejemplo MOV AX, DX.

### Stack Memory Addressing Mode

Este modo involucra el manejo de las operaciones de la pila.

Ejemplo. PUSH AX.

Sin embargo podemos condensarlo en 6 opciones distintas.

### Inmediato (Inmediate Memory Addressing)

En este modo de direccionamiento, uno de los operandos está presente directamente en el código de lainstrucción.

Ejemplo: MOV AX, 38h

*Uso*: este tipo de instrucción con direccionamiento directo sirve por ejemplo para cargar valores constantes en unregistro.

### Directo (Direct Memory Addressing)

En este caso se especifica directamente la dirección de memoria desde la cual se va a leer o escribir un dato.Este tipo de direccionamiento se usa para acceder a datos en una posición de memoria específica.

Ejemplo: MOV AX, [1325h]

*Uso*: este direccionamiento es un modo sencillo para acceder a ubicaciones específicas en la memoria, usandouna dirección constante de 16 bits en la instrucción. Es útil cuando se conoce de antemano la ubicación de losdatos en la memoria.

### Directo Indexado (Direct, Indexed Memory Addressing)

El direccionamiento directo indexado es una forma de direccionamiento en la que se utiliza un desplazamientobase junto con un índice para calcular la dirección de memoria final.

En este modo, la dirección de memoria esdeterminada mediante la suma de una dirección base y un valor contenido en un registro índice especificado, pudiendo ser el “SI” (Source Index) o “DI” (Destination Index).

Ejemplo: MOV AX, [1325h + SI]

Utilizando nuevamente la instrucción MOV, en este caso 1325h es la dirección base. “SI” es el registro índiceque se utiliza para realizar un desplazamiento adicional. La dirección efectiva de memoria será (1325h + SI),y el contenido de esa dirección se copiará al registro AX.

*Uso*: permite acceder a cualquier ubicación dentro de un bloque de datos utilizando un índice, lo que es útilpara acceder a memoria cuando los datos están organizados de manera secuencial o estructurada, como porejemplo en el manejo de tablas.

### Implícito (Implied Memory Addressing)

El direccionamiento implícito, tal como su nombre lo indica, no especifica una dirección de memoria ni se utilizaun registro para almacenar la dirección. 

En este caso, los operandos son implícitos dentro de la propia instrucción, y no es necesario proporcionar unadirección o un registro en el código de la instrucción.

Este tipo de direccionamiento es simple y se utiliza principalmente cuando la operación involucra registrospredefinidos o direcciones estándar que no necesitan ser especificadas en la instrucción. 

Ejemplo: CLC {Hace Clear en el bit de Carry del Registro de Flags}

*Uso*: Este tipo de direccionamiento simplifica la escritura del código, ya que no se requiere especificar losoperandos explícitamente. No se especifica la dirección de memoria ni el registro a operar explícitamente, porque estos son implícitos en la operación.

Algunas instrucciones de Intel 8086 utilizan direccionamiento implícito, como las instrucciones que afectan al acumulador, registro de Flags o registros especiales.

### Base Relativa (Base Relative Memory Addressing)

El direccionamiento base relativa es un modo de direccionamiento que se utiliza para calcular una direcciónmediante la combinación del registro base “BX” que contiene el valor base de la dirección efectiva más undesplazamiento. 

Este tipo de direccionamiento es comúnmente utilizado para acceder a datos dentro deestructuras de datos como arreglos o variables locales en la memoria. 

Ejemplo: MOV AX, [BX + 4h]

El valor Base se encuentra en un registro que contiene una dirección de memoria (generalmente el “BX”), y el desplazamiento (offset), que se suma como valor constante a la dirección base, para obtener la direcciónfinal.

Dirección efectiva = Base + Desplazamiento.

*Uso*: permite acceder a ubicaciones de memoria calculadas mediante un registro base y un desplazamiento, lo que facilita el acceso a parámetros dentro de estructuras de memoria. Es muy útil por ejemplo en programación de funciones.

### Pila (Stack Memory Addressing)

Este es un modo de direccionamiento que permite acceder a datos almacenados en la pila, en generalutilizando las instrucciones de POP y PUSH.

La pila se usa comúnmente para almacenar valores temporales,direcciones de retorno de funciones, entre otras. En el Intel 8086, el direccionamiento de pila se manejaprincipalmente a través del registro de puntero de pila (SP) y el registro de base de pila (BP).

El SP apuntaal tope de la pila y el BP se utiliza comúnmente para acceder a las variables locales de una función. 

Ejemplo: PUSH AX Supongamos que AX=1234h y el SP=2000h.

Entonces el valor 34h se guardará en el 1999h y el valor 12h hará lo propio en la posición 1998h.

El byte superior de datos se almacenará en la ubicación SP-1 y el byte inferior de datos se almacenará en la ubicación de memoria SP-2.
*Uso*: Las instrucciones que se utilizan para manipular la pila en el 8086 son PUSH y POP, entre otras. Estasinstrucciones afectan directamente a los registros SP y BP.

Facilita la manipulación de la pila para pasar parámetros y almacenar valores temporales, en especialdurante las llamadas y retornos de funciones.