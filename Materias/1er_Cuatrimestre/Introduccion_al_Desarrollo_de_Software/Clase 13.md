---
base: "[[Introduccion al Desarrollo de Software.base]]"
Clase Grabada: https://youtu.be/ehsMD2kDcE4?si=xWuZ7iADmCc_q84H
Fecha: 2025-05-28T22:58:00
Descripción: Testing
Diapos:
  - 2243f454-0dd6-8014-8c80-f9e93c12b49e
---
# Que es el testing?

En el desarrollo de software, el testing (o pruebas de software) es el proceso de evaluar y verificar que un producto o aplicacion de software cumple con su funcion.

El testing sirve, entre otras cosas, para:

- Validar que la **funcionalidad** de un programa sea la esperada.
- Optimizar el **rendimiento** de la aplicacion.
- Encontrar y **corregir fallas** de seguridad (vulnerabilidades).

La idea de los tests es prevenir errores frente a cambios o funcionalidades que agreguemos.

## Tipos de testing

Existen distintos tipos de pruebas de software.

### Pruebas Unitarias

Se verifica que una sola funcionalidad (feature) de todas las que existen en nuestro programa funcione correctamente para todos los casos de uso posibles.

```javascript
function sumar(a, b) { return a + b }

const suma = sumar(num1, num2)

// Unit test 1: si num1 = -num2
// Unit test 2: si num1 =
```

### Pruebas de Integracion

Se prueban varias *features* juntas comunicandose entre si. Se verifica que el resultado final de todo ese proceso sea el esperado, idealmente para todos los casos de uso posible (spoiler: en la vida real es muy dificil testear todos los casos de uso posibles)

Son pruebas que verifican que varios componentes del sistema funcionen correctamente cuando se combinan.

Los tests de integracion se centran en como interactuan las distintas partes.

### Pruebas de estres

Se expone al programa a un conjunto de escenarios donde se ponen al limite las capacidades tecnicas del mismo (tiempo de respuestas, velocidad de transferencia de archivos, capacidad de procesamiento de peticiones HTTP, etc)

Cuantas personas se pueden conectar a un servidor hasta que se caiga, o cuantes request se pueden hacer en un minuto hasta quue laguee. 

# Request en Flask
