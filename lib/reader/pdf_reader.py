from .base import BaseReader
import PyPDF2
from lib.text import DocObj


class PdfReader(BaseReader):
    """
    This class is responsible for parsing pdf files

    Parameters
    ----------
    fpath: str
        Path to the files to be read
    """
    def __init__(self, fpath):
        super(PdfReader, self).__init__(fpath)
    
    def read_all(self):
        """ Reading the entire document"""
        doc = DocObj()
        print(f"Reading document `{self.fpath}...\n")
        with open(self.fpath, 'rb') as f:
            pdfReader = PyPDF2.PdfReader(f)
            for page_id in range(len(pdfReader.pages)):
                raw_text = pdfReader.pages[page_id].extract_text()
                raw_text = raw_text.replace("\n", " ")
                raw_text = raw_text.replace("\t", " ")
                doc.insert_page(raw_text)

        return doc

    def get_page_number(self):
        pass
