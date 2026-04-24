from __future__ import annotations
from pathlib import Path

class Settings:
    """Configuración del nodo LEI - Innovación y Emprendimiento."""
    
    # Ruta base del proyecto
    root_path: Path = Path(__file__).resolve().parent.parent.parent
    
    # Identidad
    project_name: str = "Laboratorio de Economía de la Innovación (LEI)"
    
    # RAG
    rag_collection: str = "innovation_economics"

settings = Settings()
