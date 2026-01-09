---

---
# Migraciones en Entity Framework Core

Las migraciones en Entity Framework Core son una característica fundamental que permite actualizar incrementalmente el esquema de la base de datos para mantenerlo sincronizado con el modelo de datos de la aplicación, preservando los datos existentes.

## ¿Qué son las migraciones?

Las migraciones son archivos de código que describen los cambios necesarios para transformar el esquema de la base de datos de un estado a otro. En entornos de desarrollo reales, los modelos de datos evolucionan continuamente (se agregan entidades, se modifican propiedades, etc.), y las migraciones permiten aplicar estos cambios de manera controlada.

### ¿Cómo funcionan?

A nivel general, las migraciones funcionan de la siguiente manera:

- Cuando se introduce un cambio en el modelo de datos, EF Core compara el modelo actual con una instantánea del modelo anterior.
- A partir de esta comparación, genera archivos de código que describen las actualizaciones necesarias para mantener sincronizado el esquema.
- Estos archivos se pueden guardar en el control de versiones como cualquier otro código fuente.
- EF Core registra todas las migraciones aplicadas en una tabla especial de historial, lo que le permite saber cuáles se han aplicado y cuáles no.

## Objetos de colección de navegación

Antes de profundizar en las migraciones, es importante entender los objetos de colección de navegación en Entity Framework Core.

### ¿Qué son las propiedades de navegación?

Las propiedades de navegación son propiedades definidas en las entidades que permiten "navegar" de una entidad a otra relacionada. Estas propiedades no existen en la base de datos como columnas, sino que EF Core las utiliza para establecer y gestionar relaciones entre entidades.

### Tipos de propiedades de navegación:

- **Navegación de referencia**: Apunta a una sola entidad relacionada (relación uno a uno o muchos a uno).
- **Colección de navegación**: Contiene múltiples entidades relacionadas (relación uno a muchos o muchos a muchos).

### Ejemplo de colecciones de navegación

```c#
public class Blog
{
    public int Id { get; set; }
    public string Name { get; set; }
    
    // Colección de navegación - Representa una relación uno a muchos
    public List<Post> Posts { get; set; }
}

public class Post
{
    public int Id { get; set; }
    public string Title { get; set; }
    public string Content { get; set; }
    
    // Navegación de referencia - Representa una relación muchos a uno
    public int BlogId { get; set; }
    public Blog Blog { get; set; }
}
```

En este ejemplo:

- La propiedad `Posts` en la clase `Blog` es una colección de navegación.
- La propiedad `Blog` en la clase `Post` es una navegación de referencia.
- EF Core usará estas propiedades para establecer una relación uno a muchos entre blogs y posts.

## Configurando herramientas para migraciones

Para trabajar con migraciones, primero necesitas instalar las herramientas de línea de comandos de EF Core:

```bash
# Instalación de las herramientas de EF Core
dotnet tool install --global dotnet-ef

# Paquetes necesarios en tu proyecto
dotnet add package Microsoft.EntityFrameworkCore.SqlServer
dotnet add package Microsoft.EntityFrameworkCore.Tools
dotnet add package Microsoft.EntityFrameworkCore.Design

```

## Creando y aplicando migraciones

### 1. Crear un modelo de datos con colecciones de navegación

Vamos a crear un ejemplo más elaborado con diferentes tipos de relaciones:

```c#
// Modelo con relaciones uno a muchos y muchos a muchos
public class Autor
{
    public int Id { get; set; }
    public string Nombre { get; set; }
    
    // Colección de navegación (uno a muchos)
    public List<Libro> Libros { get; set; }
}

public class Libro
{
    public int Id { get; set; }
    public string Titulo { get; set; }
    
    // Navegación de referencia (muchos a uno)
    public int AutorId { get; set; }
    public Autor Autor { get; set; }
    
    // Colección de navegación (muchos a muchos)
    public List<Categoria> Categorias { get; set; }
}

public class Categoria
{
    public int Id { get; set; }
    public string Nombre { get; set; }
    
    // Colección de navegación (muchos a muchos)
    public List<Libro> Libros { get; set; }
}

```

### 2. Configurar el DbContext

```c#
public class BibliotecaContext : DbContext
{
    public BibliotecaContext(DbContextOptions<BibliotecaContext> options)
        : base(options)
    {
    }
    
    public DbSet<Autor> Autores { get; set; }
    public DbSet<Libro> Libros { get; set; }
    public DbSet<Categoria> Categorias { get; set; }
    
    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        // Configurar la relación uno a muchos entre Autor y Libro
        modelBuilder.Entity<Libro>()
            .HasOne(l => l.Autor)
            .WithMany(a => a.Libros)
            .HasForeignKey(l => l.AutorId);
            
        // Configurar la relación muchos a muchos entre Libro y Categoría
        modelBuilder.Entity<Libro>()
            .HasMany(l => l.Categorias)
            .WithMany(c => c.Libros)
            .UsingEntity(j => j.ToTable("LibroCategorias"));
    }
}

```

### 3. Registrar el DbContext en Program.cs

```c#
// En Program.cs
builder.Services.AddDbContext<BibliotecaContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection")));

```

### 4. Crear la primera migración

Desde la terminal, ejecuta:

```bash
dotnet ef migrations add MigracionInicial
```

Esto generará varios archivos en la carpeta Migrations:

- Un archivo con el nombre de la migración (ej: 20250808123456_MigracionInicial.cs)
- Un archivo de contexto del diseñador
- Un archivo de instantánea del modelo

### 5. Aplicar la migración a la base de datos

```bash
dotnet ef database update
```

## Evolución del modelo con colecciones de navegación

Ahora, supongamos que necesitamos agregar una nueva entidad `Editorial` relacionada con `Libro`:

```c#
public class Editorial
{
    public int Id { get; set; }
    public string Nombre { get; set; }
    public string Direccion { get; set; }
    
    // Colección de navegación (uno a muchos)
    public List<Libro> Libros { get; set; }
}

// Actualización de la clase Libro
public class Libro
{
    public int Id { get; set; }
    public string Titulo { get; set; }
    
    // Relación con Autor (sin cambios)
    public int AutorId { get; set; }
    public Autor Autor { get; set; }
    
    // Nueva relación con Editorial
    public int? EditorialId { get; set; }
    public Editorial Editorial { get; set; }
    
    // Relación con Categorías (sin cambios)
    public List<Categoria> Categorias { get; set; }
}
```

Actualiza la configuración en el DbContext:

```c#
protected override void OnModelCreating(ModelBuilder modelBuilder)
{
    // Configuraciones existentes...
    
    // Configurar la relación uno a muchos entre Editorial y Libro
    modelBuilder.Entity<Libro>()
        .HasOne(l => l.Editorial)
        .WithMany(e => e.Libros)
        .HasForeignKey(l => l.EditorialId);
}
```

### Generar una nueva migración para estos cambios

```bash
dotnet ef migrations add AgregarEntidadEditorial
```

Esta migración creará:

- Una nueva tabla para la entidad Editorial
- Una columna de clave foránea (EditorialId) en la tabla Libros
- Un índice en la clave foránea
- Una restricción de clave foránea entre las tablas

### Aplicar la nueva migración

```bash
dotnet ef database update
```

## Comandos útiles para migraciones

| **Comando** | **Descripción** |
| --- | --- |
| `dotnet ef migrations add NombreMigracion` | Crea una nueva migración |
| `dotnet ef database update` | Aplica todas las migraciones pendientes |
| `dotnet ef database update MigracionX` | Actualiza la base de datos a una migración específica |
| `dotnet ef migrations remove` | Elimina la última migración |
| `dotnet ef migrations script` | Genera un script SQL para todas las migraciones |
| `dotnet ef migrations list` | Lista todas las migraciones |

## Buenas prácticas

- **Migraciones pequeñas y frecuentes**: Es mejor hacer pequeños cambios y crear migraciones para cada uno, en lugar de acumular muchos cambios en una sola migración.
- **Nombres descriptivos**: Usa nombres claros que indiquen qué hace cada migración.
- **Revisa el código generado**: Es buena práctica revisar el código de migración generado antes de aplicarlo.
- **Control de versiones**: Incluye las migraciones en el control de versiones de tu proyecto.
- **Scripts para producción**: En entornos de producción, considera generar scripts SQL con `dotnet ef migrations script` en lugar de aplicar migraciones directamente.

## Conclusión

Las migraciones en Entity Framework Core son una poderosa herramienta para mantener sincronizados tus modelos de datos con el esquema de la base de datos. Cuando trabajas con relaciones complejas y objetos de colección de navegación, las migraciones se encargan de crear todas las tablas, columnas y restricciones necesarias para representar correctamente estas relaciones en la base de datos.

Al entender cómo funcionan las migraciones y cómo configurar correctamente las relaciones entre entidades, puedes construir aplicaciones .NET robustas con modelos de datos complejos que evolucionan con el tiempo sin perder datos existentes.