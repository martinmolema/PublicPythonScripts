#!/usr/bin/python3

# Example usage: draw-io-export.py --scale=2 --format=PNG --output-directory=afbeeldingen -t Diagrams.drawio

import os
import xml.etree.ElementTree as ET
import getopt, sys

# options
options = "hb:s:f:d:t"
long_options = ["help", "basename =", "scale=","format=", "output-directory=", "transparent"]

def Usage():
    print("Usage:")
    print("draw-io-export [-b basename | --basename basename] [-h|--help] [-f format | --format] [-s scale | --scale scale] [-t | --transparent] filename")
    print ("-h | --help\n display this help ")
    print ("-b | --basename\n the base of the filename to which the pagename is added")
    print ("-s | --scale\n scale the image; value must be an number; 1=100%, 2=200% etc.")
    print ("-f | --format supported export types by drawIO. e.g. PNG or JPG")
    print ("-d | --output-directory the directory where exported files are placed")
    print ("-t | --transparent the directory where exported files are placed")

# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]

basename = ""
inputFullPath = ""
format = "PNG"
scale = "1"
directory = "./"
transparent = False

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)

    if (len(values) != 0 ):
        inputFullPath = values[0]
        # set the basename default to the same name as the filename without the extension

        filename = os.path.basename(inputFullPath)
        basename = os.path.splitext(filename)[0]

    else:
        print("No filename found")
        Usage()
        exit(1)

    # checking each argument
    for currentArgument, currentValue in arguments:

        if currentArgument in ("-h", "--Help"):
            Usage()
            exit(0)

        elif currentArgument in ("-b", "--basename"):
            basename = currentValue

        elif currentArgument in ("-s", "--scale"):
            scale = currentValue

        elif currentArgument in ("-f", "--format"):
            format = currentValue

        elif currentArgument in ("-d", "--output-directory"):
            directory = currentValue

        elif currentArgument in ("-t", "--transparent"):
            transparent = True


except getopt.error as err:
    # output error, and return with an error code
    print(str(err))

print(("Using input file %s") % (inputFullPath))
print(("Using output base filename %s") % (basename))
print(("Sending result files to directory %s") % (directory))

root = ET.parse(inputFullPath).getroot()
for diagram in root.findall('diagram'):

    # get the name-attribute of the diagram element
    pagename = diagram.get('name')
    print("Processing " + pagename)

    # construct a new filename
    newfilename = directory + "/" + basename + ' - ' + pagename + '.png'


    # construct a command line. assume that drawio can be run using the path-variable
    commandline = "drawio -x -o '" + newfilename + "' -f " + format + " -s " + scale
    if transparent:
        commandline += " -t"

    # add the filename as the last parameter
    commandline = commandline + " " + inputFullPath

    # print (commandline)
    result = os.system(commandline)
    if result != 0:
        print ("#Error running command line")