from dataclasses import field
from datetime import datetime
from typing import Any, Dict, List, Optional

from ..writer import LogWriter
from .types import CommitLog, Entity


class ContainerLister:
    def on_end(self):
        pass


BaseConfig = Dict[str, Any]


class BaseContainer:
    entity: Entity
    _id: str
    _name: Optional[str]
    span_id: Optional[str]
    start_timestamp: datetime
    end_timestamp: Optional[datetime] = None
    tags: Dict[str, str] = field(default_factory=dict)
    writer: LogWriter
    listeners: List[ContainerLister]

    def __init__(self, entity: Entity, config: BaseConfig, writer: LogWriter):
        self.entity = entity
        self._id = config['id']
        self._name = config.get('name')
        self.span_id = config.get('span_id')
        self.start_timestamp = datetime.now()
        self.tags = config.get('tags', {})
        self.writer = writer
        self.listeners = []

    @property
    def id(self) -> str:
        return self._id

    def add_listener(self, listener: ContainerLister):
        self.listeners.append(listener)

    def add_tag(self, key: str, value: str):
        if self.tags == None:
            self.tags = {}
        self.tags[key] = value
        self.commit("update", {"tags": {key: value}})

    def end(self):
        self.end_timestamp = datetime.now()
        self.commit("end", {"endTimestamp": self.end_timestamp})
        for listener in self.listeners:
            listener.on_end()
        self.listeners = []

    def data(self) -> Dict[str, Any]:
        return {
            "name": self._name,
            "spanId": self.span_id,
            "tags": self.tags,
            "startTimestamp": self.start_timestamp,
            "endTimestamp": self.end_timestamp,
        }

    def commit(self, action: str, data: Optional[Dict[str, Any]] = None):
        if data is None:
            data = self.data()
        # Removing all null values from data dict
        data = {k: v for k, v in data.items() if v is not None}
        self.writer.commit(CommitLog(self.entity, self._id,
                           action, data))


class EventEmittingBaseContainer(BaseContainer):
    def event(self, id: str, name: str, tags: Optional[Dict[str, str]] = None):
        self.commit("add-event", {"id": id, "name": name,
                    "timestamp": datetime.now(), "tags": tags})
