import json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from ..writer import LogWriter
from .base import BaseContainer
from .types import Entity


@dataclass
class GenerationConfig:
    id: str
    provider: str
    model: str
    messages: List[Any] = field(default_factory=list)
    model_parameters: Dict[str, Any] = field(default_factory=dict)
    span_id: Optional[str] = None
    name: Optional[str] = None
    maxim_prompt_id: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class Generation(BaseContainer):
    def __init__(self, config: GenerationConfig, writer: LogWriter):
        super().__init__(Entity.GENERATION, config.__dict__, writer)
        self.model = config.model
        self.maxim_prompt_id = config.maxim_prompt_id
        self.messages = []
        self.provider = config.provider
        self.messages.extend(config.messages)
        self.model_parameters = config.model_parameters

    def set_model(self, model: str):
        self.model = model
        self.commit("update", {"model": model})

    def add_message(self, message: Any):
        self.messages.append(message)
        self.commit("update", {"messages": [message]})

    def set_model_parameters(self, model_parameters: Dict[str, Any]):
        self.model_parameters = model_parameters
        self.commit("update", {"model_parameters": model_parameters})

    def result(self, result: Any):
        self.commit("result", {"result": result})
        self.end()

    def data(self) -> Dict[str, Any]:
        base_data = super().data()
        return {
            **base_data,
            "model": self.model,
            "provider": self.provider,
            "maximPromptId": self.maxim_prompt_id,
            "messages": self.messages,
            "modelParameters": self.model_parameters,
        }
