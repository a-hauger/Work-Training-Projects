#!/usr/bin/env python3

import argparse
import re

def removeSentencePunc(line):
    line = re.sub("[,.?;:!\"]|\[|\]", "", line) #remove sentence punctuations
    line = re.sub("--", " ", line) #removes all instances of double hyphens
    line = re.sub("[']([\w']+[-]?[\w']*)[']", r'\1', line) #removes instances of 'word' words
    line = line.lower() #allows for correct alphabetizing later
    return line

def characterDictionaryCreator(character, dictionary):
    if character not in dictionary:
        dictionary[character] = {}
    return dictionary

def wordCounter(block, dictionary, character):
    block = removeSentencePunc(block) #send dialogue to have punc removed
    for word in block.split():
        if word not in dictionary[character]:
            dictionary[character][word] = 1
        else:
            dictionary[character][word] += 1
    return dictionary

def dictionarySorter(dictionary):
    characterNameSort = sorted(dictionary)
    totalNumWords = 0
    for characterName in characterNameSort: #sort the character names
        totalCharWords = 0
        wordList = dictionary[characterName]
        sortedWordList = sorted(wordList)
        print (str(characterName) + ":")
        for word in sortedWordList: #sort the words spoken by the character
            totalCharWords += dictionary[characterName][word]
            totalNumWords += dictionary[characterName][word]
            print("\t" + str(word) + ": " + str(dictionary[characterName][word]) + "\n")
        print ("The total number of words spoken by this character is:\n\t" + str(totalCharWords))
    print("The total number of words spoken by all characters are:\n\t" + str(totalNumWords))
    return

def writeToCSV(dictionary):
    with open("word_count.csv", mode = 'w') as WRITE_FILE:
        characterNameSort = sorted(dictionary)
        for characterName in characterNameSort:
            wordList = dictionary[characterName]
            sortedWordList = sorted(wordList)
            for word in sortedWordList:
                WRITE_FILE.write("{0},{1},{2}\n".format(characterName, word, dictionary[characterName][word]))
    WRITE_FILE.close()
    return


def main():
    parser = argparse.ArgumentParser(description='Open .txt files')
    parser.add_argument('-r', '--readFile', metavar='FILE', type=str, nargs=1, help='One .txt file to be opened and word counted')

    args = parser.parse_args()

    with open(args.readFile[0]) as READ_FILE: #open file
        character_dict = {}
        characterName = ""

        for i, line in enumerate(READ_FILE):
            if i<4:
                continue
            if re.search("^\n", line) == None: #non-empty line
                if re.search("^\s+", line) == None: #the line is a character
                    index = len(line)-1
                    characterName = line[:index].lower()
                    character_dict = characterDictionaryCreator(characterName, character_dict)
                else: #block of dialogue
                    character_dict = wordCounter(line, character_dict, characterName)

        dictionarySorter(character_dict)
        writeToCSV(character_dict)

    READ_FILE.close()

    return

if(__name__== "__main__"):
    main()