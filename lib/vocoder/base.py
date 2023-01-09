from abc import ABC, abstractmethod


class BaseVoc(ABC):
    """
    Base Class vocoder
    """
    def __init__(self, max_words):
        self.max_words = max_words

    @abstractmethod
    def generate_audio(self, text, fpath):
        pass

    def __call__(self, doc, outfpath):
        # Separate audio tracks
        tracks_text = ["",]
        cur_word_count = 0
        for page_id in range(len(doc)): 
            page_text = doc.get_page(page_id)
            page_text_split = page_text.split(" ")
            page_word_count = len(page_text_split)
            if cur_word_count + page_word_count > self.max_words:
                allowed_word_count = self.max_words - cur_word_count
                tracks_text[len(tracks_text)-1] += " " + \
                    " ".join(page_text_split[:allowed_word_count])

                tracks_text.append(" ".join(page_text_split[allowed_word_count:]))
                cur_word_count = len(page_text_split) - allowed_word_count
            else:
                tracks_text[len(tracks_text)-1] += " " + page_text
                cur_word_count += page_word_count

        # Generate audio samples
        for i, text in enumerate(tracks_text):
            fpath = outfpath + f"-{i}"
            print(f"Generating audio track {i}: `{fpath}`...")
            self.generate_audio(text, fpath)
