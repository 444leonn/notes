---

---
Podemos utilizarlo para retornar mensajes, sin tener que estar tipeandolos a manos, y predefiniendolos.

Dentro de una carpeta Helper, creamos una clase Mensajes.cs

Ejemplo simple:

```c#
namespace <NombreSolucion>.Mensajes;

public static class Mensajes
{
	public static class <NombreClase>
	{
		public const string NotFound = "El/la <NommbreClase> no existe";
	}
}
```