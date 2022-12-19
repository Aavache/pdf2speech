import os
import argparse
from lib.reader import get_reader
from lib.vocoder import get_vocoder


def main(args):
    """ Here the starting function of the
    software

    Parameters
    ----------
    args: arguments
        CLI parameters
    """
    reader = get_reader(args.fpath)
    text = reader.read_all()

    vocoder = get_vocoder(args.lang)
    out_fpath = vocoder(text, args.outdir)

    assert os.path.exists(out_fpath)
    print(f" The cue was succesfully generated at {out_fpath}")


if __name__ == "__main__":
    # Defining the arguments to module
    parser = argparse.ArgumentParser()
    parser.add_argument("--fpath", type=str, default=None, required=True,
                    help='File to be read.')
    parser.add_argument("--outdir", type=str, default=None, required=True,
                    help='Directory to store audio file')
    parser.add_argument("--lang", type=str, default='eng', help='Language.')
    args, unknowns = parser.parse_known_args()

    main(args)
