---
base: "[[Organizacion del Computador.base]]"
Fecha: 2025-11-07T11:26:00
Descripción: • Resumen de todo lo visto en el caso de Estudio Intel
Diapos: []
---
# Resumen

# Conceptos Más Importantes

# ISA (Instruction Set Architecture)

## Registros

### Registros Generales

| Tamaño | RAX | RBX | RCX | RDX |
| --- | --- | --- | --- | --- |
| 64 bits | RAX | RBX | RCX | RDX |
| 32 bits | EAX | EBX | ECX | EDX |
| 16 bits | AX | BX | CX | DX |
| 8 bits (alto) | AH | BH | CH | DH |
| 8 bits (bajo) | AL | BL | CL | DL |

**Funciones específicas:**

- **RAX (Acumulador)**: operando de instrucciones aritméticas y lógicas
- **RBX (Base)**: direccionamiento de operandos
- **RCX (Contador)**: operaciones aritméticas o de string
- **RDX (Data)**: operaciones que requieren duplas de registros

**Registros adicionales R8-R15:**

- 64 bits: R8, R9, ..., R15
- 32 bits: R8D, R9D, ..., R15D
- 16 bits: R8W, R9W, ..., R15W
- 8 bits: R8B, R9B, ..., R15B

### Registros Índice

| Tamaño | RSI | RDI |
| --- | --- | --- |
| 64 bits | RSI | RDI |
| 32 bits | ESI | EDI |
| 16 bits | SI | DI |
| 8 bits | SIL | DIL |

**Funciones:**

- **RSI (Source)**: operaciones de manejo de cadenas para apuntar al operando "origen"
- **RDI (Destination)**: operaciones de manejo de cadenas para apuntar al operando "destino"

### Registros de Pila

| Tamaño | RSP | RBP |
| --- | --- | --- |
| 64 bits | RSP | RBP |
| 32 bits | ESP | EBP |
| 16 bits | SP | BP |
| 8 bits | SPL | BPL |

**Funciones:**

- **RSP (Stack Pointer)**: dirección de memoria del tope de la pila
- **RBP (Base Pointer)**: dirección de memoria de la base de la pila

## Registros de Instrucción y Control

**RIP (Instruction Pointer)**

- 64 bits: RIP
- 32 bits: EIP
- 16 bits: IP
- Actúa como registro contador de programa (PC)
- Contiene la dirección efectiva de la instrucción siguiente que se ha de ejecutar

**RFlags (Flags)**

- 64 bits: RFlags
- 32 bits: EFlags
- 16 bits: Flags
- Almacena el estado general de la CPU
- Indica el resultado de la ejecución de cada instrucción

---

## Modos de Direccionamiento

1. **Implícito**: El dato está implícito en el código de operación
    - Ejemplo: `CBW`
2. **Registro**: El dato está en un registro
    - Ejemplo: `MOV RAX,5`
3. **Inmediato**: El dato está dentro de la instrucción
    - Ejemplo: `MOV RAX,5`
4. **Directo**: El dato está en memoria referenciado por el nombre de un campo
    - Ejemplo: `MOV RAX,[VARIABLE]`, `MOV RAX,[VARIABLE + 2]`
5. **Registro Indirecto**: El dato está en memoria apuntado por un registro base o índice
    - Ejemplo: `MOV EAX,[EBX]`, `MOV EAX,[ESI]`
6. **Registro Relativo**: El dato está en memoria apuntado por un registro base o índice más un desplazamiento
    - Ejemplo: `MOV RAX,[RBX+4]`, `MOV RAX,[VECTOR+RBX]`, `MOV [RDI+3],RAX`
7. **Base + Índice**: El dato está en memoria apuntado por un registro base más un registro índice
    - Ejemplo: `MOV [RBX+RDI],CL`
8. **Base Relativo + Índice**: El dato está en memoria apuntado por un registro base más un registro índice más un desplazamiento
    - Ejemplo: `MOV RAX,[RBX+RDI+4]`, `MOV RAX,[VECTOR+RBX+RDI]`

---

## Tipos de Dato y Memoria

### **Tipos de dato**

- **Numérico Entero**: Binario de punto fijo con Signo
- **Numérico Decimal**: Binario de punto Flotante IEEE
- **Caracteres**: ASCII

### **Memoria**

- Celda de Memoria: 1 Byte
- Palabra (Word): 2 Bytes
- Doble Palabra (Double Word): 4 Bytes
- Cuádruple Palabra (Quad Word): 8 Bytes

---

## Endianness

### **Definición**

Método aplicado para almacenar datos mayores a un byte en una computadora respecto a la dirección que se le asigna a cada uno de ellos en la memoria.

### Tipos:

**Big-Endian**:

- El orden en la memoria coincide con el orden lógico del dato
- "El dato final en la mayor dirección"
- Ejemplo: IBM Mainframe

**Little-Endian** (Intel):

- Es a la inversa, el dato inicial para la lógica se coloca en la mayor dirección y el dato final en la menor
- "El dato final en la menor dirección"

### Ejemplos

---

## NASM (Netwide Assembler)

### Directivas/Pseudo-instrucciones

| Directiva | Descripción |
| --- | --- |
| `section` | Indica el comienzo de un segmento |
| `global` | Indica que una etiqueta declarada es visible para un programa externo |
| `extern` | Indica que una etiqueta usada pertenece a un programa externo |
| `db, dw, dd, dq, dt` | Definen áreas de memoria con contenido inicial |
| `resb, resw, resd, resq, rest` | Definen áreas de memoria sin contenido inicial |
| `times` | Repite una definición la cantidad de veces que se indica |
| `%macro %endmacro` | Indican el inicio y final de un bloque para definir una macro |
| `%include` | Permite incluir el contenido de un archivo |

---

## Estructura de un Programa

```assembly
section .data
    ; Variables con contenido inicial

section .bss
    ; Variables sin contenido inicial

section .text
    global _start
_start:
    ; Código del programa

```

---

## Definición y Reserva de Campos de Memoria

### Con contenido inicial (section .data):

- `db` - define byte (1 byte)
- `dw` - define word (2 bytes)
- `dd` - define double (4 bytes)
- `dq` - define quad (8 bytes)
- `dt` - define ten (10 bytes)

### Sin contenido inicial (section .bss):

- `resb` - reserve byte (1 byte)
- `resw` - reserve word (2 bytes)
- `resd` - reserve double (4 bytes)
- `resq` - reserve quad (8 bytes)
- `rest` - reserve ten (10 bytes)

### Ejemplos:

---

## Macros

Secuencias de instrucciones asignadas a un nombre que pueden usarse en cualquier parte del programa.

### **Sintaxis**

```assembly
%macro macro_name number_of_params
    <macro body>
%endmacro

```

### Ejemplo

---

### Inclusión de Archivos

**Sintaxis:**

```assembly
%include "file_name"

```

---

# Instrucciones

## Transferencia y Copia

### MOV op1, op2

Copia el valor del 2do operando en el primer operando.

**Combinaciones:**

```assembly
; Registro a Registro
MOV AH,BL
MOV AX,BX
MOV ECX,EAX
MOV RDX,RCX

; Memoria a Registro
MOV CH,[VARIABLE_8]
MOV CX,[VARIABLE_16]
MOV ECX,[VARIABLE_32]
MOV RDX,[VARIABLE_64]

; Inmediato a Registro
MOV DL,7o
MOV CX,2450h
MOV EAX,0h

; Registro a Memoria
MOV [VARIABLE_8],AH
MOV [VARIABLE_16],AX
MOV VARIABLE_64,RAX

; Inmediato a Memoria
MOV byte[VARIABLE_8],2Ah
MOV word[VARIABLE_16],777o
MOV dword[VARIABLE_32],1234
MOV qword[VARIABLE_64],1234

```

### LEA op1, op2

Copia en el operando 1 (un registro) la dirección de memoria del operando 2.

```assembly
LEA RAX,[VARIABLE]
; Es equivalente a:
MOV RAX,VARIABLE  ; Sin corchetes

```

### MOVSB

Copia el contenido de memoria apuntado por RSI (origen) al apuntado por RDI (destino). Copia tantos bytes como los indicados en RCX.

```assembly
MOV RCX,4
LEA RSI,[MSGORI]
LEA RDI,[MSGDES]
REP MOVSB

```

### PUSH / POP

**PUSH op**: Inserta el operando (64 bits) en la pila. Decrementa RSP.
**POP op**: Elimina el último elemento de la pila y lo copia en el operando. Incrementa RSP.

```assembly
PUSH RDX
PUSH qword[VARIABLE]
POP RDX
POP qword[VARIABLE]

```

---

## Comparación

### CMP op1, op2

Compara el contenido del op1 contra el op2 mediante la resta entre los dos operandos sin modificarlos.

```assembly
; Registro con Registro
CMP AH,BL
CMP AX,BX
CMP EAX,EBX

; Registro con Memoria
CMP CH,[VARIABLE_8]
CMP CX,[VARIABLE_16]

; Registro con Inmediato
CMP CH,10o
CMP CX,2Ah

; Memoria con Registro
CMP VARIABLE,AX
CMP [VARIABLE_8],AH

; Memoria con Inmediato
CMP byte[VARIABLE_8],2Ah
CMP word[VARIABLE_16],2Ah

```

### CMPSB

Compara el contenido de memoria apuntado por RSI con el apuntado por RDI. Compara tantos bytes como los indicados en RCX.

```assembly
MOV RCX,4
LEA RSI,[MSG1]
LEA RDI,[MSG2]
REPE CMPSB
JE IGUALES

```

---

## Saltos/Bifurcaciones

### JMP op

Bifurca a la dirección indicada del operando.

```assembly
JMP finalizar

```

### Saltos Condicionales (Jcc op)

Bifurca si se cumple la condición.

**Condicionales generales:**

- `JE` - por igual (ZF=1)
- `JNE` - por no igual (ZF=0)
- `JZ` - por igual a cero (ZF=1)
- `JNZ` - por distinto a cero (ZF=0)
- `JRCXZ` - por contenido de RCX igual cero
- `JC` - por carry flag distinto a cero (CF=1)
- `JO` - por overflow (OF=1)

**Condicionales con signo:**

- `JG` - por mayor (ZF=0 and SF=OF)
- `JGE` - por mayor o igual (SF=OF)
- `JL` - por menor (SF≠OF)
- `JLE` - por menor o igual (ZF=1 or SF≠OF)

**Condicionales sin signo:**

- `JA` - por mayor (CF=0 and ZF=0)
- `JAE` - por mayor o igual (CF=0)
- `JB` - por menor (CF=1)
- `JBE` - por menor o igual (CF=1 or ZF=1)

### LOOP op

Resta 1 al contenido de RCX y si el resultado es distinto de 0, bifurca al punto indicado.

```assembly
mov rcx,5
inicio:
    ; ... instrucciones
    loop inicio

```

### CALL / RET

**CALL op**: Almacena en la pila la dirección de retorno y bifurca al punto indicado.
**RET**: Toma el elemento del tope de la pila y bifurca hacia esa dirección.

```assembly
call rutina
; ...
rutina:
    ; ... instrucciones
    ret

```

---

## Instrucciones Aritméticas

### ADD op1, op2

Suma los valores de los dos operandos (binarios de punto fijo con signo) dejando el resultado en el primero.

```assembly
ADD AH,BL
ADD AX,BX
ADD AL,[VARIABLE_8B]
ADD DL,10b
ADD VARIABLE_16,AX
ADD byte[RDI],245h

```

### SUB op1, op2

Resta los valores de los dos operandos dejando el resultado en el primero.

```assembly
SUB AH,BL
SUB AX,BX
SUB AL,[VARIABLE_8]
SUB DL,10b
SUB VARIABLE,AX
SUB byte[EDI],245h

```

### INC / DEC op

**INC**: Suma uno al operando
**DEC**: Resta uno al operando

```assembly
INC BH          ; BH = BH + 1
INC CX          ; CX = CX + 1
DEC EAX         ; EAX = EAX - 1
INC byte[VAR_8B]
DEC word[VAR_16B]

```

### Multiplicación

**Formato 1 operando: MUL/IMUL op**

- Si op es 8 bits: AX = AL * op
- Si op es 16 bits: DX:AX = AX * op
- Si op es 32 bits: EDX:EAX = EAX * op
- Si op es 64 bits: RDX:RAX = RAX * op

```assembly
MUL BH          ; AX = (AL)*(BH)
IMUL BX         ; DX:AX = (AX)*(BX)
MUL EBX         ; EDX:EAX = (EAX)*(EBX)
IMUL qword[VAR_64] ; RDX:RAX = (RAX)*(VAR_64)

```

**Formato 2 operandos: IMUL op1, op2**
Multiplica y almacena en op1. Si el resultado no entra, se trunca.

```assembly
IMUL CX,4               ; CX = (CX)*4
IMUL EAX,EBX            ; EAX = (EAX)*(EBX)
IMUL RBX,qword[VAR_64]  ; RBX = (RBX)*(VAR_64)

```

**Formato 3 operandos: IMUL op1, op2, op3**

```assembly
IMUL CX,BX,10h              ; CX = (BX)*10h
IMUL RBX,qword[VAR_64],4    ; RBX = (VAR_64)*4

```

### División: DIV/IDIV op

- Si op es 8 bits: AX/op → resto en AH, cociente en AL
- Si op es 16 bits: DX:AX/op → resto en DX, cociente en AX
- Si op es 32 bits: EDX:EAX/op → resto en EDX, cociente en EAX
- Si op es 64 bits: RDX:RAX/op → resto en RDX, cociente en RAX

```assembly
DIV BX          ; DX:AX / BX
IDIV EBX        ; EDX:EAX / EBX
DIV qword[VAR_64] ; RDX:RAX / [VAR_64]

```

### Conversión (expansión de signo)

- `CBW` - Convierte byte en AL a word en AX
- `CWD` - Convierte word en AX a double-word en DX:AX
- `CWDE` - Convierte word en AX a double-word en EAX
- `CDQE` - Convierte double-word en EAX a quad-word en RAX

```assembly
MOV AL,byte[VAR_8B]  ; AL = 9B
CBW                   ; AX = FF9B
CWDE                  ; EAX = FFFFFF9B
CDQE                  ; RAX = FFFFFFFFFFFFFF9B

```

### NEG op

Realiza el complemento a 2 del operando (cambia el signo).

```assembly
NEG BH
NEG AX
NEG byte[VAR_8]

```

---

## Instrucciones Lógicas

### AND op1, op2

Ejecuta la operación lógica AND entre los operandos, dejando el resultado en op1.

```assembly
AND AH,BL
AND AL,byte[VAR_8B]
AND CH,00h
AND word[VAR_16B],1010b

```

### OR op1, op2

Ejecuta la operación lógica OR entre los operandos.

```assembly
OR AH,BL
OR AL,byte[VAR_8B]
OR CH,00h
OR dword[VAR_32B],FFCC00AAh

```

### XOR op1, op2

Ejecuta la operación lógica EXCLUSIVE OR entre los operandos.

```assembly
XOR AH,BL
XOR AL,byte[VAR_8B]
XOR CX,250h

```

### NOT op

Ejecuta la operación lógica NOT en el operando.

```assembly
NOT AH
NOT BX
NOT byte[VAR_8B]

```

---

## Desplazamientos

### Desplazamientos Lógicos (unsigned)

**SHL op, count**: Desplazamiento a la izquierda, rellenando con ceros.
**SHR op, count**: Desplazamiento a la derecha, rellenando con ceros.

```assembly
SHL AH
SHL BX
SHR ECX
SHR word[VAR_16B]

```

### Desplazamientos Aritméticos (signed)

**SAL op, count**: Desplazamiento a la izquierda (igual que SHL).
**SAR op, count**: Desplazamiento a la derecha, preservando el signo.

```assembly
SAL AH
SAR BX
SAR dword[VAR_32B]

```

---

# Conceptos Generales

### Tablas

Tira de bytes en memoria destinada a usar como Vector o Matriz.

```assembly
tabla times 40 resb 1
vector times 10 resw 1
matriz times 25 db "*"

```

**Posicionamiento en vector:**

- Elemento i: `(i - 1) * longitudElemento`

**Posicionamiento en matriz:**

- Elemento i,j: `(i-1)*longitudFila + (j-1)*longitudElemento`
- longitudFila = longitudElemento * cantidadColumnas

**Ejemplo: Matriz 4x3 de double words**

```assembly
posx dd 02
posy dd 03
longfil dd 16
longele dd 4
matriz times 12 resd 1

mov rbx,matriz          ; puntero al inicio
mov rax,dword[posx]     ; fila
sub rax,1
imul dword[longfil]     ; desplazamiento en fila
add rcx,rax
mov rax,dword[posy]     ; columna
sub rax,1
imul dword[longele]     ; desplazamiento en columna
add rcx,rax
add rbx,rcx             ; posición final
mov dword[rbx],XXX      ; asignar valor

```

---

### Validación

Código destinado a verificar que los datos provenientes del exterior cumplen las condiciones esperadas.

### Clasificación según contenido:

- **Lógica**: que se adecúe al significado lógico
    - Ejemplo: Día de la semana: lunes, martes, etc.
    - Respuesta "S" o "N"
- **Física**: que el dato esté en un formato particular
    - Ejemplo: Campo en formato empaquetado
    - Fecha en formato DD/MM/AA

### Clasificación según mecanismo:

- **Por valor**: comparar contra uno o varios valores válidos
- **Por rango**: comparar que esté dentro de un rango continuo válido
- **Por tabla**: buscar que exista en una tabla de valores válidos

---

```assembly
MOV RCX, 10
inicio:
    ; ... código ...
    DEC RCX
    JNZ inicio      ; Salta si RCX no es cero

```

**Nota importante**: LOOP solo acepta saltos cortos (-128 a +127 bytes). Para bucles largos, usar DEC + JNZ.

---

## 7. Macros

**Definición básica**:

```assembly
%macro NOMBRE num_parametros
    ; código de la macro
%endmacro

```

**Ejemplo sin parámetros**:

```assembly
%macro LIMPIAR_REGISTROS 0
    XOR RAX, RAX
    XOR RBX, RBX
    XOR RCX, RCX
    XOR RDX, RDX
%endmacro

; Uso:
LIMPIAR_REGISTROS

```

**Ejemplo con parámetros**:

```assembly
%macro SUMAR_A_REGISTRO 2
    MOV RAX, %1        ; %1 = primer parámetro
    ADD RAX, %2        ; %2 = segundo parámetro
%endmacro

; Uso:
SUMAR_A_REGISTRO 10, 20    ; RAX = 10 + 20

```

**Macro con operaciones complejas**:

```assembly
%macro IMPRIMIR_CADENA 2
    MOV RAX, 1          ; syscall write
    MOV RDI, 1          ; stdout
    MOV RSI, %1         ; dirección del string
    MOV RDX, %2         ; longitud
    SYSCALL
%endmacro

; Uso:
IMPRIMIR_CADENA mensaje, 15

```

**Inclusión de archivos con macros**:

```assembly
%include "macros.asm"   ; Incluye archivo con definiciones

```

---

## 8. Subrutinas y Llamadas

### CALL y RET

```assembly
call subrutina       ; Guarda dirección de retorno en pila y salta
; ... código ...

subrutina:
    ; ... código de la subrutina ...
    ret             ; Recupera dirección de retorno y salta

```

### Uso de la Pila (Stack)

```assembly
; Guardar registros antes de usarlos
PUSH RAX
PUSH RBX
; ... usar RAX y RBX ...
POP RBX             ; Orden inverso (LIFO)
POP RAX

```

**Convención importante**:

- La pila crece hacia direcciones menores
- PUSH decrementa RSP
- POP incrementa RSP
- Siempre restaurar en orden inverso

---

## 9. Operaciones con Strings

### MOVSB - Copia de cadenas

```assembly
MOV RCX, 10         ; Número de bytes a copiar
LEA RSI, [origen]   ; Puntero al origen
LEA RDI, [destino]  ; Puntero al destino
REP MOVSB           ; Repite MOVSB RCX veces

```

### CMPSB - Comparación de cadenas

```assembly
MOV RCX, 5          ; Número de bytes a comparar
LEA RSI, [cadena1]
LEA RDI, [cadena2]
REPE CMPSB          ; Repite mientras sean iguales y RCX>0
JE son_iguales      ; Salta si todas fueron iguales

```

**Variantes**:

- `MOVSB` - mueve bytes
- `MOVSW` - mueve words (2 bytes)
- `MOVSD` - mueve double words (4 bytes)
- `MOVSQ` - mueve quad words (8 bytes)

---

## 10. Trabajo con Tablas/Arrays

### Vector Unidimensional

```assembly
vector times 10 dd 0    ; Vector de 10 elementos de 4 bytes

; Acceder al elemento i (base 0):
; dirección = base + i * tamaño_elemento

MOV RBX, vector         ; Base del vector
MOV RAX, 3              ; Índice (elemento 3)
MOV RCX, 4              ; Tamaño de cada elemento (dd = 4 bytes)
IMUL RAX, RCX           ; RAX = índice * tamaño
ADD RBX, RAX            ; RBX apunta al elemento 3
MOV dword[RBX], 100     ; Asignar valor

```

**Fórmula simplificada con registro índice**:

```assembly
MOV RBX, vector
MOV RDI, 3              ; Índice
MOV dword[RBX + RDI*4], 100  ; elemento[3] = 100

```

### Matriz Bidimensional

```assembly
; Matriz 4x3 (4 columnas, 3 filas) de double words
matriz times 12 resd 1

; Acceder a elemento[fila][columna] (base 1):
; posición = (fila-1) * longitud_fila + (columna-1) * longitud_elemento
; longitud_fila = num_columnas * longitud_elemento

; Ejemplo: elemento fila=2, columna=3
MOV RBX, matriz
MOV RAX, 2              ; Fila
SUB RAX, 1              ; Índice base 0
MOV RCX, 16             ; Long. fila = 4 columnas * 4 bytes
IMUL RAX, RCX           ; Desplazamiento por fila
MOV RDX, 3              ; Columna
SUB RDX, 1
IMUL RDX, 4             ; Desplazamiento por columna
ADD RAX, RDX            ; Desplazamiento total
ADD RBX, RAX            ; Posición final
MOV dword[RBX], 999     ; Asignar valor

```

---

## 11. Validación de Datos

### Validación por Valor

```assembly
; Validar que un carácter sea 'S' o 'N'
CMP AL, 'S'
JE valido
CMP AL, 'N'
JE valido
JMP invalido

valido:
    ; ... procesamiento ...
invalido:
    ; ... manejo de error ...

```

### Validación por Rango

```assembly
; Validar que un número esté entre 1 y 100
CMP AX, 1
JL fuera_rango          ; Si AX < 1
CMP AX, 100
JG fuera_rango          ; Si AX > 100
; ... AX está en rango válido ...

fuera_rango:
    ; ... manejo de error ...

```

### Validación por Tabla

```assembly
; Validar que un valor exista en una tabla
tabla db 10, 20, 30, 40, 50, 0  ; Tabla terminada en 0
valor db 30                      ; Valor a buscar

MOV RSI, tabla
MOV AL, byte[valor]

buscar:
    MOV BL, byte[RSI]
    CMP BL, 0               ; ¿Fin de tabla?
    JE no_encontrado
    CMP AL, BL              ; ¿Es el valor buscado?
    JE encontrado
    INC RSI                 ; Siguiente elemento
    JMP buscar

encontrado:
    ; ... valor válido ...
no_encontrado:
    ; ... valor inválido ...

```

---

## 12. Modos de Direccionamiento - Resumen Práctico

```assembly
; Inmediato
MOV AX, 100             ; AX = 100

; Registro
MOV AX, BX              ; AX = contenido de BX

; Directo
MOV AX, [variable]      ; AX = contenido en dirección 'variable'

; Registro Indirecto
MOV AX, [RBX]           ; AX = contenido en dirección apuntada por RBX

; Registro + Desplazamiento
MOV AX, [RBX + 4]       ; AX = contenido en (RBX + 4)
MOV AX, [vector + RBX]  ; AX = contenido en (dirección de vector + RBX)

; Base + Índice
MOV AX, [RBX + RDI]     ; AX = contenido en (RBX + RDI)

; Base + Índice + Desplazamiento
MOV AX, [RBX + RDI + 4]         ; AX = contenido en (RBX + RDI + 4)
MOV AX, [matriz + RBX + RDI]    ; Útil para matrices

```

---

## 13. Conversión y Extensión de Signo

**Problema común**: Al dividir, necesitamos extender el dividendo.

```assembly
; Si tenemos un valor de 16 bits en AX y queremos dividir
MOV AX, -10         ; AX = FFF6h (negativo)
MOV BX, 3
; ¡ERROR! DX contiene basura
; IDIV BX           ; Resultado incorrecto

; CORRECTO:
MOV AX, -10
CWD                 ; Extiende AX a DX:AX (DX = FFFF si AX negativo)
IDIV BX             ; Ahora DX:AX / BX funciona correctamente

```

**Instrucciones de conversión**:

```assembly
CBW     ; AL (8 bits) → AX (16 bits)
CWD     ; AX (16 bits) → DX:AX (32 bits)
CWDE    ; AX (16 bits) → EAX (32 bits)
CDQ     ; EAX (32 bits) → EDX:EAX (64 bits)
CDQE    ; EAX (32 bits) → RAX (64 bits)
CQO     ; RAX (64 bits) → RDX:RAX (128 bits)

```

---

## 14. Estructura Típica de un Programa

```assembly
section .data
    ; Variables inicializadas
    mensaje db 'Hola Mundo', 0
    numero dw 1234
    tabla times 10 dd 0

section .bss
    ; Variables no inicializadas
    buffer resb 100
    contador resd 1

section .text
    global _start

_start:
    ; Código principal

    ; Llamar a subrutina
    call mi_subrutina

    ; Salir del programa (Linux)
    MOV RAX, 60         ; syscall exit
    MOV RDI, 0          ; código de salida
    SYSCALL

mi_subrutina:
    PUSH RBP            ; Guardar base pointer
    MOV RBP, RSP        ; Establecer nuevo frame

    ; ... código de la subrutina ...

    MOV RSP, RBP        ; Restaurar stack pointer
    POP RBP             ; Restaurar base pointer
    RET

```

---

## 15. Consejos y Trampas Comunes

### ⚠️ Errores Frecuentes

9. **Olvidar el tamaño en operaciones con memoria**:

```assembly
; ❌ ERROR: Ambiguo
MOV [variable], 100

; ✅ CORRECTO: Especificar tamaño
MOV byte[variable], 100
MOV word[variable], 100
MOV dword[variable], 100

```

10. **Confundir dirección con contenido**:

```assembly
; ❌ ERROR: Copia la dirección, no el contenido
MOV RAX, variable

; ✅ CORRECTO: Copia el contenido
MOV RAX, [variable]

; Para copiar la dirección, usar LEA:
LEA RAX, [variable]

```

11. **No extender signo antes de dividir**:

```assembly
; ❌ ERROR: DX contiene basura
MOV AX, 100
IDIV BX

; ✅ CORRECTO:
MOV AX, 100
CWD                 ; Extiende AX a DX:AX
IDIV BX

```

12. **Desbalancear la pila**:

```assembly
; ❌ ERROR: PUSH sin POP correspondiente
PUSH RAX
PUSH RBX
POP RAX            ; ¡Incorrecto! Orden LIFO

; ✅ CORRECTO:
PUSH RAX
PUSH RBX
POP RBX
POP RAX

```

### 💡 Trucos Útiles

13. **Limpiar un registro rápidamente**:

```assembly
XOR RAX, RAX       ; Más rápido que MOV RAX, 0

```

14. **Multiplicar/dividir por potencias de 2**:

```assembly
SHL RAX, 3         ; RAX = RAX * 8 (más rápido que IMUL)
SHR RAX, 2         ; RAX = RAX / 4 (más rápido que DIV)

```

15. **Intercambiar valores sin registro temporal**:

```assembly
XOR RAX, RBX
XOR RBX, RAX
XOR RAX, RBX       ; RAX y RBX intercambiados

```

16. **Verificar si un registro es cero**:

```assembly
TEST RAX, RAX      ; Más eficiente que CMP RAX, 0
JZ es_cero

```

---

## Resumen Final - Lo Esencial

17. **Endianness**: Intel guarda bytes en orden invertido (little-endian)
18. **Registros**: RAX-RDX (general), RSI/RDI (strings), RSP/RBP (pila), RIP (instrucción)
19. **Tamaños**: byte(1), word(2), dword(4), qword(8)
20. **Operaciones básicas**: MOV, ADD, SUB, MUL, DIV, CMP, JMP, CALL, RET
21. **Bucles**: LOOP decrementa RCX automáticamente
22. **Macros**: Reutilizar código con %macro/%endmacro
23. **Arrays**: desplazamiento = índice * tamaño_elemento
24. **Pila**: PUSH/POP en orden LIFO
25. **Flags**: ZF (zero), CF (carry), SF (sign), OF (overflow)
26. **Validación**: Por valor, por rango, o por tabla

---