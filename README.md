# 🏛️ LEI - Laboratorio de Economía de la Innovación 2026

## Emprendimiento y Economía de la Innovación (Ciclo 7) - UNL

El **Laboratorio de Economía de la Innovación (LEI)** estudia los motores del cambio tecnológico, los ecosistemas emprendedores y su impacto en la productividad regional.

---

## 🏗️ Arquitectura de Documentación

Organización de recursos académicos:

- **[Sílabo de la Materia](docs/syllabus/SYLLABUS.pdf)**: Guía de contenidos y evaluación.
- **[Lecturas y Referencias](docs/readings/)**: Material sobre Schumpeter, sistemas de innovación y emprendimiento.
- **[Índice documental por unidades](docs/README.md)**: Navegación por el sílabo y por las evidencias de cada unidad.
- **[Arquitectura](ARCHITECTURE.md)**: Estructura técnica del repo.
- **[Roadmap](ROADMAP.md)**: Seguimiento de unidades.

---

## 📄 Arquitectura de Reporteo (Quarto)

La redacción de informes y evidencia académica sigue el **Estándar Nivel 5**:
- El archivo `_quarto.yml` reside en la **raíz del repositorio**.
- Todo el output generado (HTML/PDF intermedios, dependencias JS/CSS) se concentra automáticamente en el directorio `_site/` o `dist/`.
- No existen carpetas `*_files/` ad-hoc. Todo está cubierto por el `.gitignore` canónico.

---

## 🚀 Guía de Inicio

```bash
# Sincronización de entorno
uv sync

# Análisis de innovación
python src/orchestration/M01-U1-LEI-Master_Build.py
```

---
*LEI - Centro de Investigación Econométrica. UNL.*
