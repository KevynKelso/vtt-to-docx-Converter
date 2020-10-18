import click

from utils.functions import make_document
from utils.functions import get_vtt_files
from utils.utils_print import (
    failPrint,
    successPrint,
    warningPrint
)

def main():
    vtt_files = get_vtt_files('./input')

    for vtt_file in vtt_files:
        vtt_name = vtt_file[8:]
        warningPrint(f'Processing {vtt_name} . . .')
        title = click.prompt('Video Title', default='Unknown')
        warningPrint(
                '''Leave this option as default (1) if there are multiple 
                speakers in video'''
        )
        sentence_count = click.prompt(
                'How many sentences to combine each row by?', default=1)
        make_document(vtt_file, title, sentence_count)
        successPrint('Done.')

if __name__ == '__main__':
    main()

