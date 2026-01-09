# Guía Completa de Entity Framework Core - Métodos Detallados

## 1. CONSULTAS BÁSICAS (Lectura)

### `ToList()` / `ToListAsync()`

**Qué hace:** Ejecuta la consulta y devuelve **todos** los resultados en una lista en memoria.

**Cuándo usar:** Cuando necesitas trabajar con todos los registros en memoria.

**Cuándo NO usar:** Con tablas grandes (miles de registros) - consume mucha memoria.

```csharp
// Trae TODOS los usuarios a memoria
var usuarios = await _context.Usuarios.ToListAsync();

// Después puedes filtrar en memoria (pero es ineficiente)
var activos = usuarios.Where(u => u.Activo).ToList();
```

**vs `AsEnumerable()`:** ToList ejecuta la consulta inmediatamente. AsEnumerable difiere la ejecución pero igual trae todo a memoria eventualmente.

---

### `FirstOrDefault()` / `FirstOrDefaultAsync()`

**Qué hace:** Devuelve el **primer elemento** que cumple la condición, o `null` si no encuentra nada.

**Cuándo usar:** Cuando esperas uno o más resultados pero solo necesitas el primero.

**Cuándo NO usar:** Si necesitas asegurarte que hay exactamente un resultado (usa `SingleOrDefault`).

```csharp
// Busca el primer usuario con ese email (o null)
var usuario = await _context.Usuarios
    .FirstOrDefaultAsync(u => u.Email == "juan@email.com");

if (usuario == null)
{
    return NotFound();
}

// CUIDADO: Si hay múltiples con ese email, toma el primero
// No genera error aunque haya duplicados
```

**vs `First()`:** `First()` lanza excepción si no encuentra nada. `FirstOrDefault()` devuelve null (más seguro).

---

### `SingleOrDefault()` / `SingleOrDefaultAsync()`

**Qué hace:** Devuelve el **único elemento** que cumple la condición, o `null` si no hay ninguno. **Lanza excepción** si hay más de uno.

**Cuándo usar:** Cuando esperas exactamente 0 o 1 resultado (campos únicos como email, DNI).

**Cuándo NO usar:** Si puede haber múltiples resultados (usa `FirstOrDefault`).

```csharp
// Busca UN usuario con ese DNI
var usuario = await _context.Usuarios
    .SingleOrDefaultAsync(u => u.DNI == "12345678");

// Si hay 2+ usuarios con ese DNI, lanza InvalidOperationException
// Útil para detectar datos duplicados que no deberían existir
```

**vs `FirstOrDefault()`:**

- `SingleOrDefault()` valida que solo haya 1 resultado (más estricto)
- `FirstOrDefault()` toma el primero sin validar (más permisivo)

---

### `Find()` / `FindAsync()`

**Qué hace:** Busca una entidad por su **clave primaria** (Primary Key).

**Cuándo usar:** Cuando tienes el ID y quieres buscar por él. Es más eficiente porque revisa primero la memoria antes de consultar la BD.

**Cuándo NO usar:** Si necesitas buscar por otro campo (usa `FirstOrDefault` o `SingleOrDefault`).

```csharp
// Busca usuario por ID (clave primaria)
var usuario = await _context.Usuarios.FindAsync(5);

// Si el usuario ya está en memoria (change tracker), lo devuelve
// sin hacer consulta a la BD (más rápido)

// NO PUEDES hacer esto con Find:
// var usuario = await _context.Usuarios.FindAsync(u => u.Email == "...");
// ❌ Error: Find solo acepta la clave primaria
```

**vs `FirstOrDefault(u => u.Id == id)`:** Find es más rápido porque chequea la memoria primero.

---

### `Where()`

**Qué hace:** Filtra resultados según una condición. **NO ejecuta la consulta**, solo la construye.

**Cuándo usar:** Para filtrar datos. Puedes encadenar múltiples `Where`.

```csharp
// Filtra usuarios activos
var activos = await _context.Usuarios
    .Where(u => u.Activo == true)
    .ToListAsync();

// Puedes encadenar múltiples Where
var resultado = await _context.Usuarios
    .Where(u => u.Activo == true)
    .Where(u => u.Edad >= 18)
    .Where(u => u.Ciudad == "Buenos Aires")
    .ToListAsync();

// Es equivalente a:
var resultado = await _context.Usuarios
    .Where(u => u.Activo == true && u.Edad >= 18 && u.Ciudad == "Buenos Aires")
    .ToListAsync();
```

**IMPORTANTE:** `Where()` no ejecuta la consulta hasta que uses `ToList()`, `FirstOrDefault()`, etc.

---

### `Select()`

**Qué hace:** **Proyecta** datos, es decir, selecciona solo ciertos campos o transforma el resultado.

**Cuándo usar:** Para traer solo los campos necesarios (más eficiente). Útil para crear DTOs.

```csharp
// ❌ MAL: Trae TODOS los campos del usuario
var usuarios = await _context.Usuarios.ToListAsync();
var nombres = usuarios.Select(u => u.Nombre).ToList();

// ✅ BIEN: Trae SOLO el campo Nombre desde la BD
var nombres = await _context.Usuarios
    .Select(u => u.Nombre)
    .ToListAsync();

// Crear un DTO directamente
var usuariosDTO = await _context.Usuarios
    .Select(u => new UsuarioDTO
    {
        Id = u.Id,
        NombreCompleto = u.Nombre + " " + u.Apellido,
        Email = u.Email
    })
    .ToListAsync();

// SQL generado: SELECT Id, Nombre, Apellido, Email FROM Usuarios
// No trae Password, FechaNacimiento, etc.
```

**Beneficio:** Reduce el tráfico de red y es más rápido.

---

## 2. ORDENAMIENTO

### `OrderBy()` / `OrderByDescending()`

**Qué hace:** Ordena los resultados de forma ascendente o descendente.

```csharp
// Ordenar por nombre (A-Z)
var usuarios = await _context.Usuarios
    .OrderBy(u => u.Nombre)
    .ToListAsync();

// Ordenar por edad (mayor a menor)
var usuarios = await _context.Usuarios
    .OrderByDescending(u => u.Edad)
    .ToListAsync();
```

---

### `ThenBy()` / `ThenByDescending()`

**Qué hace:** Agrega un criterio de ordenamiento **secundario**.

**Cuándo usar:** Cuando quieres ordenar por múltiples campos.

```csharp
// Ordena por Ciudad, y dentro de cada ciudad por Nombre
var usuarios = await _context.Usuarios
    .OrderBy(u => u.Ciudad)
    .ThenBy(u => u.Nombre)
    .ToListAsync();

// Primero por Edad (descendente), luego por Nombre (ascendente)
var usuarios = await _context.Usuarios
    .OrderByDescending(u => u.Edad)
    .ThenBy(u => u.Nombre)
    .ToListAsync();
```

---

## 3. PAGINACIÓN

### `Skip()` / `Take()`

**Qué hace:** Salta N registros y toma M registros. Esencial para paginación.

**Cuándo usar:** APIs con paginación, listados grandes.

```csharp
// Página 1: registros 0-9
var pagina1 = await _context.Usuarios
    .OrderBy(u => u.Id)
    .Skip(0)
    .Take(10)
    .ToListAsync();

// Página 2: registros 10-19
var pagina2 = await _context.Usuarios
    .OrderBy(u => u.Id)
    .Skip(10)
    .Take(10)
    .ToListAsync();

// Paginación genérica
int pageNumber = 3;
int pageSize = 20;
var resultados = await _context.Usuarios
    .OrderBy(u => u.Id)
    .Skip((pageNumber - 1) * pageSize)
    .Take(pageSize)
    .ToListAsync();
```

**IMPORTANTE:** Siempre usa `OrderBy()` antes de `Skip/Take`, sino el orden puede ser aleatorio.

---

## 4. AGREGACIÓN Y CONTEO

### `Count()` / `CountAsync()`

**Qué hace:** Cuenta cuántos registros cumplen la condición.

```csharp
// Contar todos los usuarios
var total = await _context.Usuarios.CountAsync();

// Contar usuarios activos
var activos = await _context.Usuarios
    .CountAsync(u => u.Activo == true);

// ❌ INEFICIENTE:
var lista = await _context.Usuarios.ToListAsync();
var count = lista.Count(); // Trae todo a memoria solo para contar

// ✅ EFICIENTE:
var count = await _context.Usuarios.CountAsync(); // Hace COUNT(*) en SQL
```

---

### `Any()` / `AnyAsync()`

**Qué hace:** Verifica si **existe al menos un** registro que cumple la condición.

**Cuándo usar:** Para verificar existencia. Más eficiente que `Count() > 0`.

```csharp
// ¿Existe algún usuario con ese email?
var existe = await _context.Usuarios
    .AnyAsync(u => u.Email == "juan@email.com");

if (existe)
{
    return BadRequest("El email ya está registrado");
}

// ❌ INEFICIENTE:
var count = await _context.Usuarios
    .CountAsync(u => u.Email == "juan@email.com");
if (count > 0) { ... }

// ✅ EFICIENTE:
var existe = await _context.Usuarios
    .AnyAsync(u => u.Email == "juan@email.com");
```

**vs `Count() > 0`:** `Any()` se detiene en el primer resultado. `Count()` cuenta todos.

---

### `Sum()` / `Average()` / `Min()` / `Max()`

**Qué hace:** Operaciones matemáticas sobre una colección.

```csharp
// Suma total de ventas
var totalVentas = await _context.Pedidos
    .SumAsync(p => p.Total);

// Promedio de edades
var edadPromedio = await _context.Usuarios
    .AverageAsync(u => u.Edad);

// Producto más caro
var precioMaximo = await _context.Productos
    .MaxAsync(p => p.Precio);

// Producto más barato
var precioMinimo = await _context.Productos
    .MinAsync(p => p.Precio);
```

---

## 5. OPERACIONES DE ESCRITURA

### `Add()` / `AddAsync()`

**Qué hace:** Marca una entidad para ser **insertada** en la BD.

**IMPORTANTE:** No se guarda hasta llamar `SaveChanges()`.

```csharp
var nuevoUsuario = new Usuario
{
    Nombre = "Juan",
    Email = "juan@email.com",
    Activo = true
};

// Marca para insertar (aún NO está en la BD)
_context.Usuarios.Add(nuevoUsuario);

// AHORA se inserta en la BD
await _context.SaveChangesAsync();

// nuevoUsuario.Id ahora tiene el valor generado por la BD
```

---

### `AddRange()` / `AddRangeAsync()`

**Qué hace:** Agrega **múltiples entidades** a la vez.

**Cuándo usar:** Insertar varios registros. Más eficiente que múltiples `Add()`.

```csharp
var usuarios = new List<Usuario>
{
    new Usuario { Nombre = "Juan", Email = "juan@email.com" },
    new Usuario { Nombre = "María", Email = "maria@email.com" },
    new Usuario { Nombre = "Pedro", Email = "pedro@email.com" }
};

// Marca todos para insertar
_context.Usuarios.AddRange(usuarios);

// Inserta todos en una sola operación
await _context.SaveChangesAsync();
```

---

### `Update()`

**Qué hace:** Marca una entidad para ser **actualizada**.

**Cuándo usar:** Cuando tienes una entidad desconectada del contexto.

```csharp
// Escenario común en APIs:
// 1. Recibes datos del frontend
var usuarioActualizado = new Usuario
{
    Id = 5,
    Nombre = "Juan Actualizado",
    Email = "nuevo@email.com"
};

// 2. Marcas como modificado
_context.Usuarios.Update(usuarioActualizado);

// 3. Guardas
await _context.SaveChangesAsync();

// CUIDADO: Esto actualiza TODOS los campos
```

**MEJOR PRÁCTICA (actualización parcial):**

```csharp
// 1. Buscar la entidad existente
var usuario = await _context.Usuarios.FindAsync(5);

if (usuario == null)
{
    return NotFound();
}

// 2. Modificar solo los campos necesarios
usuario.Nombre = "Juan Actualizado";
usuario.Email = "nuevo@email.com";

// 3. EF detecta automáticamente los cambios
await _context.SaveChangesAsync();

// SQL generado: UPDATE Usuarios SET Nombre = ..., Email = ... WHERE Id = 5
// Solo actualiza los campos modificados
```

---

### `Remove()` / `RemoveRange()`

**Qué hace:** Marca entidades para ser **eliminadas**.

```csharp
// Eliminar un usuario
var usuario = await _context.Usuarios.FindAsync(5);

if (usuario != null)
{
    _context.Usuarios.Remove(usuario);
    await _context.SaveChangesAsync();
}

// Eliminar múltiples
var usuariosInactivos = await _context.Usuarios
    .Where(u => u.Activo == false)
    .ToListAsync();

_context.Usuarios.RemoveRange(usuariosInactivos);
await _context.SaveChangesAsync();
```

---

### `SaveChanges()` / `SaveChangesAsync()`

**Qué hace:** **Persiste todos los cambios** en la base de datos.

**MUY IMPORTANTE:** Sin esto, nada se guarda en la BD.

```csharp
// Ejemplo completo
var usuario = new Usuario { Nombre = "Juan" };
_context.Usuarios.Add(usuario); // Marca para insertar

var otro = await _context.Usuarios.FindAsync(2);
otro.Nombre = "Actualizado"; // Marca para actualizar

var eliminar = await _context.Usuarios.FindAsync(3);
_context.Usuarios.Remove(eliminar); // Marca para eliminar

// HASTA AQUÍ nada se guardó en la BD

await _context.SaveChangesAsync(); // AHORA se ejecutan todos los cambios

// SQL generado:
// BEGIN TRANSACTION
// INSERT INTO Usuarios ...
// UPDATE Usuarios SET Nombre = ... WHERE Id = 2
// DELETE FROM Usuarios WHERE Id = 3
// COMMIT TRANSACTION
```

**Retorna:** El número de filas afectadas.

```csharp
int cambios = await _context.SaveChangesAsync();
// cambios = 3 (1 insert + 1 update + 1 delete)
```

---

## 6. RELACIONES (JOINS)

### `Include()`

**Qué hace:** Carga datos de entidades relacionadas (Eager Loading).

**Cuándo usar:** Cuando necesitas datos de tablas relacionadas.

```csharp
// Modelo:
public class Pedido
{
    public int Id { get; set; }
    public int UsuarioId { get; set; }
    public Usuario Usuario { get; set; } // Navegación
}

public class Usuario
{
    public int Id { get; set; }
    public string Nombre { get; set; }
    public List<Pedido> Pedidos { get; set; }
}

// Sin Include (Usuario es null)
var pedido = await _context.Pedidos.FirstOrDefaultAsync();
// pedido.Usuario es null ❌

// Con Include (Usuario se carga)
var pedido = await _context.Pedidos
    .Include(p => p.Usuario)
    .FirstOrDefaultAsync();
// pedido.Usuario contiene los datos ✅

// SQL generado:
// SELECT * FROM Pedidos p
// INNER JOIN Usuarios u ON p.UsuarioId = u.Id
```

---

### `ThenInclude()`

**Qué hace:** Carga relaciones **anidadas** (relaciones de relaciones).

```csharp
public class Pedido
{
    public int Id { get; set; }
    public Usuario Usuario { get; set; }
    public List<DetallePedido> Detalles { get; set; }
}

public class DetallePedido
{
    public int Id { get; set; }
    public Producto Producto { get; set; }
}

// Cargar Pedido -> Detalles -> Productos
var pedido = await _context.Pedidos
    .Include(p => p.Usuario)
    .Include(p => p.Detalles)
        .ThenInclude(d => d.Producto)
    .FirstOrDefaultAsync();

// Ahora tienes acceso a:
// pedido.Usuario
// pedido.Detalles[0].Producto
```

---

### `AsNoTracking()`

**Qué hace:** Desactiva el **change tracking** (seguimiento de cambios).

**Cuándo usar:** Consultas de solo lectura. Más rápido y consume menos memoria.

**Cuándo NO usar:** Si vas a modificar los datos.

```csharp
// Sin AsNoTracking (tracking activado)
var usuarios = await _context.Usuarios.ToListAsync();
// EF guarda una copia en memoria para detectar cambios

// Con AsNoTracking (solo lectura)
var usuarios = await _context.Usuarios
    .AsNoTracking()
    .ToListAsync();
// Más rápido, menos memoria

// ❌ NO puedes hacer esto:
var usuario = await _context.Usuarios
    .AsNoTracking()
    .FirstOrDefaultAsync();
usuario.Nombre = "Cambio"; // Se modifica
await _context.SaveChangesAsync(); // ❌ No se guarda porque no está tracked
```

**Usa en:** Consultas para APIs de lectura, reportes, listados.

---

## 7. OPERACIONES AVANZADAS

### `ExecuteUpdate()` / `ExecuteUpdateAsync()` (.NET 7+)

**Qué hace:** Actualiza registros **directamente en la BD** sin cargarlos en memoria.

**Cuándo usar:** Actualizaciones masivas. Mucho más eficiente.

```csharp
// ❌ INEFICIENTE (carga 1000 usuarios en memoria):
var usuarios = await _context.Usuarios
    .Where(u => u.Ciudad == "Buenos Aires")
    .ToListAsync();

foreach (var u in usuarios)
{
    u.Activo = false;
}
await _context.SaveChangesAsync();

// ✅ EFICIENTE (actualización directa):
await _context.Usuarios
    .Where(u => u.Ciudad == "Buenos Aires")
    .ExecuteUpdateAsync(setter => setter
        .SetProperty(u => u.Activo, false)
    );

// SQL generado:
// UPDATE Usuarios SET Activo = 0 WHERE Ciudad = 'Buenos Aires'
```

---

### `ExecuteDelete()` / `ExecuteDeleteAsync()` (.NET 7+)

**Qué hace:** Elimina registros **directamente** sin cargarlos.

```csharp
// ❌ INEFICIENTE:
var inactivos = await _context.Usuarios
    .Where(u => u.Activo == false)
    .ToListAsync();
_context.RemoveRange(inactivos);
await _context.SaveChangesAsync();

// ✅ EFICIENTE:
await _context.Usuarios
    .Where(u => u.Activo == false)
    .ExecuteDeleteAsync();

// SQL generado:
// DELETE FROM Usuarios WHERE Activo = 0
```

---

### `FromSqlRaw()` / `FromSqlInterpolated()`

**Qué hace:** Ejecuta **SQL directo** cuando LINQ no es suficiente.

**Cuándo usar:** Consultas complejas, procedimientos almacenados.

**PELIGRO:** `FromSqlRaw` es vulnerable a SQL Injection. Usa `FromSqlInterpolated`.

```csharp
// ❌ PELIGROSO (SQL Injection):
string ciudad = "Buenos Aires"; // Podría ser "'; DROP TABLE Usuarios--"
var usuarios = await _context.Usuarios
    .FromSqlRaw($"SELECT * FROM Usuarios WHERE Ciudad = '{ciudad}'")
    .ToListAsync();

// ✅ SEGURO (usa parámetros):
var usuarios = await _context.Usuarios
    .FromSqlInterpolated($"SELECT * FROM Usuarios WHERE Ciudad = {ciudad}")
    .ToListAsync();

// Procedimiento almacenado
var resultado = await _context.Usuarios
    .FromSqlRaw("EXEC ObtenerUsuariosActivos")
    .ToListAsync();
```

---

## RESUMEN DE CUÁNDO USAR CADA MÉTODO

|              Necesitas               |                   Usa                    |
|:------------------------------------:|:----------------------------------------:|
|         Todos los registros          |             `ToListAsync()`              |
|          Un registro por ID          |             `FindAsync(id)`              |
| Primer registro que cumple condición |         `FirstOrDefaultAsync()`          |
|       Exactamente un registro        |         `SingleOrDefaultAsync()`         |
|          Filtrar registros           |                `Where()`                 |
|         Solo ciertos campos          |                `Select()`                |
|         Verificar si existe          |               `AnyAsync()`               |
|           Contar registros           |              `CountAsync()`              |
|              Paginación              |             `Skip().Take()`              |
|       Traer datos relacionados       |      `Include()` / `ThenInclude()`       |
|      Solo lectura (más rápido)       |             `AsNoTracking()`             |
|               Insertar               |      `Add()` + `SaveChangesAsync()`      |
|              Actualizar              | Modificar entidad + `SaveChangesAsync()` |
|               Eliminar               |    `Remove()` + `SaveChangesAsync()`     |
|         Actualización masiva         |          `ExecuteUpdateAsync()`          |
|          Eliminación masiva          |          `ExecuteDeleteAsync()`          |
