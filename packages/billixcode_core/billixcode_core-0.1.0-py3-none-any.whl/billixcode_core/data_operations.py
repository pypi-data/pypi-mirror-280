from abc import ABC, abstractmethod


class AbstractDataOperations(ABC):

    @abstractmethod
    def upsert(self):
        pass
