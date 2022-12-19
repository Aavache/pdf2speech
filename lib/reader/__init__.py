import os
from .pdf_reader import PdfReader
from .txt_reader import TxtReader


def get_reader(fpath: str):
    """ Given the file, this function
    returns the appropiate file reader 
    
    Parameters
    ----------
    fpath: str
        The path to the file to be read

    Returns
    -------
    obj
        reader object initialized
    """
    fname = os.basename(fpath)

    # Getting the extensions
    fname_arr = fname.split(".")
    assert len(fname_arr) == 2, f"The file name {fname} must "\
            "have an extension"

    ext = fname[1].lower()

    if ext == "pdf": 
        return PdfReader(fpath)
    elif ext == "txt":
        return TxtReader(fpath)
    else:
        raise ValueError(f" Extension {ext} is not supported")