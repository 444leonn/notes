---
cover: "[[Aprendiendo .NET]]"
---
Cuando creamos una nueva solucion para un proyecto de .NET, se nos crea una serie de carpetas que conforman la estructura de nuestro proyecto.

# Inicios de un Proyecto

Para todo proyecto de una ***Web API con ASP*** el “*entrypoint” *o punto de entrada de nuestra aplicacion es el archivo nombre `Program.cs` 

## Tipos de Proyecto para APIs

En .NET tenemos dos tipos de manera de desarrollar una API, puede ser la llamada ***minimal *** o la manejada por controladores

## Builder

Dentro de `Program.cs` se almacena el `builder` de la aplicacion que se declara como `var builder = WebApplication.CreateBuilder(args);` .

El mismo representa un *constructor *al que yo le puedo agregar diferentes cosas y servicios.

Como por ejemplo: `builder.Services.AddSwaggerGen();` 

### Servicios

Podemos decir que cada servicio representa un componente que vamos a estar utilizando en la aplicacion, ya sea externo o interno (hecho por nosotros mismos)

- Existen servicios generales de ASP.NET
- Existen servicios creados por nosotros

Luego de agregar los servicios, se buildea o construye la aplicacion con
`var app = builder.Build();`

Y una vez que ya construimos la app, le podemos agregar *middleware*

==Para utilizar ====*controllers *====utilizamos el servicio para agregarlos y luego los mapeamos==

==`builder.Services.AddControllers();`==

### Middlewares

Son componentes que **manipulan los metodos **HTTP

- Se lo llama “***application request pipeline” ***o*** “pipeline” ***
- El orden importa, se debe respetar un orden para llamarlos
- ==Ademas del servicio de agregar los controller debemos agregar el middleware con==
==`app.MapControllers();`==

## MVC

Es un patron arquitectural de software, se puede interpretar como la manera o metodologia en la que definimos los distintos componentes que va a tener nuestro software.

Posee tres partes:

## Models

Pensemos a los models como clases que poseen la estructura de los datos, los cuales muy probablemente guardemos posteriormente en la base de datos.

Por lo general, al solo ser utilizados para almacenar la informacion, los models no requieren metodos.

## Controllers

Los controllers son similares a lo que vi de las routes, en donde en estos archivos almacenamos todo nuestro endpoint.

```c#
using Microsoft.EntityFrameworkCore.Mvc;

namespace MandrilAPI.Controller;

// Data Annotations
[ApiController]
[Route("api/[controller]")]
 
public class MandrilController : ControllerBase // Hereda  la clase
{
	[HttpGet] // Action
	public ActionResult<IEnumerable<Mandril>> Get()
	{
		var data = // toda la informacion (ver de conectar con db)
		return Ok(data)
	}
}
```

- Los valores encerrados entre [] son los llamados *data annotations*
- Luego el `: ControllerBase` significa que la clase de MandrilController, es heredada de la de ControllerBase la cual forma para de la biblioteca de EntityFramework.Mvc que incluimos al principio del controller con el using.
El `ControllerBase` nos proporciona una serie de funciones para poder utilizar en el controlador. (continuar anotando mas adelante)
- *ActionResult *nos permite retornar todos las cosas necesarias para nuestra peticion.
- *IEnumerable *nos permite devolver mas de un valor, por ejemplo mas clase de las de Mandril

La misma idea es la seguida para realizar la peticion de un POST, PUT o DELETE, o incluso de mas GET. Lo importante es seguir la convencion de utilizar Controller’s asociados con modelos especificos.

# Frameworks a Utilizar 

# Conexion con la Base de Datos

Para conectar nuestra base de datos a nuestra API con .NET debemos crear una clase que se llame `AppDbContext.cs` la cual debe heredar las funcionalidades de `DbContext` la cual forma parte del `Microsoft.EntityFrameworkCore` , luego debemos crear un constructor

## Creacion DbContext

```c#
using Microsoft.EntityFrameworkCore;
using <nombre_proyecto>.Models

namespace <nombre_proyecto>.Db; // Db o Data por ser el nombre de la carpeta
{
	public class AppDbContext : DbContext
	{
		public AppDbContext(DbContextOptions<AppDbContext> options)
		: base(options)
		{
		}
		
		public DbSet<{nombre_model}> {nombre_tabla} { get; set; } 
		public DbSet<{nombre_model}> {nombre_tabla} { get; set; }
		// Se pueden tener mas
	}
}
```

En el `DbSet` lo que se pone entre brackets es el nombre de la clase del modelo y luego va el nombre de la tabla que va a quedar asignado a ese modelo

## Connection String

```c#
"Server=localhost;Database=<DB_NAME>;Integrated Security=false;User Id=<USERNAME>;Password=<USER PASSWORD>;TrustServerCertificate=True;Encrypt=False;"
```

## Registrar DbContext

Se debe registrar el `AppDbContext` en nuestro `Program.cs` como un *servicio *junto con su Connection String

```c#
// incluirlo con using <nombre_proyecto>.Db o .Data

builder.Services.AddDbContext<AppDbContext>(
	option => option.UseSqlServerbuilder.Configuration.GetConnectionString("Connection")
);
```

[[Migraciones en .NET y C con Entity Framework Core]]

[[Data Transfer Object (DTO)]]

[[Include y Relacion con EF]]

[[Actualizar un controlador PUT]]

[https://www.youtube.com/watch?v=CAF5cyjs5hY](https://www.youtube.com/watch?v=CAF5cyjs5hY)
