# Subir el informe a GitHub

## Publicación desde la página web

1. Descomprimir el ZIP en una carpeta local.
2. Abrir [dani2176/informe-de-Eva-3](https://github.com/dani2176/informe-de-Eva-3).
3. Elegir **Add file → Upload files**.
4. Arrastrar **el contenido descomprimido**, manteniendo juntas las carpetas `ejemplos`, `herramientas` y `plantillas`, y los archivos de la raíz. No subir únicamente el ZIP: GitHub no mostrará su contenido como un informe navegable.
5. Revisar los archivos que ya existan para no reemplazar otros trabajos por error. Registrar el cambio con un mensaje descriptivo.
6. Abrir el README del repositorio y seguir **Informe completo en GitHub**. Comprobar que se muestran las tablas y las fracciones en la vista **Preview**.
7. Completar las revisiones e historial reales y crear la versión `v1.1` según la pauta del curso. Si el tag ya existe, no sobrescribirlo sin revisar a qué entrega corresponde.

## Estructura que debe quedar en la raíz

```text
README.md
COMO_SUBIR_A_GITHUB.md
CHANGELOG.md
requirements.txt
.gitignore
ejemplos/
  caso-valle-elqui/
    informe.md
    informe.docx
    informe.pdf
    objetivos.yaml
    mediciones.csv
    evidencia.json
    sla.md
    salida_calc.txt
    resultados.json
herramientas/
  calc_sla.py
  formulas.py
  regenerar.py
plantillas/
  informe_base.md
  formato_inacap.docx
```

## Si se usa Git en el computador

Clonar el repositorio en una carpeta nueva y copiar allí el contenido del paquete. Revisar `git status` antes de confirmar cambios. No copiar otra carpeta `.git`.

```bash
git clone https://github.com/dani2176/informe-de-Eva-3.git
cd informe-de-Eva-3
git switch -c mejora/presentacion-sla
```

Después de copiar y revisar los archivos:

```bash
git add README.md COMO_SUBIR_A_GITHUB.md CHANGELOG.md requirements.txt .gitignore ejemplos/ herramientas/ plantillas/
git commit -m "Mejora tablas, ecuaciones y lectura del informe SLA"
git push -u origin mejora/presentacion-sla
```

Integrar la rama mediante una solicitud de cambios o el procedimiento del grupo. Cuando la entrega esté cerrada en `main`, crear el tag `v1.1` si aún no existe. Los comandos de publicación no se ejecutaron durante la preparación de este paquete.
