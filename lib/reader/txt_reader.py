from .base import BaseReader


class TxtReader(BaseReader):
    """
    This class is responsible for parsing pdf files
    """
    def __init__(self, fpath):
        super(self, TxtReader).__init__(fpath)
    
    def read_all(self):
        pass

    def get_page_number(self):
        pass