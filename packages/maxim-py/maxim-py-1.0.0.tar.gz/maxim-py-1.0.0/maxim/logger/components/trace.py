from dataclasses import dataclass
from typing import Dict, Optional,TYPE_CHECKING

from ..writer import LogWriter
from .base import EventEmittingBaseContainer
from .feedback import Feedback
from .generation import Generation, GenerationConfig
from .retrieval import Retrieval, RetrievalConfig
from .types import Entity
if TYPE_CHECKING:
    from .span import Span, SpanConfig  # Type checking only

@dataclass
class TraceConfig:
    id: str
    name: Optional[str] = None
    session_id: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class Trace(EventEmittingBaseContainer):
    def __init__(self, config: TraceConfig, writer: LogWriter):
        super().__init__(Entity.TRACE, config.__dict__, writer)
        self.commit("create", {
            **self.data(),
            "sessionId": config.session_id,
        })

    def generation(self, config: GenerationConfig) -> Generation:
        generation = Generation(config, self.writer)
        self.commit("add-generation", {
            **generation.data(),
            "id": generation.id,
        })
        return generation

    def retrieval(self, config: RetrievalConfig):
        retrieval = Retrieval(config, self.writer)
        self.commit("add-retrieval", {
            "id": config.id,
            **retrieval.data(),
        })
        return retrieval

    def span(self, config: 'SpanConfig') -> 'Span':
        from .span import Span, SpanConfig
        span = Span(config, self.writer)
        self.commit("add-span", {
            "id": config.id,
            **span.data(),
        })
        return span

    def feedback(self, feedback: Feedback):
        self.commit("add-feedback", feedback.__dict__)
