from .base import BaseVoc


class GTTSVoc(BaseVoc):
    """
    This class is responsible converting text
    to speech
    """
    def __init__(self, fpath):
        super(self, GTTSVoc).__init__(fpath)

    def __call__(self, text, out_dir):
        pass
