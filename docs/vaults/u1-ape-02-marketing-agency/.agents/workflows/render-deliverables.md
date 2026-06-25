---
name: render-deliverables
description: Flujo de trabajo para compilación, validación y compilación final Quarto de la Agencia de Marketing
---

# Workflow: Compilación y Validación de Entregables

Este flujo de trabajo guía al agente en el proceso de renderizado y aseguramiento de calidad de los documentos académicos y de negocio del proyecto.

## Paso 1: Auditoría del Entorno
*   Verificar que la versión de Python del entorno virtual sea correcta:
    ```bash
    ./.venv/bin/python --version
    ```

## Paso 2: Renderizar Documento de Lean Canvas
*   Compilar el Lean Canvas en múltiples formatos:
    ```bash
    quarto render 01-lean-canvas.qmd --to html
    quarto render 01-lean-canvas.qmd --to pdf
    ```

## Paso 3: Renderizar Investigación de Mercados
*   Asegurar que todas las librerías estadísticas (como Pandas, NumPy o Matplotlib) estén instaladas antes de compilar:
    ```bash
    quarto render 02-market-research.qmd --to html
    ```

## Paso 4: Verificación Visual e Inferencia
*   Confirmar que las ecuaciones matemáticas del tamaño muestral y los gráficos de `data/` se muestran correctamente en los archivos `.html` y `.pdf` resultantes.
