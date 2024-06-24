from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Optional

from ..writer import LogWriter
from .base import BaseContainer
from .types import Entity


@dataclass
class RetrievalConfig():
    id: str
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class Retrieval(BaseContainer):
    def __init__(self, config: RetrievalConfig, writer: LogWriter):
        super().__init__(Entity.RETRIEVAL, config.__dict__, writer)
        self.commit("create")

    def input(self, query: str):
        self.commit("update", {"input": query})
        self.end()

    def output(self, docs: Any):
        self.commit("output", {"docs": docs, "endTimestamp": datetime.now()})
        self.end()
