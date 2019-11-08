# word_frequency.py
import os, sys, string

#parsed_text = []
#histogram_words = []
#histogram_frequency = []

def parseFile(document):
    """convert text file into a string of every word, removing all punctuation and converting to lower case"""
    #global parsed_text
    #f = open(os.path.join(sys.path[0],document)).read().split()
    f = open(document).read().split()

    unwanted_punctuation_table = dict.fromkeys(map(ord, '\n\r“”"‘’,.…!?:'), None)    
    parsed_text = [line.translate(str.maketrans(unwanted_punctuation_table)).lower() for line in f]
    #print ( len(parsed_text))
    #wordcount(parsed_text)

    return parsed_text

def markov_dictionary(histogram):
    markov_dict = {}
    for index in range(len(histogram)-2):
        word_1 = histogram[index]
        word_2 = histogram[index+1]
        if word_1 not in markov_dict.keys():
            #new word with its own new list
            markov_dict[word_1] = [ [word_2,1] ]
            #new_list_item = [word_2,1]
            #markov_dict[word_1].append(new_list_item)
        else:
            existing = False
            for x in range(len( markov_dict[word_1] )):
                if word_2 == markov_dict[word_1][x][0]:
                    #increase frequency of existing word
                    markov_dict[word_1][x][1] += 1
                    existing = True
                    break
            if existing == False:
                #add new word to list
                new_list_item = [word_2, 1]
                markov_dict[word_1].append(new_list_item)
    return markov_dict

def markov_max_freq(markov_dict):
    max_freq = 0
    for word_list in markov_dict.values():
        #print(word_list)
        for num in word_list:
            if num[1] > max_freq:
                max_freq = num[1]
    return max_freq

def wordcount_max_freq(histogram):
    max_freq = 0
    for word in histogram:
        if word[1] > max_freq:
            max_freq = word[1]
    return max_freq

def wordcount_list(histogram):
    """seperate into unique words and count them ALL up"""
    global histogram_words, histogram_frequency
    histogram_words = []
    histogram_frequency = []

    for word in histogram:
        if word not in histogram_words:
            histogram_words.append(word)
            histogram_frequency.append(1)
        else:
            i= histogram_words.index(word)
            histogram_frequency[i] += 1
    print( len(histogram_words))
    print( len(histogram_frequency))
    #print(histogram_words)

def wordcount_dict(histogram):
    """worst for space efficiency, best for time"""
    histogram_dict = []

    for word in histogram:
        match = False
        for dict_word in histogram_dict:
            if word in dict_word.keys():
                match = True
                dict_word[word] += 1
        if match == False:
            new_item = {
                word : 1
            }
            histogram_dict.append(new_item)
    print (f'unique words in dict format: { len(histogram_dict)}')

def wordcount_tup(histogram):
    histogram_tup_words = (histogram[0],)
    histogram_tup_freq = (0,)

    for word in histogram:
        match = False
        for tup_word in histogram_tup_words:
            if word == tup_word:
                match = True
                i = histogram_tup_words.index(tup_word)
                head = histogram_tup_freq[:i]
                tail = histogram_tup_freq[i+1:] if (len(histogram_tup_freq) > i) else None
                histogram_tup_freq = head + (histogram_tup_freq[i]+1,) + tail
                #print (histogram_tup_freq)
                #print (f'words: { len(histogram_tup_words)} freq: { len(histogram_tup_freq)}')
        if match == False:
            histogram_tup_words = histogram_tup_words + (word,)
            histogram_tup_freq = histogram_tup_freq + (1,)
    #print (f'unique words in tuple format: { len(histogram_tup_words)}')

def wordcount_count(histogram):
    """worst time efficiency, but best space efficiency"""
    #[(1,['word',word]),
    # (2,['word']),
    # (10,['word','words','wordz']),
    # ]

def unique_words(histogram):
    """take in a histogram and return the number of words overall - Dual List version"""
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
    markov_dict = markov_dictionary(histogram)
    print (f'total words: { len(histogram)}')
    print (f'total of unique words: {unique_words(histogram)}')
    print (markov_dict)
    #wordcount_dict(histogram)
    #wordcount_tup(histogram)
    #print (f'total occurances of the word "monster" :{frequency("monster",histogram)}')