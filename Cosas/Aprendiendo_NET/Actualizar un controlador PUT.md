---

---
### `[HttpPut]` usando **DbContext** en **ASP.NET Core** con **Entity Framework Core**

Los pasos generales son los siguientes:

---

### 1. Definir el método de acción `HttpPut`.

El método del controlador debe estar decorado con el atributo `[HttpPut]` e incluir normalmente un parámetro de ruta para el **ID** de la entidad que se quiere actualizar.

Además, debe aceptar el objeto actualizado de la entidad desde el cuerpo de la petición.

```c#
[HttpPut("{id}")]
public async Task<IActionResult> UpdateMyEntity(int id, [FromBody] MyEntity updatedEntity)
{
    // ...
}

```

---

### 2. Validar la petición.

Dentro del método, asegurarse de que el `id` proporcionado coincida con la propiedad `Id` de `updatedEntity` para mantener la consistencia de los datos.

También comprobar que `ModelState.IsValid` sea verdadero para garantizar que el objeto recibido cumple con las anotaciones de datos definidas en el modelo.

```c#
if (id != updatedEntity.Id)
{
    return BadRequest(); // O un error más específico
}

if (!ModelState.IsValid)
{
    return BadRequest(ModelState);
}

```

---

### 3. Recuperar y actualizar la entidad existente.

Buscar la entidad actual en la base de datos usando el **DbContext**.

Si la entidad existe, actualizar sus propiedades con los valores de `updatedEntity`.

```c#
var existingEntity = await _context.MyEntities.FindAsync(id);

if (existingEntity == null)
{
    return NotFound();
}

// Actualizar propiedades con los valores de updatedEntity
_context.Entry(existingEntity).CurrentValues.SetValues(updatedEntity);

```

👉 Alternativamente, si usás un DTO o querés mapear manualmente las propiedades:

```c#
existingEntity.PropertyName1 = updatedEntity.PropertyName1;
existingEntity.PropertyName2 = updatedEntity.PropertyName2;
// ... y así para todas las propiedades que quieras actualizar

```

---

### 4. Guardar cambios en la base de datos.

Después de modificar las propiedades de la entidad, llamar a `_context.SaveChangesAsync()` para persistir los cambios.

```c#
try
{
    await _context.SaveChangesAsync();
}
catch (DbUpdateConcurrencyException)
{
    // Manejar conflictos de concurrencia si corresponde
    if (!_context.MyEntities.Any(e => e.Id == id))
    {
        return NotFound();
    }
    else
    {
        throw;
    }
}

```

---

### 5. Devolver la respuesta apropiada.

Retornar un **NoContent()** (HTTP 204) si la actualización fue exitosa, o bien otros códigos adecuados como **NotFound()** (HTTP 404) o **BadRequest()** (HTTP 400) en caso de errores.

```c#
return NoContent();

```