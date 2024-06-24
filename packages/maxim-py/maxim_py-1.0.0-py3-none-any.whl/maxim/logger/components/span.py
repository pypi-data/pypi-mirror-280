from dataclasses import dataclass
from typing import Dict, List, Optional

from ..writer import LogWriter
from .base import EventEmittingBaseContainer
from .generation import Generation, GenerationConfig
from .retrieval import Retrieval, RetrievalConfig
from .trace import Trace
from .types import Entity


@dataclass
class SpanConfig:
    id: str
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class Span(EventEmittingBaseContainer):
    ENTITY = Entity.SPAN

    def __init__(self, config: SpanConfig, writer: LogWriter):
        super().__init__(self.ENTITY, config.__dict__, writer)
        self.traces: List[Trace] = []
        self.commit("create")

    def generation(self, config: GenerationConfig) -> Generation:
        generation = Generation(config, self.writer)
        payload = generation.data()
        payload["id"] = config.id
        payload["spanId"] = self.id
        self.commit("add-generation", {
            **payload,
        })
        return generation

    def retrieval(self, config: RetrievalConfig):
        retrieval = Retrieval(config, self.writer)
        self.commit("add-retrieval", {
            "id": config.id,
            **retrieval.data(),
        })
        return retrieval
