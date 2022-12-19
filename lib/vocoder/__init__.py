from .gtts_voc import GTTSVoc


def get_vocoder(
        voc_name: str,
        lang: str
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

    Returns
    -------
    obj
        vocoder initialized  
    """

    # Init vocoder
    if voc_name == "gtts": 
        return GTTSVoc(lang)
    else:
        raise ValueError(f" The vocoder with name {voc_name} is not supported")
    