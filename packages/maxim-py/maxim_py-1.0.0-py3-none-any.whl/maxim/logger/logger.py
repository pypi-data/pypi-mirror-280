# Assuming similar components exist in Python with the same functionality
from ..logger.components.session import Session, SessionConfig
from ..logger.components.trace import Trace, TraceConfig
from .writer import LogWriter, LogWriterConfig


class LoggerConfig:
    def __init__(self, id, auto_flush=False, flush_interval=None):
        self.id = id        
        self.auto_flush = auto_flush
        self.flush_interval = flush_interval

class Logger:
    def __init__(self, config : LoggerConfig, api_key, base_url, is_debug=False):
        if not config.id:
            raise ValueError("Logger must be initialized with id of the logger")
        self._id = config.id
        self.is_debug = is_debug
        writer_config = LogWriterConfig(auto_flush=config.auto_flush,
                                flush_interval=config.flush_interval,
                                base_url=base_url,
                                api_key=api_key,
                                repository_id=config.id)
        self.writer = LogWriter(writer_config)
        self.sessions = {}
        self.traces = {}

    def session(self, config: SessionConfig) -> Session:
        session = self.sessions.get(config.id)
        if session is None:
            session = Session(config, self.writer)
            self.sessions[config.id] = session
        return session

    def trace(self, config: TraceConfig) -> Trace:
        trace = self.traces.get(config.id)
        if trace is None:
            trace = Trace(config, self.writer)
            self.traces[config.id] = trace
        return trace

    @property
    def id(self):
        return self._id

    def cleanup(self):
        # Ending all traces and sessions
        for trace in self.traces.values():
            trace.end()
        for session in self.sessions.values():
            session.end()
        # Cleaning all traces and sessions
        self.sessions = {}
        self.traces = {}
        self.writer.flush()
        self.writer.cleanup()