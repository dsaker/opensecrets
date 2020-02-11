#!/usr/bin/python3

import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    insert = ''
    delete = ''

    try:
        opts, args = getopt.getopt(argv,"hi:o:n:d:",["ifile=","ofile=","insert=","delete="])
    except getopt.GetoptError:
        print('ReplaceText.py -i <inputfile> -o <outputfile> -n <insert> -d <delete>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('ReplaceText.py -i <inputfile> -o <outputfile> -n <insert> -d <delete>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-n", "--insert"):
            insert = arg
        elif opt in ("-d", "--delete"):
            delete = arg
    
    with open(inputfile, 'r') as file :
        filedata = file.read()

    filedata = filedata.replace(delete, insert)

    with open(outputfile, 'w') as file:
        file.write(filedata)

    print('Input file is "', inputfile)
    print('Output file is "', outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])