---

---
# Include

El método .Include(s => s.TipoSocio) le indica a Entity Framework Core que, al consultar la tabla Socios, también debe traer los datos relacionados de la tabla TipoSocio para cada socio.

Por defecto, Entity Framework solo carga la entidad principal (Socio) y no sus relaciones (TipoSocio) a menos que se lo pidas explícitamente con Include. Si no usas Include, la propiedad de navegación TipoSocio queda en null en los objetos Socio, aunque el ID exista en la base de datos.

Al usar Include, cada objeto Socio tendrá su propiedad TipoSocio cargada con los datos correspondientes, y así puedes acceder a s.TipoSocio.Nombre sin que lance una excepción.

## 1. Relaciones en Entity Framework Core

En una base de datos relacional, las tablas pueden estar relacionadas entre sí. Por ejemplo, un Socio puede tener un TipoSocio. En C# y Entity Framework Core, esto se representa con propiedades de navegación:

- En la clase `Socio` tienes una propiedad como `public TipoSocio TipoSocio { get; set; }` y una clave foránea como `public int TipoSocioId { get; set; }`.
- En la clase `TipoSocio` puedes tener una lista de socios: `public List<Socio> Socios { get; set; }`.

Esto permite que, al consultar un Socio, puedas acceder a su TipoSocio y viceversa.

## 2. El método Include

Por defecto, cuando haces una consulta como `_context.Socios.ToListAsync()`, solo se traen los datos de la tabla Socios. Las propiedades de navegación (como TipoSocio) quedan en null.

Para traer también los datos relacionados, usas `.Include`, así:

```c#
var socios = await _context.Socios
    .Include(s => s.TipoSocio)
    .ToListAsync();

```

Esto le dice a Entity Framework que haga un JOIN en la base de datos y traiga los datos de TipoSocio junto con cada Socio. Así, puedes acceder a `s.TipoSocio.Nombre` directamente en tu código.

# Resumen visual

Sin Include:

- Socio.TipoSocio → null

Con Include:

- Socio.TipoSocio → objeto completo con sus datos

¿Te gustaría ver un ejemplo de código más completo o saber cómo se configuran estas relaciones en las clases?