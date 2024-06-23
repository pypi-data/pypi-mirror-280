from abc import abstractmethod, ABC


class AbstractMessageProducer(ABC):
    @abstractmethod
    def emit(self, event):
        pass
