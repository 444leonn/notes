---
base: "[[Introduccion al Desarrollo de Software.base]]"
Clase Grabada: https://youtu.be/JB8vDm734tk?si=KhyHtX8jSdsgerZg
Fecha: 2025-05-28T22:58:00
Descripción: Continuacion GIT
Diapos:
  - 2243f454-0dd6-80b3-8307-c5efd315e3d6
---
# BRANCHES

## Que es una branch?

- Una branch (rama) es una línea de desarrollo independiente.
- Permite trabajar en diferentes características o correcciones de bugs de manera aislada.
- git checkout <nombre_de_la_rama>: Cambia a la rama especificada.
- git switch <nombre_de_la_rama>: Cambia a la rama especificada (más moderno y seguro).

### .checkout

- Un comando versátil utilizado para cambiar de rama o restaurar archivos en tu directorio de trabajo.
- Permite navegar entre ramas, crear nuevas ramas, y revertir archivos o commits específicos.

### **Blame y Cherry-Pick**

- **git blame**: Muestra la última modificación de cada línea en un archivo.
- Uso Común: Identificar quién hizo un cambio específico y cuándo.
- **git cherry-pick **: Aplica los cambios de un commit específico a la rama actual.

# **¿Qué es **`**git stash**`**?**