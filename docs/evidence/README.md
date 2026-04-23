# Bóveda de Evidencia — Laboratorio de Economía de la Innovación (LEI)

> Nodo Federado v7.4.0 | Período: Marzo - Agosto 2026

Este directorio contiene toda la evidencia académica reproducible del nodo LEI, organizada por Unidad Didáctica y tipo de actividad.

## Estructura Canónica

```
docs/evidence/
└── U1-Sistemas-Innovacion/
    ├── Boveda_Lecturas/          # Control de lecturas y síntesis bibliográfica
    └── Boveda_Taller_Aplicado/   # Talleres de clase y aprendizaje autónomo
```

## Índice de Evidencias

| Unidad | Actividad | Archivo | Estado |
|:---|:---|:---|:---|
| U1 | Sistemas de Innovación | [U1-Sistemas-Innovacion/](U1-Sistemas-Innovacion/) | 🔄 En construcción |
| Proyecto | Consultora Económica Loja | [Business-Project-CEL/](Business-Project-CEL/index.qmd) | 🚀 Inicializado |

## Gobernanza

- Todos los archivos de evidencia deben ser **Quarto (`.qmd`)**.
- Los metadatos YAML deben ser minimalistas y **libres de comillas** innecesarias.
- Los diagramas complejos usan `layout-ncol: 2` (Doctrina Mermaid).
- Documentos con interactividad OJS usan `.content-visible` para dualidad HTML/PDF.
- Este índice debe actualizarse en cada sesión de trabajo.

## Vincular al RAG

```bash
# Consultar el cerebro central para este nodo
uv run python -c "
from src.core.brain import brain
results = brain.query('sistemas nacionales de innovación', n_results=5)
for r in results:
    print(r)
"
```
