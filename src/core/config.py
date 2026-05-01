from __future__ import annotations
from ecs_quantitative.core.federation import FederatedNodeConfig


class NodeSettings(FederatedNodeConfig):
    """Configuración canonizada para el nodo innovation_economics."""

    project_name: str = "Innovation Economics (LEI)"
    rag_collection: str = "innovation_economics"


settings = NodeSettings()
