from abc import ABC, abstractmethod


class BaseReader(ABC):
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def read_all(self):
        """Reading document."""
        raise NotADirectoryError("This method must be implemented")
