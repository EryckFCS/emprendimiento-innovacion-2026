import pytest
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
DOCS_DIR = REPO_ROOT / "docs"

VAULTS = ["evidence", "readings", "syllabus"]


def get_units():
    units = []
    for vault in VAULTS:
        vault_path = DOCS_DIR / vault
        if not vault_path.exists():
            continue
        for item in vault_path.iterdir():
            if item.is_dir() and not item.name.startswith("."):
                units.append((vault, item))
    return units


@pytest.mark.parametrize("vault_name, unit_path", get_units())
def test_unit_structure(vault_name, unit_path):
    """Valida la estructura interna de cada unidad según su tipo de bóveda."""

    # Unidades documentales y de evidencia usualmente tienen index.qmd o README.md
    index_file = unit_path / "index.qmd"
    readme_file = unit_path / "README.md"
    assert index_file.exists() or readme_file.exists(), f"La unidad {unit_path.name} en {vault_name} no tiene index.qmd ni README.md"

    # Assets folder is mandatory for all EXCEPT maybe some legacy ones, but we enforce it for Nivel 5
    assets_dir = unit_path / "assets"
    
    # Evidence specifics (Heavy)
    if vault_name == "evidence":
        # Enforce assets/ on evidence
        assert assets_dir.is_dir(), f"La unidad {unit_path.name} en {vault_name} no tiene carpeta assets/"

        mandatory_dirs = ["scripts", "logs", "data"]
        for d in mandatory_dirs:
            assert (
                unit_path / d
            ).is_dir(), f"La unidad analítica {unit_path.name} debe tener carpeta {d}/"
    else:
        # Document specifics (Light) - NO heavy folders
        forbidden_dirs = ["scripts", "logs", "data"]
        for d in forbidden_dirs:
            assert not (
                unit_path / d
            ).exists(), f"La unidad documental {unit_path.name} NO debe tener carpeta {d}/"


def test_no_flotantes_in_vault_root():
    """Valida que no haya archivos flotantes en la raíz de las bóvedas (excepto .gitignore o README)."""
    for vault in VAULTS:
        vault_path = DOCS_DIR / vault
        if not vault_path.exists():
            continue

        flotantes = [f for f in vault_path.iterdir() if f.is_file() and f.name not in [".gitignore", "README.md", ".gitkeep"]]

        assert (
            not flotantes
        ), f"Archivos flotantes prohibidos en docs/{vault}/: {[f.name for f in flotantes]}"


def test_no_flotantes_in_units():
    """Valida que no haya archivos flotantes en la raíz de cada unidad excepto los permitidos para Quarto."""
    for vault, unit_path in get_units():
        allowed_extensions = [".qmd", ".md", ".bib", ".yml"]
        allowed_files = [".gitignore"]

        flotantes = []
        for f in unit_path.iterdir():
            if f.is_file():
                if f.name in allowed_files:
                    continue
                if f.suffix in allowed_extensions:
                    continue
                flotantes.append(f)

        assert not flotantes, f"Archivos flotantes prohibidos en la unidad {unit_path.name} ({vault}): {[f.name for f in flotantes]}"
