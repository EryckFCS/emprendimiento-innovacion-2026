import os
from pathlib import Path
from typing import Any

class Settings:
    def __init__(self):
        self.project_name = "LEI - Laboratorio de Economía de la Innovación"
        self.root_path = Path(__file__).parent.parent.parent
        self.config_path = self.root_path / "pyproject.toml"

settings = Settings()
