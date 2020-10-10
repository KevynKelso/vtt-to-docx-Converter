# vtt to docx Converter

## Setup

Run `chmod u+x ./main.py` to enable user permission to run the script
as an executable.

Run `pipenv shell` to enter vitual environment.

Run `pipenv install` to install necessary packages.

## Usage

Copy .vtt files into the `./input` directory. To run the VTT conversion, run
`python main.py` from the command line. The vtt files will be processed and
you will be asked for the video title for each file. This is because that
information is not contained in the .vtt file and is needed for documentation
purposes. Finished .docx files will show up in the `./ouput` directory
with the same file name and the `.docx` extension.

### Example

```
$: python main.py
Processing VTT timing transcript_Stella_FW_Belcastro_L1_C2.vtt . . .
Video Title [Unknown]: Zach’s Story
Done.
```

This example will output one docx file into `./output`.

