# AGENTS.md — High-Fidelity Federated Node: Laboratorio de Economía de la Innovación (LEI)

> This repository is a **Level 5 Pure Node** in the Federated Architecture v7.4.0.  
> It operates under the Constitution centralized in:
> `/home/erick-fcs/Capital_Workstation/capital-workstation-libs/.github/copilot-instructions.md`
> and the supervision of the **Vault Architect**.

---

## 1. Node Identity and Governance

| Field | Value |
|:---|:---|
| **Node** | Laboratorio de Economía de la Innovación (LEI) |
| **Status** | Active — Content Synthesis Phase |
| **Teacher** | Econ. Jose Vicente Ordoñez Yaguache |
| **Student** | Erick Fabricio Condoy Seraquive |
| **Central Library** | `ecs_quantitative` (capital-workstation-libs) |
| **Intelligence Level** | 5 — Intelligent Ecosystem with Controlled Autonomy |
| **Gatekeeper** | `tests/test_vault_architecture.py` (Mandatory) |
| **RAG** | `global_knowledge` (Federated Vector Store) |

---

## 2. Advanced Intelligence Capabilities (v2.0)

This node is an **autonomous inference unit** designed for:

1.  **Innovation Systems Audit**: Real-time evaluation of economic structures against the Schumpeterian and National Innovation Systems frameworks.
2.  **Federated Knowledge Consumption**: Deep integration with `ecs_quantitative` for data-driven innovation metrics and statistical modeling.
3.  **Atomic Evidence Mapping**: Absolute traceability between theoretical readings (`docs/readings/`) and empirical lab workshops (`docs/evidence/`).

---

## 3. Operational Protocols (Active Directives)

### 3.1. Guardian Protocol (Architecture Gatekeeper)
- **Invariant**: Every structural change must be validated by the architectural test suite.
- **Action**: Before closing any task, the agent MUST execute `uv run pytest tests/test_vault_architecture.py`.
- **Failure**: If the test fails, the repository is considered "Unstable" and the absolute priority is to restore atomic symmetry.

### 3.2. Research Protocol (Analytic Loop)
1.  **Detection**: Identify if the task is "Theory" (Readings) or "Application" (Evidence).
2.  **Location**: Analytical scripts and execution outputs MUST live in their respective sub-vault under `docs/evidence/`.
3.  **Registration**: Each analysis must generate reproducible logs in its local `logs/` folder to guarantee forensic reproducibility.

---

## 4. Vault Architecture (Atomic Level 5)

### 4.1. Analytical Structure (`docs/evidence/`)
Every workshop, report, or business model application (e.g., CEL) is an isolated unit:
```text
docs/evidence/[unit]/
├── index.qmd               # Orchestrator and narrative
├── scripts/                # Local logic or data extraction
├── logs/                   # Execution evidence
├── assets/                 # Final figures, diagrams, and reports
└── data/                   # Specific datasets
```
*(Note: Quarto source files like `*.qmd` and `*.bib` are permitted in the unit root to accommodate complex multi-document rendering).*

### 4.2. Documentary Structure (`readings/`, `syllabus/`)
```text
docs/[vault]/[unit]/
├── index.qmd               # Master document
└── assets/                 # Static assets (PDFs, readings)
```

---

## 5. Resilience Strategy

1.  **Zero Floating Doctrine**: No unapproved files can exist in the root of a unit. All analytical outputs must be in `logs/` or `assets/`.
2.  **Path Integrity**: Use absolute or library-resolved paths to avoid fragility.

---

## 6. Environment and Maintenance

```bash
# Environment Sync
uv sync

# Architecture Audit
uv run pytest tests/test_vault_architecture.py

# Evidence Rendering (Example)
quarto render docs/evidence/Business-Project-CEL/index.qmd --to pdf
```

---

## Golden Rule

> **If the repository's reality contradicts this document, the agent must correct the repository or propose an amendment to AGENTS.md.** Federated knowledge is the only reproducible truth. If something implemented here is useful for other subjects, propose it for the central library.
