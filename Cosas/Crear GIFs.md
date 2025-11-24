---

---
## 🔹 Paso 1. Crear las capturas

1. Escribís tu array en un editor de texto (puede ser VS Code, Notepad++, Word, o incluso un Google Docs).
2. Vas cambiando los números manualmente en cada paso (como si mostraras un algoritmo).
3. Sacás una **captura de pantalla** de cada estado:
    - En Windows → `Win + Shift + S`
    - En Linux → `Shift + PrtSc` o **Flameshot/Peek**
    - En macOS → `Cmd + Shift + 4`

---

## 🔹 Paso 2. Unirlas en un GIF

Con esas imágenes podés armar el GIF con varias herramientas:

### 🔧 Linux

- **ImageMagick**:
```bash
convert -delay 80 -loop 0 frame1.png frame2.png frame3.png animacion.gif

```
(`-delay 80` ajusta la velocidad)
- **Peek** → grabás la carpeta con las imágenes abiertas en un visor.

### 🔧 Windows

- [**ScreenToGif**](https://www.screentogif.com/) → podés importar imágenes y ordenarlas como frames.
- O con **IrfanView** → crear GIFs desde múltiples imágenes.

### 🔧 Online

- [ezgif.com](https://ezgif.com/maker) → subís las capturas y genera el GIF.

---

## 🔹 Paso 3. Insertar en Markdown

Una vez creado `animacion.gif`, lo agregás:

```markdown
![Animación de ordenamiento](animacion.gif)

```

---