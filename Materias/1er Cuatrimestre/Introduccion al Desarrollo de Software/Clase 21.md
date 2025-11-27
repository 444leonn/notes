---
base: "[[Introduccion al Desarrollo de Software.base]]"
Clase Grabada: https://youtu.be/BxXjVDv6XmY?si=LlSxVkdajl74Mhw_
Fecha: 2025-05-28T22:58:00
Descripción: Ejercitacion Integral FRONT  + BACK
Diapos:
  - 2243f454-0dd6-80d1-965c-f0edac4ff9fd
---
# Frontend

## **Requerimientos de nuestra app simple**

- Debe haber una vista que contenga un formulario y permita ingresar el número de padrón de un alumno. Debe contener un botón que diga “Buscar datos alumno”
- Si existe, debe ir a otra vista llamada detalle.html que muestre los datos personales del alumno y todas las materias que cursó.
- Las materias aprobadas deberán aparecer en verde y las que no en rojo.
- Al hacer click en una materia, deberá mostrar un pop-up con la fecha y la nota numérica obtenida.
- Al hacer click sobre el código de materia, se debe poder visualizar todos los alumnos que la cursaron
- Se debe poder agregar una nota desde la vista de detalles para ese alumno.

## **¿Qué endpoints vamos a necesitar?**

- /alumnos
    - /alumnos/<padron>
    - /alumnos/<padron>/notas
- /materias
    - /materias/<codigo>/alumnos

# Backend

## Modelo de Datos

### Creamos la Base de Datos

- Crear una base de datos llamada Facultad que contenga 3 tablas (alumnos, materias, notas)
- Definir Pk, Fk necesarias para la estructura de tablas.

Campos de cada tabla:

- alumno debe tener los campos padrón, nombre, apellido
- materias debe tener los campos, código_materia, nombre, carrera
- notas debe tener los campos, código_materia, nota, fecha, padrón

## Joins

### Distintos tipos de SQL Joins

![[join-types.png]]

### Inner Join

<!-- Column 1 -->
```sql
SELECT column_name(s)
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;
```

<!-- Column 2 -->
![[inner-join.png]]

# Integrar FRONT con BACK

# **Controller Service Repository**

![[image 51.png]]