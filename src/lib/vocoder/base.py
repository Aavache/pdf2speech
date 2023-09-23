import math
from abc import ABC, abstractmethod

import click

from ..text import DocObj


class BaseVocoder(ABC):
    """Base class vocoder.

    Parameters
    ----------
    output_dir: str
        Path of the output directory to be generated tracks
    lang: str
        language
    words_per_track: int
        Maximum number of words per track
    """

    def __init__(self, output_dir, lang, words_per_track, text_name, *args, **kwargs):
        self.output_dir = output_dir
        self.max_words = words_per_track
        self.lang = lang
        self.text_name = text_name

    @property
    @abstractmethod
    def vocoder_name(self):
        raise NotImplementedError

    @abstractmethod
    def generate_audio(self, text: str, track_id: int):
        """Generate the audio file from the text."""
        raise NotImplementedError

    def __call__(self, doc: DocObj):
        # Separate audio tracks
        tracks_text = [
            "",
        ]
        cur_word_count = 0

        for page_id in range(len(doc)):
            page_text = doc.get_page(page_id)
            page_text_split = page_text.split(" ")
            page_word_count = len(page_text_split)

            if cur_word_count + page_word_count > self.max_words:
                allowed_word_count = self.max_words - cur_word_count
                tracks_text[-1] += " " + " ".join(page_text_split[:allowed_word_count])

                page_text_split = page_text_split[allowed_word_count:]
                page_word_count = len(page_text_split)

                for i in range(math.ceil(page_word_count / self.max_words)):
                    tracks_text.append(" ".join(page_text_split[i * self.max_words : (i + 1) * self.max_words]))

                cur_word_count = len(tracks_text[-1].split(" "))
            else:
                tracks_text[-1] += " " + page_text
                cur_word_count += page_word_count

        # Generate audio samples
        for i, text in enumerate(tracks_text):
            click.echo(f"Generating audio track #{i}...")
            self.generate_audio(text, i)
