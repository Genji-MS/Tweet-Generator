#dictionary_words.py
import random
import sys

words_list = ""

def load_words_file():
    """parse the 'words' file from MAC OS X"""
    global words_list
    f = open('/usr/share/dict/words', 'r')
    words_list = f.readlines()
    f.close()

def fetch_random_words(params):
    """grab a specified command line number of random words from our 'words' file and return them as a string"""
    length = int(params)
    output = ""
    while length > 0:
        rng = random.randint(0,len(words_list)-1)
        output += words_list[rng].rstrip('\r\n') + " "
        length -= 1
    return output

if __name__ == "__main__":
    params = sys.argv[1:]
    load_words_file()
    output = fetch_random_words(params[0])
    print (output)