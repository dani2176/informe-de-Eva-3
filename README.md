# Verificación del SLA de Agrícola Valle de Elqui

**Evaluación 3 · Septiembre de 2026 · INACAP La Serena**

Informe de Daniel Videla para Infraestructura de Telecomunicaciones Avanzada, carrera Ingeniería en Telecomunicaciones, Conectividad y Redes. Profesor: Daniel Ruz.

## Leer el trabajo

| Documento | Uso |
|---|---|
| [Informe completo en GitHub](ejemplos/caso-valle-elqui/informe.md) | Lectura en línea con tablas y ecuaciones matemáticas |
| [Informe PDF](ejemplos/caso-valle-elqui/informe.pdf) | Presentación con formato INACAP y páginas fijas |
| [Informe Word](ejemplos/caso-valle-elqui/informe.docx) | Edición con ecuaciones nativas de Word |
| [Guía para subir los archivos](COMO_SUBIR_A_GITHUB.md) | Publicación del contenido descomprimido |

## Resultado principal

El servicio incumple disponibilidad y tiempo de respuesta. El crédito acreditado es **15 % del cargo mensual, equivalente a 180.000 CLP netos**.

| Indicador | Objetivo | Resultado | Veredicto |
|---|---:|---:|---|
| Disponibilidad | ≥ 99,9 % | 99,62963 % | No cumple |
| Latencia RTT | ≤ 30 ms | 27,4 ms | Cumple |
| Jitter | ≤ 10 ms | 9,91945 ms | Cumple el agregado; requiere respaldo de trazabilidad |
| Pérdida | ≤ 0,5 % mensual | Solo 60 % de cobertura | Evidencia insuficiente |
| Throughput | ≥ 180 Mbps | 180,75 Mbps | Cumple |
| Primera respuesta | ≤ 60 min en todos los tickets | Máximo 66 min | No cumple |
| Restauración | ≤ 240 min por incidente atribuible | Máximo 75 min | Cumple |

```math
A=\frac{43\,200-160}{43\,200}\times100=99{,}62963\,\%
```

La pérdida parcial no se convierte en un incumplimiento. La reserva de jitter se explica en la metodología del informe y no altera el crédito acreditado.

## Datos y trazabilidad

| Archivo | Contenido |
|---|---|
| [sla.md](ejemplos/caso-valle-elqui/sla.md) | Extracto contractual |
| [objetivos.yaml](ejemplos/caso-valle-elqui/objetivos.yaml) | Umbrales, tramos y cargo mensual |
| [mediciones.csv](ejemplos/caso-valle-elqui/mediciones.csv) | Mediciones utilizadas |
| [evidencia.json](ejemplos/caso-valle-elqui/evidencia.json) | Grupos de jitter, cobertura y eventos |
| [salida_calc.txt](ejemplos/caso-valle-elqui/salida_calc.txt) | Salida completa de la calculadora |
| [resultados.json](ejemplos/caso-valle-elqui/resultados.json) | Resultados sin redondear |
| [CHANGELOG.md](CHANGELOG.md) | Cambios y tareas pendientes |

## Reproducir los documentos

Desde la raíz de este repositorio, con Python 3.10 o posterior:

```bash
python -m pip install -r requirements.txt
python herramientas/regenerar.py
```

La ejecución recalcula los indicadores y genera Markdown, Word y PDF en `ejemplos/caso-valle-elqui/`. El PDF se genera con ReportLab; Word puede distribuir las líneas de forma ligeramente distinta. Las fórmulas de Word son editables y las de GitHub usan bloques `math`.

Los objetivos se guardan con sintaxis JSON compatible con YAML 1.2. No se necesita PyYAML. El contenido se edita en [plantillas/informe_base.md](plantillas/informe_base.md); los archivos `informe.*` son salidas generadas. Si cambian las mediciones, deben revisarse también las interpretaciones y los valores fijos de la redacción.

## Presentación en GitHub

Abrir `informe.md` en la pestaña **Preview**, no en **Code** ni **Raw**. Los saltos de página usados para impresión se eliminan en esta versión y las fórmulas se muestran fuera de las tablas para mantener su legibilidad. El visor de GitHub ofrece navegación por encabezados.

Formato basado en la documentación de GitHub sobre [expresiones matemáticas](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions) y [tablas](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-tables).

## Estado de publicación

Este paquete está preparado para el repositorio `dani2176/informe-de-Eva-3`. La preparación local no acredita un envío a GitHub ni la existencia del tag `v1.1`. La declaración de asistencia está en la sección 09 del informe; el historial y las revisiones personales deben reflejar acciones reales.
