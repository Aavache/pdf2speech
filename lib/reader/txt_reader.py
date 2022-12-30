from .base import BaseReader
from lib.text import DocObj


class TxtReader(BaseReader):
    """
    This class is responsible for parsing pdf files

    Parameters
    ----------
    fpath: str
        Path to the files to be read
    """
    def __init__(self, fpath):
        super(TxtReader, self).__init__(fpath)
    
    def read_all(self):
        """ Reading the entire file"""
        with open(self.fpath, 'r') as f:
            raw_text = f.read() 
            raw_text.replace("\n", "")

        doc = DocObj()
        doc.insert_page(raw_text)

        return doc