# Clases vs Structs de C

En C trabajabas con `struct` así:

```c
struct Persona {
    char nombre[50];
    int edad;
};
```

En C# las **clases** son similares pero con superpoderes:

```csharp
public class Persona 
{
    public string Nombre { get; set; }
    public int Edad { get; set; }
    
    // Constructor
    public Persona(string nombre, int edad) 
    {
        Nombre = nombre;
        Edad = edad;
    }
    
    // Método (función dentro de la clase)
    public void Saludar() 
    {
        Console.WriteLine($"Hola, soy {Nombre}");
    }
}
```

**Diferencias clave:**

- Las clases pueden tener **métodos** (funciones que operan sobre los datos)
- Tienen **constructores** (funciones especiales para crear instancias)
- Las **propiedades** (`{ get; set; }`) son como campos pero con lógica opcional

## Interfaces

Una **interface** es como un contrato. Define *qué* debe hacer algo, pero no *cómo*.

Imaginate que en C querías que diferentes structs tengan una función `calcular_area()`. Tendrías que definir la función para cada uno manualmente. Las interfaces te permiten garantizar que ciertas clases implementen ciertos métodos:

```csharp
public interface IFigura 
{
    double CalcularArea();
    double CalcularPerimetro();
}

public class Circulo : IFigura  // ":" significa "implementa"
{
    public double Radio { get; set; }
    
    public double CalcularArea() 
    {
        return Math.PI * Radio * Radio;
    }
    
    public double CalcularPerimetro() 
    {
        return 2 * Math.PI * Radio;
    }
}

public class Rectangulo : IFigura 
{
    public double Base { get; set; }
    public double Altura { get; set; }
    
    public double CalcularArea() 
    {
        return Base * Altura;
    }
    
    public double CalcularPerimetro() 
    {
        return 2 * (Base + Altura);
    }
}
```

Ahora podés hacer esto:

```csharp
IFigura[] figuras = new IFigura[] 
{
    new Circulo { Radio = 5 },
    new Rectangulo { Base = 10, Altura = 5 }
};

foreach (var figura in figuras) 
{
    Console.WriteLine($"Área: {figura.CalcularArea()}");
}
```

## ICollection y colecciones

`ICollection<T>` es una **interface** que representa una colección de elementos. El `<T>` es un **genérico** (como templates en C++).

En C trabajabas con arrays fijos:

```c
int numeros[10];
```

En C# tenés varias opciones:

```csharp
// Array (tamaño fijo, como en C)
int[] numeros = new int[10];

// List<T> (tamaño dinámico, como un vector/ArrayList)
List<int> lista = new List<int>();
lista.Add(5);
lista.Add(10);

// ICollection<T> es la interface que implementan List, HashSet, etc.
ICollection<int> coleccion = new List<int>();
```

**¿Por qué usar `ICollection<T>` en lugar de `List<T>`?**

Cuando defines un método o propiedad, usar la interface te da flexibilidad:

```csharp
public class Producto 
{
    public string Nombre { get; set; }
    public decimal Precio { get; set; }
}

public class Carrito 
{
    // Puede ser List, HashSet, o cualquier cosa que implemente ICollection
    public ICollection<Producto> Productos { get; set; } = new List<Producto>();
}
```

## En Entity Framework

En EF (para bases de datos), las clases representan **tablas** y las propiedades representan **columnas**:

```csharp
public class Usuario 
{
    public int Id { get; set; }  // Clave primaria
    public string Email { get; set; }
    
    // Relación uno a muchos: un usuario tiene muchos posts
    public ICollection<Post> Posts { get; set; }
}

public class Post 
{
    public int Id { get; set; }
    public string Titulo { get; set; }
    public string Contenido { get; set; }
    
    // Relación: este post pertenece a un usuario
    public int UsuarioId { get; set; }  // Foreign key
    public Usuario Usuario { get; set; }  // Navegación
}
```

Aquí `ICollection<Post>` permite que EF maneje la relación automáticamente. Cuando cargás un usuario, podés acceder a `usuario.Posts` y obtener todos sus posts.

## Resumen rápido

- **Clase**: struct de C + funciones + comportamiento
- **Interface**: contrato que define qué métodos debe tener algo
- **`ICollection<T>`**: interface para colecciones (listas, sets, etc.)
- **Genéricos (`<T>`)**: como templates, te permiten reutilizar código para diferentes tipos
