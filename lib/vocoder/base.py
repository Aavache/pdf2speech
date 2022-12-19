from abc import ABC, abstractmethod
import os


class BaseVocoder(ABC):
    """
    """
    def __init__(self, fpath):
        self.fname = fpath
        self.fname = os.basename(fpath)
     