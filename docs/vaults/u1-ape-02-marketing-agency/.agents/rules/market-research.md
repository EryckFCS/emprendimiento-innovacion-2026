---
name: market-research
description: Protocolo Metodológico de Validación Ágil y Análisis Cualitativo/Cuantitativo de Demanda
---

# Protocolo Metodológico de Validación Ágil

Este documento rige la validación comercial de la propuesta de valor de la agencia de marketing. Prohíbe el uso de encuestas académicas masivas ineficaces y prioriza la validación real con tomadores de decisiones y experimentos en el mercado (Test de Humo).

## 1. Validación Cualitativa: Entrevistas B2B en Profundidad
En lugar de cuestionarios masivos impersonales, la demanda inicial se validará mediante entrevistas directas con propietarios, administradores o gerentes de PYMEs:
*   **Enfoque**: Descubrir los cuellos de botella reales en su embudo de adquisición de clientes, el nivel de frustración con agencias anteriores, el presupuesto actual que asignan de manera informal y su comprensión del retorno de inversión (ROI) publicitario.
*   **Protocolo de Entrevista**:
    *   No vender la agencia al inicio; centrarse en explorar la problemática actual del entrevistado.
    *   Preguntar por comportamientos pasados y presentes (*"¿Cuánto gastó en publicidad el mes pasado?"*, *"¿Cómo midió las ventas resultantes?"*) en lugar de intenciones futuras (*"¿Contrataría a una agencia?"*).
*   **Consistencia y Sistematización**: Documentar cada entrevista en una matriz de problemas y mapear las respuestas en un **Mapa de Empatía** para extraer las barreras reales de contratación.

## 2. Validación Cuantitativa: Test de Humo (Smoke Test)
La validación del interés real y la disposición a pagar se realizará mediante una **Landing Page de Validación** activa de la agencia (diseñada en el directorio `web/`):
*   **Arquitectura del Experimento**:
    *   Una página web de una sola pantalla con una Propuesta de Valor Única clara y tres planes de servicio recurrentes explícitos con precios.
    *   Un botón de llamada a la acción (CTA) claro: *"Solicitar Auditoría Gratuita"* o *"Reservar Paquete"*.
    *   Un formulario para capturar datos de contacto (Lead Generation).
*   **Métricas de Conversión Clave**:
    *   **Tasa de Clics en los Planes (CTR)**: Porcentaje de usuarios que hacen clic en los botones de precios con respecto al total de visitas.
    *   **Tasa de Conversión de Leads (CR)**: Porcentaje de visitas que completan el formulario de registro para iniciar contacto.
    *   **Costo por Lead (CPL)** simulado para proyectar la viabilidad de adquisición en campañas activas.

## 3. Criterios de Éxito para la Validación
La propuesta de valor se considerará validada comercialmente si se alcanzan los siguientes hitos operativos:
1.  **Hito Cualitativo**: Al menos 8 de cada 10 PYMEs entrevistadas declaran que su mayor problema de marketing es la falta de certeza sobre si la publicidad digital genera ventas reales (atribución).
2.  **Hito Cuantitativo**: La Landing Page del Test de Humo obtiene una **Tasa de Conversión (CR) de leads $\ge 5\%$** de tráfico calificado de prueba.
