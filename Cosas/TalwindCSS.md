# Cosas de TailwindCSS

## Estilos Personalizados

Para crear estilos personalizados debemos crear un archivo `input.css` e importar tailwind, luego hacemos `@theme{}` y dentro ponemos las variables para los estilos que queremos crear.

Ejemplo:

```css
@import 'tailwincss';

@theme {
    --color-primario: #09f;

    -breakpoint-xs: 350px;
}
```

## Evitar que VSCode nos warmee de que no reconoce @apply o @theme

Debemos crear dentro de la carpeta `/.vscode` un archivo `settings.json` y colocar lo siguiente

```json
{
    "file.associations": {
        "*.css": "tailwindcss",
    }
}
```