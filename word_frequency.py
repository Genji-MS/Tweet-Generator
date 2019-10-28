# word_frequency.py
import os
import sys
import string, re

#parsed_text = []
#histogram_words = []
#histogram_frequency = []

def parseFile(document):
    """convert text file into a string of every word, removing all punctuation and converting to lower case"""
    #global parsed_text
    f = open(os.path.join(sys.path[0],document)).read().split()

    unwanted_punctuation_table = dict.fromkeys(map(ord, '\n\r“”",.…!?'), None)
    parsed_text = [line.translate(str.maketrans(unwanted_punctuation_table)).lower() for line in f]
    #print ( len(parsed_text))
    #wordcount(parsed_text)
    
    return parsed_text

def wordcount(histogram):
    """seperate into unique words and count them ALL up"""
    #global histogram_words, histogram_frequency
    histogram_words = []
    histogram_frequency = []

    for word in histogram:
        if word not in histogram_words:
            histogram_words.append(word)
            histogram_frequency.append(1)
        else:
            i= histogram_words.index(word)
            histogram_frequency[i] += 1
    #print( len(histogram_words))
    #print( len(histogram_frequency))
    #print(histogram_words)

def unique_words(histogram):
    """take in a histogram and return the number of words overall"""
    histogram_words = []
    for word in histogram:
        if word not in histogram_words:
            histogram_words.append(word)
    
    return ( len(histogram_words) )

def frequency(match_word,histogram):
    """take a specific word and return how many times it occurs"""
    histogram_frequency = 0
    for word in histogram:
        if word == match_word:
            histogram_frequency += 1

    return ( histogram_frequency )

if __name__ == "__main__":
    histogram = parseFile('MonsterUnderTheBed')
    print (f'total words: { len(histogram)}')
    print (f'total of unique words: {unique_words(histogram)}')
    print (f'total occurances of the word "monster" :{frequency("monster",histogram)}')