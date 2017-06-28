#!/usr/bin/env python3

import csv

def main():
    from argparse import ArgumentParser

    # Create a command line argument parser
    parser = ArgumentParser()

    # Add arguments to the parser
    parser.add_argument("csvfile1", help="CSV file 1")
    parser.add_argument("csvfile2", help="CSV file 2")

    # Parse the command line arguments
    args = parser.parse_args()

    # Open both CSV files
    with open(args.csvfile1, 'r', newline='') as CSV1, open(args.csvfile2, 'r', newline='') as CSV2:
        namesWords1 = list(csv.reader(CSV1))
        namesWords2 = list(csv.reader(CSV2))

    print()

    # If the names/words/counts match
    if(namesWords1 == namesWords2):
        print("{} and {} match perfectly!".format(args.csvfile1, args.csvfile2))
    # Otherwise, they don't match
    else:
        print("{} and {} do not match!".format(args.csvfile1, args.csvfile2))

    print()

    exit(0)

if(__name__ == "__main__"):
    main()
