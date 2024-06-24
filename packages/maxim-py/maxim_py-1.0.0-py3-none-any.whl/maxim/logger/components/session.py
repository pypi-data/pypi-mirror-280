from dataclasses import dataclass
from typing import Dict, Optional

from ..writer import LogWriter
from .base import EventEmittingBaseContainer
from .feedback import Feedback
from .trace import Trace, TraceConfig
from .types import Entity


@dataclass
class SessionConfig:
    id: str
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class Session(EventEmittingBaseContainer):
    ENTITY = Entity.SESSION

    def __init__(self, config: SessionConfig, writer: LogWriter):
        super().__init__(Session.ENTITY, config.__dict__, writer)
        self.commit("create")

    def trace(self, config: TraceConfig) -> Trace:
        # Assuming TraceConfig in Python has a session_id attribute
        config.session_id = self.id
        return Trace(config, self.writer)

    def feedback(self, feedback: Feedback):
        self.commit("add-feedback", feedback.__dict__)
