---

---
# Gestion de Clientes/Ventas

# Ideas

El proyecto tiene el objetivo de tener una plataforma de gestion de clientes, en donde podemos ver un detalle de toda la informacion del mismo (datos personales), ademas de un historial de las compras efectuadas del mismo.

Por lo que a partir de esta idea principal, surgen distintas funcionalidades que pueden sumarle utilidad a la pagina y hacerla mas completa

### Gestion de Stock

con la opcion de modificar, dar de alta y baja productos. (nombre, imagen, descripcion, color, talles, precio, cantidad por talle)

## Clientes: 

- se puede buscar clientes por nombre y visualizar todos los datos del mismo (nombre, apellido, cuit, dni, direccion, datos de contacto, telefono, mail)
- Historial de compras de clientes

## Ventas

cada vez que se produce una venta permite autoactualizar el stock.

# Tecnologias a Implementar

La idea es implementar un desarrollo haciendo empleo de metodologias de desarrollo agiles, trabajando con versionado de la aplicacion, a traves de Git y GitHub usando un manejo de branches al estilo GitHub Flow.

Tambien se plantea el desarrollo de la siguiente manera:

## Backend

Se utilizara una API Rest a desarrollar utilizando base de datos Postgre SQL levantandola con docker-compose, ademas de ***expressJS**** *con JavaScript  para la conexion y ejecutar las queries.

[[Base de Datos]]

[[Definiendo las RUTAS]]

## Frontend

Se busca utilizar HTML, CSS, y JavaScript, haciendo manejo de distintos templates, y haciendo routing para cada endpoint.

Para el diseño se utilizara Tailwind CSS, junto con REACT.

[[Diseñando el Frontend]]
