from abc import ABC, abstractmethod
import os


class BaseReader(ABC):
    """
    Abstract class for reading documents
    """
    def __init__(self, fpath):
        self.fpath = fpath
        self.fname = os.path.basename(fpath)

    @abstractmethod
    def read_all(self):
        """ Reading the entire document"""
        pass