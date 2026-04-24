from __future__ import annotations
from ecs_quantitative.memory.agent_memory import get_memory
from .config import settings

# Instancia de memoria compartida para el lóbulo de innovación
brain = get_memory(collection_name=settings.rag_collection)
