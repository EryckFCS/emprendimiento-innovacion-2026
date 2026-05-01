# Architecture - Innovation Economics (LEI)

## Purpose

This repository organizes the evidence, canonical writing, and documentary management of the LEI node under the **Federated Architecture v8.0.0**.

## Work Layers

- **`docs/vaults/`**: Forensic evidence vaults (`uX-[cat]-[seq]-slug`).
- **`docs/writing/`**: Canonical narrative and high-fidelity deliveries.
- **`docs/management/`**: Planning, architecture reports, and risk management.
- **`docs/readings/`**: Theoretical support and thematic literature.
- **`docs/syllabus/`**: Institutional guidelines and official syllabus.
- **`bibliography/`**: Universal Sanitization Protocol (USP) pipeline.
- **`config/`**: Intelligence mapping and node configuration.
- **`src/`**: Core domain logic and task orchestration.
- **`tests/`**: Gatekeepers and architectural compliance suites.

## Governance Rules

1. **Zero Floating Doctrine**: No analytical or raw files are allowed in the repository root. All research MUST live within a vault.
2. **Standardized Naming**: All vaults must follow the institutional naming convention.
3. **USP Compliance**: Literature MUST be sanitized through the USP pipeline before RAG ingestion.
4. **Path Resilience**: Use relative pathing within vaults to ensure portability.


## Intervención v8.1.5 (Endurecimiento)

El nodo ha sido endurecido y unificado en Python 3.12. Se eliminaron archivos flotantes y se centralizó la gestión del Data Lake vía `ecs_core`.