import os


def get_reader(fpath: str, *args, **kwargs):
    """Given the file, this function returns the appropiate file reader.

    Returns
    -------
    obj
        reader object initialized
    """
    fname = os.path.basename(fpath)

    # Getting the extensions
    fname_arr = fname.split(".")
    assert len(fname_arr) == 2, f"The file name {fname} must " "have an extension"

    ext = fname_arr[1].lower()

    if ext == "pdf":
        from .pdf_reader import PdfReader

        return PdfReader(fpath, *args, **kwargs)
    elif ext == "txt":
        from .txt_reader import TxtReader

        return TxtReader(fpath, *args, **kwargs)
    else:
        raise ValueError(f" Extension {ext} is not supported")
