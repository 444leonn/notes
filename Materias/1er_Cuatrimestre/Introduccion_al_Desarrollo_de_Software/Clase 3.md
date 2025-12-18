---
base: "[[Introduccion al Desarrollo de Software.base]]"
cover: "[[banner-bash.jpeg]]"
Clase Grabada: https://youtu.be/IdBYGcquT-E?si=yMt_LZmlsOF93fJv
Fecha: 2025-05-28T22:58:00
Descripción: Estructuras Condicionales e Iterativas, Ciclicas, Pipelines, Grep, Sed, REGEX.
Diapos:
  - 2243f454-0dd6-8013-b25e-dc9c6d5d550d
---
# Estructuras Condicionales e Iterativas

El Shell como intérprete puede resolver estructuras condicionales e iterativas, facilitando y ampliando la forma de interactuar con el usuario y permitiendo un gran abanico de posibilidad a la hora de crear Scripts.

## Condicionales

### If

La estrutura de un condicional es:

### Case

La estructura de un condicional tipo Case es:

```bash
case expression1 in
	pattern1)
		comandos ;;
	pattern2)
		comandos ;;
	...
esac
```

***Ejemplo:***

### Elementos de Comparacion

<u>**Números:**</u>

<u>**Cadenas:**</u>

# Estructuras Ciclicas

- Una estructura cíclica nos permitirá repetir instrucciones dentro de un script. En Bash existen 3 estructuras for, while y until.
- Cada una de ellas tiene un uso específico.

## For

El for nos permitirá iterar sobre una lista de valores.

En donde: i es la variable que tomará valor

[in LIST] es la lista de valores. Ejemplo:

```bash
in {1. .5}
(( c=1; c<=5; c++ ))
in file1 file2 file3
in $(Linux-Or-Unix-Command-Here
```

Su estructura es:

```bash
for i [in LIST ];
do 
	COMMANDS;
done 

```

***Ejemplo:***