import os
import tempfile
import threading
import time
import uuid
from queue import Queue
from typing import Union

from ..apis.maxim import MaximAPI


class LogWriterConfig:
    def __init__(self, base_url, api_key, repository_id, auto_flush=False, flush_interval:Union[int,None]=10, is_debug=False):
        self.base_url = base_url
        self.api_key = api_key
        self.repository_id = repository_id
        self.auto_flush = auto_flush
        self.flush_interval = flush_interval
        self.is_debug = is_debug

class LogWriter:
    def __init__(self, config: LogWriterConfig):
        self.id = str(uuid.uuid4())
        self.config = config
        self.queue = Queue()
        self.mutex = threading.Lock()
        self.is_debug = config.is_debug
        self.logs_dir = os.path.join(tempfile.gettempdir(), f"maxim-sdk/{self.id}/maxim-logs")
        self.__flush_thread = None
        os.makedirs(self.logs_dir, exist_ok=True)
        if self.config.auto_flush:
            if self.config.flush_interval:
                self.__flush_thread = threading.Timer(int(self.config.flush_interval), self.flush)
                self.__flush_thread.start()
            else:
                raise ValueError("flush_interval is set to None.flush_interval has to be a number")

    def write_to_file(self, logs):
        filename = f"logs-{time.strftime('%Y-%m-%dT%H:%M:%SZ')}.log"
        filepath = os.path.join(self.logs_dir, filename)
        if self.is_debug:
            print(f"Writing logs to file: {filename}")
        with open(filepath, 'w') as file:
            for log in logs:
                file.write(log.serialize() + "\n")
        return filepath

    def flush_log_files(self):
        if os.path.exists(self.logs_dir) == False:
            return
        files = os.listdir(self.logs_dir)
        for file in files:
            with open(os.path.join(self.logs_dir, file), 'r') as f:
                logs = f.read()
            try:
                MaximAPI.pushLogs(self.config.base_url, self.config.api_key, self.config.repository_id, logs)
                os.remove(os.path.join(self.logs_dir, file))
            except Exception as e:
                if self.is_debug:
                    raise Exception(e)
    
    def flush_logs(self, logs):
        try:
            # Pushing old logs first
            self.flush_log_files()
            # Pushing new logs
            logs_to_push = "\n".join([log.serialize() for log in logs])
            MaximAPI.pushLogs(self.config.base_url, self.config.api_key, self.config.repository_id, logs_to_push)
        except Exception as e:
            self.write_to_file(logs)                            

    def commit(self, log):
        self.queue.put(log)

    def flush(self):
        with self.mutex:
            items = []
            while not self.queue.empty():
                items.append(self.queue.get())
            if len(items) == 0:
                if self.is_debug:
                    print("[MaximSDK] No logs to flush")
                return
            if self.is_debug:
                print("[MaximSDK] Flushing logs to server")
        self.flush_logs(items)
        if self.is_debug:
            print("[MaximSDK] Flush complete")

    def cleanup(self):
        if self.config.flush_interval and self.__flush_thread:
            self.__flush_thread.cancel()
        self.flush()

