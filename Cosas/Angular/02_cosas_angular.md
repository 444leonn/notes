# Cosas Varias de Angular

## Creacion de Proyecto

```bash
ng new <project-name>
```

## Levantar el localhost

```bash
ng serve
```

## Crear un Component

```bash
ng generate component <component-name>
```

## Peticiones Http

Para poder conectar nuestros componentes con un Backend debemos utilizar el `HttpClient`.

Y debemos tambien utilizar interfaces de typesrcipt que modelen los datos que nos llegan desde el backend.

## Formularios

Existen dos tipos de manera de construir los formularios:

- Reactivos
- Basados en Plantillas

### Reactivos

Para usar controles de formulario, hay tres pasos.

1. Generar un nuevo componente y registrar el módulo de formularios reactivos. Este módulo declara las directivas de formularios reactivos que necesitas para usar formularios reactivos.
2. Instanciar un FormControl.
3. Registrar el FormControl en la plantilla.

