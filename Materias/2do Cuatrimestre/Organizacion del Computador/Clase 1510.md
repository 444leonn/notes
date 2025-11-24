---
base: "[[Organizacion del Computador.base]]"
Fecha: 2025-11-05T18:59:00
Descripción: |-
  • Caso de Estudio INTEL
  • Registros 
  • Pseudo-Instrucciones e Instrucciones
Diapos:
  - 2a23f454-0dd6-805b-b20a-ddf0d256b8d1
---
## Temas

---

# ISA (Instruction Set Architecture)

## Registros

---

## Modos de Direccionamiento

---

## Tipos de Dato y Memoria

---

## Endianness

---

# NASM (Netwide Assembler)

---

### Estructura de un Programa

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

### Definición y Reserva de Campos de Memoria

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

```assembly
; Reserva de memoria
campo1 resb 1           ; 1 byte
campo2 resb 2           ; 2 bytes
campo3 resw 1           ; 2 bytes
campo4 resw 2           ; 4 bytes
campo5 resd 1           ; 4 bytes
vector1 times 2 resb 2  ; 4 bytes
vector2 times 3 resw 2  ; 12 bytes

; Definición con contenido inicial - Numéricos
decimal1 db 11          ; Memoria: 0B
decimal2 dw -11         ; Memoria: F5 FF
decimal3 dd 12345       ; Memoria: 39 30 00 00
hexa1 db -0Bh           ; Memoria: F5
hexa2 dw 0Ch            ; Memoria: 0C 00

; Definición con contenido inicial - Caracteres
letra db 'A'            ; Memoria: 41
cadena db 'hola'        ; Memoria: 68 6F 6C 61
numero db '12'          ; Memoria: 31 32
vector1 times 3 db 'A'  ; Memoria: 41 41 41
vector2 times 3 db 'A',0 ; Memoria: 41 00 41 00 41 00

```

---

### Macros

Secuencias de instrucciones asignadas a un nombre que pueden usarse en cualquier parte del programa.

**Sintaxis:**

```assembly
%macro macro_name number_of_params
    <macro body>
%endmacro

```

**Ejemplo sin parámetros:**

```assembly
%macro LIMPIAR_PANTALLA 0
    mov eax, 4
    mov ebx, 1
    ; ... instrucciones
%endmacro

```

**Ejemplo con parámetros:**

```assembly
%macro ESCRIBIR 1
    mov eax, 4
    mov ebx, 1
    mov ecx, %1
    ; ... instrucciones
%endmacro

```

---

### Inclusión de Archivos

**Sintaxis:**

```assembly
%include "file_name"

```

---

# Instrucciones

# Conceptos Generales

---

## Validación

---