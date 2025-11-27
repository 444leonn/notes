#!/usr/bin/env python3

import os
import re
from pathlib import Path

def calcular_ruta_relativa(archivo_md, carpeta_images):
    """Calcula la ruta relativa desde el .md hasta /images"""
    ruta_md = Path(archivo_md).parent
    ruta_images = Path(carpeta_images)
    return os.path.relpath(ruta_images, ruta_md)

def reemplazar_imagenes(directorio_raiz):
    patron = r'!\[\[([^\]]+)\]\]'
    carpeta_images = os.path.join(directorio_raiz, 'images')

    for root, dirs, files in os.walk(directorio_raiz):
        for file in files:
            if file.endswith('.md'):
                ruta_completa = os.path.join(root, file)
                ruta_relativa = calcular_ruta_relativa(ruta_completa, carpeta_images)

                with open(ruta_completa, 'r', encoding='utf-8') as f:
                    contenido = f.read()

                # Reemplazar con la ruta relativa correcta
                contenido_nuevo = re.sub(
                    patron,
                    lambda m: f"![]({ruta_relativa}/{m.group(1)})",
                    contenido
                )

                if contenido != contenido_nuevo:
                    with open(ruta_completa, 'w', encoding='utf-8') as f:
                        f.write(contenido_nuevo)
                    print(f"Actualizado: {ruta_completa}")
                    print(f"  Ruta usada: {ruta_relativa}/")

# Ejecutar desde el directorio raíz actual
reemplazar_imagenes('.')
