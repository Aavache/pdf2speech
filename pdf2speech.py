import os
import time
import argparse
from lib.reader import get_reader
from lib.vocoder import get_vocoder
from lib.utils.constants import MAX_WORDS

OUTPUT_PATH = "./outputs/"


def main(args):
    """ Here the starting function of the
    software

    Parameters
    ----------
    args: arguments
        CLI parameters
    """
    # Create output directory
    os.makedirs(args.outdir, exist_ok=True)

    # Defining the output filename
    time_stamp = time.strftime("%Y%m%d-%H%M%S")
    fname = os.path.basename(args.fpath).split(".")[0]
    outfpath = os.path.join(args.outdir, time_stamp + "-" + fname)

    # Reading the written file
    reader = get_reader(args.fpath)
    doc = reader.read_all()

    # Generating the audio and export
    vocoder = get_vocoder(args.voc, args.lang, args.max_words)
    vocoder(doc, outfpath)

    print(f" The audio track/s were succesfully generated at {args.outdir}")


if __name__ == "__main__":
    # Defining the arguments to module
    parser = argparse.ArgumentParser()
    parser.add_argument("fpath", type=str, help='File to be read.')
    parser.add_argument("outdir", type=str, help='Directory to store audio file')
    parser.add_argument("-l", "--lang", type=str, default='en', help='Language.')
    parser.add_argument("--voc", type=str, default='gtts', help='Vocoder name.')
    parser.add_argument("--max-words", type=int, default=MAX_WORDS, help='Number of words per track')
    args, unknowns = parser.parse_known_args()

    main(args)
