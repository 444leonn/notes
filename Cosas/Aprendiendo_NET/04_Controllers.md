
# Controllers

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

- *ActionResult* nos permite retornar todos las cosas necesarias para nuestra peticion.
- *IEnumerable* nos permite devolver mas de un valor, por ejemplo mas clase de las de Mandril

La misma idea es la seguida para realizar la peticion de un POST, PUT o DELETE, o incluso de mas GET. Lo importante es seguir la convencion de utilizar Controller’s asociados con modelos especificos.
