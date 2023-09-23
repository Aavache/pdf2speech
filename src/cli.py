import os
import click

from .lib.reader import get_reader
from .lib.vocoder import get_vocoder


@click.command()
@click.argument('text-path', type=str, nargs=1)
@click.argument('output-dir', type=str, nargs=1)
@click.option('-fp', '--from_page', help='From which page to start', 
              type=int, default=0)
@click.option('-v', '--vocoder', help='Vocoder name', 
             type=click.Choice(['gtts']), default='gtts', show_default=True)
@click.option('-w', '--words-per-track', help='Number of words per track', type=int,
              default=500, show_default=True)
@click.option('-l', '--language', help='Language', type=str, default='en', show_default=True)
def cli(text_path, output_dir, from_page, vocoder, words_per_track, language):
    """Convert a text file into speech audio"""
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Defining the output filename
    text_fname = os.path.basename(text_path).split(".")[0]

    # Reading the written file
    click.echo(f"Reading file `{text_path}`...")
    reader = get_reader(text_path)
    doc = reader.read_all(text_path, from_page)

    click.echo(f"Done reading, turn to create the audio at `{output_dir}`...")
    # Generating the audio and export
    vocoder = get_vocoder(vocoder, output_dir, language, words_per_track, text_fname)
    vocoder(doc)

    click.echo(f"All the files were succesfully generated \n")

if __name__ == '__main__':
    cli("../input_examples/lorem_ipsum.pdf", "tmp/", 
        from_page=0, 
        vocoder="gtts", 
        words_per_track=500, 
        language="en"
    )
