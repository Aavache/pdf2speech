import os
import time

from gtts import gTTS

from ..utils.constants import TRACK_NANE_TEMPLATE
from .base import BaseVocoder

EXTENSION = "mp3"
AVAILABLE_LANG = ("en", "es")


class GTTSVocoder(BaseVocoder):
    """This class is responsible converting text to speech using the GTTS vocoder.

    Parameters
    ----------
    out_dir: str
        Path of the output directory to be generated tracks
    lang: str
        language
    words_per_track: int
        Maximum number of words per track
    """

    def __init__(self, *wargs, **kwargs):
        super(GTTSVocoder, self).__init__(*wargs, **kwargs)

        assert self.lang in AVAILABLE_LANG, (
            f"{self.lang} is not an available languages." f" Here the list of all languages: {AVAILABLE_LANG}"
        )
        self.slow = False

    @property
    def vocoder_name(self):
        return "gtts"

    def generate_audio(self, text: str, track_id: int):
        aud_obj = gTTS(text=text, lang=self.lang, slow=self.slow)

        file_name = TRACK_NANE_TEMPLATE.format(
            time_stamp=time.strftime("%Y%m%d-%H%M%S"),
            text_fname=self.text_name,
            track_id=str(track_id),
            vocoder=self.vocoder_name,
            ext=EXTENSION,
        )

        track_path = os.path.join(self.output_dir, file_name)

        aud_obj.save(track_path)

        if not os.path.exists(track_path):
            raise FileExistsError(f" The file {track_path} was not generated correctly")
