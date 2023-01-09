def get_vocoder(
        voc_name: str,
        lang: str,
        max_words: int
    ):
    """ Returns a vocoder to generate
    the audio file
    returns the appropiate file reader 
    
    Parameters
    ----------
    voc_name: str
        Name of the vocoder
    lang: str
        Language
    max_words: int
        Maximum number of words per track

    Returns
    -------
    obj
        vocoder initialized  
    """

    # Init vocoder
    if voc_name == "gtts": 
        from .gtts_voc import GTTSVoc
        return GTTSVoc(lang, max_words)
    else:
        raise ValueError(f" The vocoder with name {voc_name} is not supported")
    