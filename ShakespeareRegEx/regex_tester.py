#!/usr/bin/env python3

import argparse
import re

def main():
    parser = argparse.ArgumentParser(description='Open .txt files')
    parser.add_argument('-r', '--readFile', metavar='FILE', type=str, nargs=1,
                        help='One .txt file to be opened and word counted')

    args = parser.parse_args()

    with open(args.readFile[0]) as READ_FILE:
        for line in READ_FILE:
            if re.search("^\n", line) == None:
                print ("You used re.search == None, I hope you wanted that! You should hae found a non-empty line!")
                if re.search("^\s+", line) == None:
                    print ("You successfully found a character name.")
                    print (line)
                else:
                    print ("You successfully found a block of text.")
                    print(line)


if (__name__ == "__main__"):
    main()