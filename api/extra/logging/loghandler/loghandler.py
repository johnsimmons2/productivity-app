from abc import abstractmethod
from extra.logging.log import Log


class LogHandler:
    @abstractmethod
    def handle(self, log:Log):
        pass