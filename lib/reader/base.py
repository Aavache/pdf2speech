from abc import ABC, abstractmethod
import os


class BaseReader(ABC):
    """
    """
    def __init__(self, fpath):
        self.fname = fpath
        self.fname = os.basename(fpath)
    
    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def get_page_number(self):
        pass