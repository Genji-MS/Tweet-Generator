#rearrange.py
import random
import sys

def rearrange_words(params):
    """ randomly arrange words that were input on the command line (separated by space) and return the results"""
    length = len(params)
    output = ""
    while length > 0:
        rng = random.randint(0,length-1)
        output += params.pop(rng) + " "
        length -= 1
    return output

def reverse_words(params):
    """ reverse the words that were input on the command line (separated by space) and return the results"""
    length = len(params)
    output = ""
    while length > 0:
        output += params.pop(length-1) + " "
        length -=1
    return output

if __name__ == "__main__":
    params = sys.argv[1:]

    output = rearrange_words(params)
    print (f'rearanged words: {output}')
    #output = reverse_words(params)
    #print (f'reversed words: {output}')