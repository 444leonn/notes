---
cover: "[[Aprendiendo .NET]]"
---

# Aprendiendo .NET

Cuando creamos una nueva solucion para un proyecto de .NET, se nos crea una serie de carpetas que conforman la estructura de nuestro proyecto.

>[!IMPORTANT] Para crear una API con .NET hacemos:
>
>```bash
>dotnet new webapi -o <api_name>
>```

## Inicios de un Proyecto

Para todo proyecto de una ***Web API con ASP*** el “*entrypoint”* o punto de entrada de nuestra aplicacion es el archivo nombre `Program.cs`.

### Tipos de Proyecto para APIs

En .NET tenemos dos tipos de manera de desarrollar una API, puede ser la llamada ***minimal*** o la manejada por controladores.

>[!IMPORTANT] Para crear API minimal usamos:
>
>```bash
>dotnet new web -n MyMinimalApi
>```

### Builder

Dentro de `Program.cs` se almacena el `builder` de la aplicacion que se declara como `var builder = WebApplication.CreateBuilder(args);` .

El mismo representa un *constructor* al que yo le puedo agregar diferentes cosas y servicios.

Como por ejemplo: `builder.Services.AddSwaggerGen();`

### Servicios

Podemos decir que cada servicio representa un componente que vamos a estar utilizando en la aplicacion, ya sea externo o interno (hecho por nosotros mismos)

- Existen servicios generales de ASP.NET
- Existen servicios creados por nosotros

Luego de agregar los servicios, se buildea o construye la aplicacion con
`var app = builder.Build();`

Y una vez que ya construimos la app, le podemos agregar *middleware*

Para utilizar *controllers* utilizamos el servicio para agregarlos y luego los mapeamos

`builder.Services.AddControllers();`

### Middlewares

Son componentes que **manipulan los metodos** HTTP

- Se lo llama “***application request pipeline”*** o ***“pipeline”***
- El orden importa, se debe respetar un orden para llamarlos
- Ademas del servicio de agregar los controller debemos agregar el middleware con
`app.MapControllers();`

## MVC

Es un patron arquitectural de software, se puede interpretar como la manera o metodologia en la que definimos los distintos componentes que va a tener nuestro software.

Posee tres partes:

### Models

Pensemos a los models como clases que poseen la estructura de los datos, los cuales muy probablemente guardemos posteriormente en la base de datos.

Por lo general, al solo ser utilizados para almacenar la informacion, los models no requieren metodos.

### Frameworks a Utilizar

[[Migraciones en .NET y C con Entity Framework Core]]

[[Data Transfer Object (DTO)]]

[[Include y Relacion con EF]]

[[Actualizar un controlador PUT]]

#### Videos

[Crear una WEB API REST en C# | .NET CORE 9| 8 | (GET, POST, PUT,DELETE)](https://www.youtube.com/watch?v=CAF5cyjs5hY)
