# pdf2speech: generate audio tracks from text 📄 ➡️ 🔊

Reading PDF files and converting them to audible cues. Feed your favorite books and rest you eyesight while going back home after a hard day of work and reading documents on the computer screen.

## Install

```sh
git clone https://github.com/Aavache/pdf2speech.git
cd pdf2speech
pip install .
```

## How to use the tool

Ask for help to the terminal and insert the requested arguments:

```sh
p2s --help

>>>
Usage: p2s [OPTIONS] TEXT_PATH OUTPUT_DIR

  Convert a text file into speech audio

Options:
  -fp, --from_page INTEGER       From which page to start
  -v, --vocoder [gtts]           Vocooder name  [default: gtts]
  -w, --words-per-track INTEGER  Number of pages per track  [default: 500]
  -l, --language TEXT            Language  [default: en]
  --help                         Show this message and exit.
```

Take a look to the examples in `input_examples` and the corresponding generated audios tracks `outputs`.

## Reference

The code is generic to any text to speech vocoder, however at the moment only the google-based synthesize is available, i.e. [gTTs](https://pypi.org/project/gTTS/).

## Future work

* Support state-of-the-art TTS methods.
* Supporting more text formats, at the moment `pdf` and `txt` are allowed.
