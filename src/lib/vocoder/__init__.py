def get_vocoder(voc_name: str, *args, **kwargs) -> object:
    """Returns a vocoder to generate the audio file returns the appropiate file reader.

    Parameters
    ----------
    voc_name: str
        Name of the vocoder

    Returns
    -------
    obj
        vocoder initialized
    """

    # Init vocoder
    if voc_name == "gtts":
        from .gtts_voc import GTTSVocoder

        return GTTSVocoder(*args, **kwargs)
    else:
        raise ValueError(f" The vocoder with name {voc_name} is not supported")
