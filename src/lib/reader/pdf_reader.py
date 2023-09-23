import PyPDF2

from ..text import DocObj
from .base import BaseReader


class PdfReader(BaseReader):
    """This class is responsible for parsing pdf files.

    Parameters
    ----------
    fpath: str
        Path to the file to be read
    from_page: str
        From page to start reading
    """

    def read_all(self, fpath: str, from_page: int = 0, *args, **kwargs) -> DocObj:
        """Reading the entire document."""
        doc = DocObj()
        print(f"Reading document `{fpath}`...\n")
        with open(fpath, "rb") as f:
            pdfReader = PyPDF2.PdfReader(f)
            for page_id in range(len(pdfReader.pages)):
                if from_page > page_id:
                    continue
                raw_text = pdfReader.pages[page_id].extract_text()
                raw_text = raw_text.replace("\n", " ")
                raw_text = raw_text.replace("\t", " ")
                doc.insert_page(raw_text)

        return doc
