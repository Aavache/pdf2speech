from ..text import DocObj
from .base import BaseReader


class TxtReader(BaseReader):
    """This class is responsible for parsing pdf files.

    Returns
    -------
    obj
        reader object initialized
    """

    def read_all(self, fpath, *args, **kwargs) -> DocObj:
        """Reading a txt file."""
        with open(fpath, "r") as f:
            raw_text = f.read()
            raw_text.replace("\n", "")

        doc = DocObj()
        doc.insert_page(raw_text)  # all in a single page

        return doc
