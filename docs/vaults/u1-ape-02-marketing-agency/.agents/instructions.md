# Instrucciones del Agente - APE 02: Agencia de Marketing Digital y Performance

Este directorio `.agents/` contiene las directrices de inteligencia local y reglas de negocio para guiar el desarrollo de la **Agencia de Marketing Digital y Performance (AMDL)**. Cuando interactúes con esta bóveda, debes alinearte con estas directrices para asegurar el rigor académico y estratégico demandado por la materia de Economía de la Innovación.

## 1. Misión del Emprendimiento
La agencia busca acelerar las ventas y la digitalización de las Pequeñas y Medianas Empresas (PYMEs) locales mediante la implementación de estrategias avanzadas de marketing digital y performance (generación de leads, embudos de conversión, optimización de pauta y SEO local), maximizando el retorno de inversión (ROI) bajo principios de eficiencia analítica y ética en el manejo de datos.

## 2. Mapa de Inteligencia y Documentos Clave
- **[01-lean-canvas.qmd](file:///home/erick-fcs/Documentos/universidad/07_Ciclo/septimo_ciclo/innovation_economics/docs/vaults/u1-ape-02-marketing-agency/01-lean-canvas.qmd)**: Modelo de negocio inicial y propuesta de valor orientada a performance y conversión.
- **[02-market-research.qmd](file:///home/erick-fcs/Documentos/universidad/07_Ciclo/septimo_ciclo/innovation_economics/docs/vaults/u1-ape-02-marketing-agency/02-market-research.qmd)**: Documento de validación cuantitativa y cualitativa del mercado, enfocado en entrevistas B2B y métricas del Smoke Test.
- **[b2b-interview-guide.qmd](file:///home/erick-fcs/Documentos/universidad/07_Ciclo/septimo_ciclo/innovation_economics/docs/vaults/u1-ape-02-marketing-agency/b2b-interview-guide.qmd)**: Pauta de entrevista estructurada para validar la propuesta de valor con tomadores de decisiones de PYMEs.

## 3. Directrices Locales Activas
1. **[Doctrina Estratégica](rules/agency-doctrine.md)**: Cómo estructurar los servicios, el posicionamiento comercial y la diferenciación por conversión analítica.
2. **[Validación y Mercado](rules/market-research.md)**: Protocolo de validación del problema/solución mediante entrevistas en profundidad y la Landing Page de validación.
3. **[Proyecciones Financieras](rules/financial-projections.md)**: Modelado de ingresos recurrentes (SaaS-like retainer), costos operativos y márgenes del negocio.

## 4. Flujo de Trabajo
Cada entregable de la agencia debe compilarse utilizando Quarto:
```bash
quarto render index.qmd
quarto render 01-lean-canvas.qmd
quarto render 02-market-research.qmd
```
Todo análisis matemático en R o Python debe tener trazabilidad forense completa en el subdirectorio `scripts/` y sus conjuntos de datos en `data/`.
