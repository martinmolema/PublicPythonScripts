# Draw IO Image exporter
This simple Python3 converter enables you to export all pages ('tabs') in your
DrawIO file to (e.g.) PNG-images.

The script uses the GetOpts library to parse parameters. When run without any parameter
a usage is displayed like below:
```bash
Usage:
draw-io-export.py [ -h | --help ] [ -b basename| --basename basename] [ -s scale| --scale scale] [ -f format| --format format] [ -d path| --output-directory path] [ -t | --transparent ]  filename

-h | --help
     display this help
-b | --basename
     the base of the filename to which the pagename is added
-s | --scale
     scale the image; value must be an number; 1=100%, 2=200% etc.
-f | --format
     supported export types by drawIO. e.g. PNG or JPG
-d | --output-directory
     the directory where exported files are placed
-t | --transparent
     background of the exported image is made transparent

 ```
## Example
Example Usage :
draw-io-export.py --scale=2 --format=PNG --output-directory=afbeeldingen -t Diagrams.drawio

An example file is present in this repository for testing