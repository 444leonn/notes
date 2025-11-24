---
cover: "[[Data Transfer Object (DTO).png]]"
---
[https://www.youtube.com/watch?v=4p6z6hL8BNg](https://www.youtube.com/watch?v=4p6z6hL8BNg)

# ¿Qué son los DTOs?

Un **DTO** (Data Transfer Object) es una clase simple que se utiliza para transportar datos entre procesos, capas o servicios. Los DTOs solo contienen propiedades para los datos que necesitas transferir, sin lógica de negocio ni relaciones complejas.

---

## ¿Por qué se usan?

- **Seguridad:** Evitan exponer información sensible o innecesaria de tus entidades.
- **Simplicidad:** Permiten enviar solo los datos relevantes, haciendo las respuestas más ligeras y fáciles de consumir.
- **Desacoplamiento:** Separan la estructura interna de la base de datos del formato de los datos que se exponen en la API.
- **Mantenimiento:** Facilitan cambios futuros en la base de datos sin afectar la API ni el frontend.

---

## ¿Cómo se implementa un DTO?

1. **Crea una clase DTO**
Define una clase con solo las propiedades que quieres exponer.

```c#
namespace api_prueba_challenge.Models
   {
       public class DeporteDto
       {
           public int Id { get; set; }
           public string Nombre { get; set; } = null!;
       }
   }

```

2. **Usa el DTO en el controlador**
Proyecta los datos de la entidad al DTO antes de devolverlos en la API.

```c#
[HttpGet]
   public async Task<ActionResult<IEnumerable<DeporteDto>>> GetDeportes()
   {
       var deportes = await _context.Deportes
           .Select(d => new DeporteDto
           {
               Id = d.Id,
               Nombre = d.Nombre
           })
           .ToListAsync();

       return deportes;
   }

```

---

# **En resumen:**

Los DTOs te ayudan a controlar y simplificar los datos que viajan por tu API, mejorando la seguridad y el mantenimiento del proyecto.

# Framework de AutoMapper (no usar)

[[AutoMapper]]

[https://www.youtube.com/watch?v=pr_pemcmVAs](https://www.youtube.com/watch?v=pr_pemcmVAs)
