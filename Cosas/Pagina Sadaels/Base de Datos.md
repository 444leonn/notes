---

---
Para la misma utilizaremos el motor PostgreSQL.

Y lo levantaremos con docker, se debe tener el motor de docker y docker-compose para ello.

# Definiendo las distintas tablas

Con el objetivo de poder tener un buen desarrollo se planificaran bien las distintas tablas y sus conexiones/vinculaciones para poder hacer un buen manejo de la informacion

## Prendas

Dado que la empresa se dedica a la produccion y comercializacion de distintas prendas de ropa, debemos crear tablas para las mismas.

### Tabla Principal

Esta tabla llevara el nombre de* “prendas” *y tendra las siguientes columnas:

### Tabla de Talles

Esta tiene el objetivo de permitir que una prenda pueda tener varios talles

### Tabla de Colores

Esta tiene el objetivo de permitir que una prenda pueda tener varios colores

### Tabla de Stock

Esta tiene el objetivo juntar las tres tablas anteriores

Por lo que vamos a estar realizando JOINS a las otras tablas para poder mostrar la informacion.

### Aproximacion de sentencia en SQL

```sql
CREATE TABLE prendas (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre_prenda VARCHAR(50) NOT NULL UNIQUE,
    descripcion VARCHAR(500) NOT NULL,
    imagen VARCHAR(500) NOT NULL,
    precio INT NOT NULL
);

CREATE TABLE colores (
    id_color INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre_color VARCHAR(50) NOT NULL
);

CREATE TABLE talles (
    id_talle INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre_talle VARCHAR(50) NOT NULL
);

CREATE TABLE prenda_stock (
    id_prenda INT,
    id_color INT,
    id_talle INT,
    stock INT DEFAULT 0,
    PRIMARY KEY (id_prenda, id_color, id_talle),
    FOREIGN KEY (id_prenda) REFERENCES prendas(id),
    FOREIGN KEY (id_color) REFERENCES colores(id_color),
    FOREIGN KEY (id_talle) REFERENCES talles(id_talle)
);
```

## Clientes

El objetivo es almacenar todos los datos de los clientes, para que en un futuro sea mas sencillo acceder a su informacion y poder facturar las distintas ventas

```sql
CREATE TABLE clientes (
    id_cliente INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50),
    dni INT NOT NULL UNIQUE,
    cuit INT UNIQUE,
    telefono INT,
    mail VARCHAR(50),
    direccion VARCHAR(50)
);
```

## Historial de Compras

(a lo mejor se puede utilizar para la funcionalidad de ventas)

```sql
CREATE TABLE historial_compras (
    id_compra INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_cliente INT,
    id_prenda INT,
	  id_color INT,
	  id_talle INT,
	  FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
	  FOREIGN KEY (id_prenda) REFERENCES prendas(id),
	  FOREIGN KEY (id_color) REFERENCES colores(id_color),
	  FOREIGN KEY (id_talle) REFERENCES talles(id_talle)
);
```

# Diagrama

![[base-de-datos-sadaels.svg]]

## Codigo en DBML

```sql
Table prendas {
  id INT [pk, increment]
  nombre_prenda VARCHAR(50) [not null, unique]
  descripcion VARCHAR(500) [not null]
  imagen VARCHAR(500) [not null]
  precio INT [not null]
}

Table colores {
  id_color INT [pk, increment]
  nombre_color VARCHAR(50) [not null]
}

Table talles {
  id_talle INT [pk, increment]
  nombre_talle VARCHAR(50) [not null]
}

Table prenda_stock {
  id_prenda INT [not null, pk]
  id_color INT [not null, pk]
  id_talle INT [not null, pk]
  stock INT [default: 0]
}

Table clientes {
  id_cliente INT [pk, increment]
  nombre VARCHAR(50) [not null]
  apellido VARCHAR(50)
  dni INT [not null, unique]
  cuit INT [unique]
  telefono INT
  mail VARCHAR(50)
  direccion VARCHAR(50)
}

Table historial_compras {
  id_compra INT [pk, increment]
  id_cliente INT
  id_prenda INT
  id_color INT
  id_talle INT
}

Ref: prenda_stock.id_prenda > prendas.id
Ref: prenda_stock.id_color > colores.id_color
Ref: prenda_stock.id_talle > talles.id_talle

Ref: historial_compras.id_cliente > clientes.id_cliente
Ref: historial_compras.id_prenda > prendas.id
Ref: historial_compras.id_color > colores.id_color
Ref: historial_compras.id_talle > talles.id_talle
```