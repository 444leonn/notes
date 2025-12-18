---
base: "[[Organizacion del Computador.base]]"
Fecha: 2025-11-06T12:12:00
Descripción: • Assembler Embebido en C
Diapos:
  - 2a23f454-0dd6-8076-bac3-fbafb59f310b
---
# Assembler embebido en C — Resumen

> Fuente única: “Assembler embebido en C” (Pedro Ignacio Martos). Ejemplos y textos tomados del material.

## Formas de intercalar assembler en GCC

- Forma básica: secuencia GAS sin entradas/salidas explícitas. El compilador C no conoce sus efectos; se compila con `as`. Útil a nivel archivo o en funciones `naked`.
- Forma extendida: solo dentro de funciones C con `asm(...)`, permitiendo mapear variables de C a registros y declarar clobbers.

## Sintaxis de `asm()` extendido

```c
asm (
    /* assembler template (GAS) */
    : /* output operands (opcional) */
    : /* input operands  (opcional) */
    : /* clobbered registers list (opcional) */
);
```

## Assembler template (GAS)

- Registros con prefijo `%`. En templates con operandos, usar `%%` para registros literales y `%0`, `%1` para parámetros.
- Instrucciones equivalentes sin parámetros:
```c
asm ("movl %eax, %ebx");
asm ("movl %%eax, %%ebx");
```
- Con parámetros (copiar “a” en “b”):
```c
int a = 10, b;
asm ("movl %1, %0\n\t"
     "movl %%eax, %%ebx"
     : "=r"(b)     /* output */
     : "r"(a)      /* input  */
     : "%eax");    /* clobbered register */
```

## Output operands

- Asocian salidas del asm a variables C. Prefijo `=` indica que se escribe la variable.
- Literales frecuentes: `"r"` (registro genérico), `"g"` (registro o memoria), `"x"` (asignación libre).
- Ejemplo BSF:
```c
uint32_t Mask = 1234;
uint32_t Index;
asm ("bsfl %1, %0"
     : "=r"(Index)
     : "r"(Mask)
     : "cc");  // FLAGS modificados
```
- Si hay otros accesos a memoria además de E/S, agregar `"memory"` en clobbers.

## Input operands

- Mapean variables C como argumentos de instrucciones.
- Ejemplo con constraints específicas:
```c
int randomness = 4;
asm ("movl %0, %%eax"
     :
     : "b"(randomness)   // randomness en EBX
     : "eax");           // EAX modificado
```
- Lista completa de literales: GCC Simple Constraints.

## Clobbered register list

- Indicar registros afectados para que el compilador preserve su contenido.
- Ejemplo:
```c
asm volatile ("movc3 %0, %1, %2"
             : /* no outputs */
             : "g"(from), "g"(to), "g"(count)
             : "r0", "r1", "r2", "r3", "r4", "r5");
```
- `"cc"` para FLAGS, `"memory"` si hay efectos de memoria adicionales.

## Ejemplo: PF en assembler desde C

Código de multiplicación de arrays (fragmento tal como en la diapositiva):

```c
// Multiplicacion en C
for (i=0; i< 10; i++) {
    resultadoA[i] = arrayA[i] * constanteC;
}

// Multiplicacion en Assembler
i = 10;
asm (
    "movl %0, %%eax\n\t"
    "..."  // ver material para el bloque completo de instrucciones mostradas
    : "=c" (arrayB), "=r" (resultadoB), "=r" (constanteASM)
    : "eax", "mmx", "xmm1", "xmm2"
);
```

Salida observada: diferencias por precisión float vs. double.

## Uso de funciones escritas en assembler

- Prototipo en C, implementación en assembler.
- Calling convention del SO para parámetros y retorno.
- Portabilidad limitada entre Windows/Linux y entre x86_64/ARM64.

### Ejemplos

Archivos `sumaf.s` y `sumad.s` (GAS, extensión `.s`):

```assembly
# sumaf.s
.globl sumaf
.text
sumaf:
    xorps %xmm0, %xmm0     # inicializa a 0 xmm0
    cmp $0, %rsi           # elementos = 0?
    je fin
ciclo:
    addss (%rdi), %xmm0    # sumo el elemento actual (float)
    add $4, %rdi           # paso al siguiente elemento
    dec %rsi               # decremento contador
    jnz ciclo              # si no termine, vuelvo a sumar
fin:
    ret
```

```assembly
# sumad.s
.globl sumad
.text
sumad:
    xorpd %xmm0, %xmm0     # inicializa a 0 xmm0
    cmp $0, %rsi           # elementos = 0?
    je fin
ciclo:
    addsd (%rdi), %xmm0    # sumo el elemento actual (double)
    add $8, %rdi           # paso al siguiente elemento
    dec %rsi
    jnz ciclo
fin:
    ret
```

Archivo C `sumaDesdeC.c`:

```c
float sumaf (float[], unsigned int);
double sumad (double[], unsigned int);

int main(void) {
    float arreglof[6]  = {40.5, 26.7, 21.9, 1.5, -40.5, -23.4};
    double arreglod[6] = {40.5, 26.7, 21.9, 1.5, -40.5, -23.4};
    float resultadof; double resultadod;
    unsigned int cantElementos[4] = {6, 2, 0, 3};
    int i;
    for (i=0; i<4; i++) {
        resultadof = sumaf (arreglof, cantElementos[i]);
        printf("Se sumaron %d elementos float, el resultado es: %20.7f\n", cantElementos[i], resultadof);
        resultadod = sumad (arreglod, cantElementos[i]);
        printf("Se sumaron %d elementos double, el resultado es: %20.7f\n", cantElementos[i], resultadod);
        printf("\n");
    }
}
```

Compilación:

```bash
gcc -o sumaDesdeC -z noexecstack sumaDesdeC.c sumaf.s sumad.s
```

Salida de consola: muestra distinta precisión entre float y double.

---

### Recordatorio

- Forma básica: para código a nivel archivo o funciones `naked`.
- Forma extendida: `asm(template : outs : ins : clobbers)`.
- Usar `cc` y `memory` cuando corresponda.
- Diferencias de portabilidad: Windows/Linux y x86_64/ARM64 (calling conventions).