# LEI - Laboratorio de Economia de la Innovacion 2026

El Laboratorio de Economia de la Innovacion organiza la evidencia, la escritura canonica y la gestion documental del nodo.

## Arquitectura de Documentacion

- [Indice documental](docs/README.md)
- [Boveda de evidencias](docs/vaults/README.md)
- [Boveda de escritura](docs/writing/index.qmd)
- [Boveda de gestion](docs/management/index.qmd)
- [Boveda de lecturas](docs/readings/index.qmd)
- [Silabo oficial](docs/syllabus/oficial/index.qmd)
- [Arquitectura](ARCHITECTURE.md)
- [Roadmap](ROADMAP.md)

## Guia de Inicio

```bash
uv sync
uv run python main.py
uv run pytest tests/test_vault_architecture.py tests/test_main.py
quarto render docs/vaults/Business-Project-CEL/index.qmd --to pdf
```

La carpeta `writing/` en la raiz se conserva solo como transicion historica.
