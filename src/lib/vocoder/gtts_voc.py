import os
from .base import BaseVoc
from gtts import gTTS

EXTENSION = ".mp3"
AVAILABLE_LANG = ("en", "es")


class GTTSVoc(BaseVoc):
    """
    This class is responsible converting text
    to speech using the GTTS vocoder

    Parameters
    ----------
    outfpath: str
        Path of the output files to be generated,
        without including the extension
    lang: str
        language
    max_words: int
        Maximum number of words per track
    """
    def __init__(self, lang, max_words):
        super(GTTSVoc, self).__init__(max_words)
        assert lang in AVAILABLE_LANG, f"{lang} is not an available languages." \
            f" Here the list of all languages: {AVAILABLE_LANG}"
        self.lang = lang
        self.slow = False

    def generate_audio(self, text, fpath):
        aud_obj = gTTS(text=text, lang=self.lang, slow=self.slow)
        fpath = fpath + EXTENSION
        aud_obj.save(fpath)
        assert os.path.exists(fpath)
        