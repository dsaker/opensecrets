#!/usr/bin/python3

import argparse, sys

def main(argv):
    parser = argparse.ArgumentParser()  
    parser.add_argument('inputfile', help="the input file")
    parser.add_argument('outputfile', help="the output file")
    parser.add_argument('delete', help="the text to be replaced")
    parser.add_argument('insert', help="the text to be inserted")
    args = parser.parse_args()

    with open(args.inputfile, 'r') as file :
        filedata = file.read()

    filedata = filedata.replace(args.delete, args.insert)

    with open(args.outputfile, 'w') as file:
        file.write(filedata)

    print('Input file is "', args.inputfile)
    print('Output file is "', args.outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])