---
name: financial-projections
description: Directrices de Modelado Financiero, Costos y Análisis de Viabilidad Económica
---

# Directrices de Modelado y Proyecciones Financieras

Rige la simulación económica de viabilidad de la agencia. Prohíbe estimaciones optimistas infundadas.

## 1. Arquitectura de Ingresos (Pricing)
*   **Modelo de Retenedores Mensuales (Retainers)**: El flujo de ingresos debe modelarse a través de tres niveles de servicio recurrentes (Básico, Intermedio, Avanzado).
*   **Willingness to Pay (WTP)**: Los precios de los paquetes deben estar estrictamente correlacionados y justificados por los resultados de la encuesta de investigación de mercado (`02-market-research.qmd`).
*   **Proyección de Cohortes y Churn**: Incorporar una tasa de pérdida mensual de clientes (*churn rate*) de al menos el 5% al 10% en escenarios conservadores para evitar sobreestimar el crecimiento a largo plazo.

## 2. Estructura de Costos y Recursos
*   **Costos Fijos**: Detallar salarios del equipo core, licencias de software (CRM, herramientas SEO, analítica), hosting ecológico y costos administrativos mínimos.
*   **Costos Variables**: Costos de adquisición de pauta digital de terceros (que deben ser transparentes e idealmente facturados directamente al cliente final), y comisiones por ventas o diseñadores/desarrolladores freelancers de apoyo.
*   **Métricas Unitarias Clave (LTV / CAC)**:
    *   **Customer Acquisition Cost (CAC)**: Debe incorporar pauta propia, tiempo del comercial y costo de herramientas.
    *   **Lifetime Value (LTV)**: Basado en el ticket promedio mensual de los retenedores y la tasa de abandono estimada.
    *   **Ratio de Salud Financiera**: Apuntar a un ratio $LTV/CAC \ge 3.0$ a partir del mes 6 de operación estable.

## 3. Análisis de Rentabilidad y Sensibilidad
*   **Punto de Equilibrio (Break-Even Point)**: Calcular exactamente cuántos clientes estables en cada plan son necesarios para cubrir la estructura de costos mensuales fijos.
*   **Simulaciones de Sensibilidad**: Presentar tres escenarios en la evaluación financiera final:
    1.  **Pesimista**: Alta tasa de churn, baja WTP de las PYMEs, y CAC elevado.
    2.  **Base**: Consistente con las medianas de la encuesta.
    3.  **Optimista**: Adopción acelerada e introducción de servicios de consultoría premium.
