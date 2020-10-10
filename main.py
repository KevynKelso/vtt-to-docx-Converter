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
        make_document(vtt_file, title)
        successPrint('Done.')

if __name__ == '__main__':
    main()

