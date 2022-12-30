import os
from .base import BaseVoc
from gtts import gTTS

EXTENSION = ".mp3"
AVAILABLE_LANG = ("en")


class GTTSVoc(BaseVoc):
    """
    This class is responsible converting text
    to speech

    Parameters
    ----------
    outfpath: str
        Path of the output files to be generated,
        without including the extension
    lang: str
        language
    """
    def __init__(self, lang):
        super(GTTSVoc, self).__init__()
        assert lang in AVAILABLE_LANG, f"{lang} is not an available languages." \
            f" Here the list of all languages: {AVAILABLE_LANG}"
        self.lang = lang
        self.slow = False

    def __call__(self, doc, outfpath):
        aud_obj = gTTS(text=doc.get_all_text(), lang=self.lang, slow=self.slow)
        fpath = outfpath + EXTENSION
        aud_obj.save(fpath)
        assert os.path.exists(fpath)

        return fpath

