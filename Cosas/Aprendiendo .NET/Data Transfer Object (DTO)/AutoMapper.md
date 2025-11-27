---

---
# **¿Qué es AutoMapper?**

AutoMapper es un mapeador de objetos. El mapeo de objetos funciona transformando un objeto de entrada de un tipo en un objeto de salida de un tipo diferente. Lo interesante de AutoMapper es que proporciona convenciones interesantes que simplifican la tarea de mapear el tipo A con el tipo B. Mientras el tipo B siga la convención establecida de AutoMapper, prácticamente no se requiere configuración para mapear dos tipos.

# **¿Por qué utilizar AutoMapper?**

Mapear código es aburrido. Probar código de mapeo es aún más aburrido. AutoMapper ofrece una configuración sencilla de tipos, así como pruebas sencillas de mapeos. La verdadera pregunta podría ser "¿por qué usar mapeo objeto-objeto?". El mapeo puede ocurrir en muchos lugares de una aplicación, pero principalmente en los límites entre capas, como entre las capas de IU/Dominio o las capas de Servicio/Dominio. Las preocupaciones de una capa a menudo entran en conflicto con las de otra, por lo que el mapeo objeto-objeto genera modelos segregados, donde las preocupaciones de cada capa solo pueden afectar a los tipos de esa capa.

# **¿Cómo uso AutoMapper?**

Primero, necesita un tipo de origen y uno de destino con los que trabajar. El diseño del tipo de destino puede verse influenciado por la capa en la que reside, pero AutoMapper funciona mejor siempre que los nombres de los miembros coincidan con los del tipo de origen. Si tiene un miembro de origen llamado "FirstName", este se asignará automáticamente a un miembro de destino llamado "FirstName". AutoMapper también admite [el aplanamiento](https://docs.automapper.io/en/stable/Getting-started.html#Flattening.html) .

AutoMapper ignorará las excepciones de referencia nula al asignar el origen al destino. Esto es así por diseño. Si no le convence este enfoque, puede combinar el de AutoMapper con [solucionadores de valores personalizados](https://docs.automapper.io/en/stable/Getting-started.html#Custom-value-resolvers.html) si es necesario.

Una vez que tenga sus tipos, puede crear un mapa para ambos usando a `MapperConfiguration`y CreateMap. Normalmente, solo necesita una `MapperConfiguration`instancia por dominio de aplicación y debe instanciarse durante el inicio. Puede ver más ejemplos de configuración inicial en [Configuración](https://docs.automapper.io/en/stable/Getting-started.html#Setup.html) .

`var config = ``**new**`` MapperConfiguration(cfg => cfg.CreateMap<Order, OrderDto>(), loggerFactory);`

El tipo de la izquierda es el tipo de origen y el de la derecha, el tipo de destino. Para realizar una asignación, llame a una de las `Map`sobrecargas:

`var mapper = config.CreateMapper();
``*// or*``var mapper = ``**new**`` Mapper(config);
OrderDto dto = mapper.Map<OrderDto>(order);`

La mayoría de las aplicaciones pueden usar la inyección de dependencia para inyectar la `IMapper`instancia creada.

AutoMapper también tiene versiones no genéricas de estos métodos, para aquellos casos en los que es posible que no conozca el tipo en el momento de la compilación.

# **¿Dónde configuro AutoMapper?**

La configuración solo debe realizarse una vez por dominio de aplicación. Esto significa que el mejor lugar para colocar el código de configuración es al inicio de la aplicación, como el archivo Global.asax para aplicaciones ASP.NET. Normalmente, la clase de arranque de configuración se encuentra en su propia clase, y esta se llama desde el método de inicio. La clase de arranque debe construir un `MapperConfiguration`objeto para configurar los mapas de tipos.

Para ASP.NET Core, el artículo [Inyección de dependencia](https://docs.automapper.io/en/stable/Getting-started.html#Dependency-injection.html#asp-net-core) muestra cómo configurar AutoMapper en su aplicación.

# **¿Cómo puedo probar mis asignaciones?**

Para probar sus asignaciones, debe crear una prueba que haga dos cosas:

- Llama a tu clase bootstrapper para crear todas las asignaciones
- Llamar a MapperConfiguration.AssertConfigurationIsValid

He aquí un ejemplo:

`var config = AutoMapperConfiguration.Configure();

config.AssertConfigurationIsValid();`

![[net-automapper.png]]
