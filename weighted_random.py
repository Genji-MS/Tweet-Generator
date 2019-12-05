from word_frequency import parseFile, markov_dictionary, markov_order_two_with_color
#from numpy.random import choice
from random import randint

#total_words = 0 # can use sum(dictionary.value) to grab all the key values to add them up
histogram_words = []
histogram_frequency = []
weighted_rng = []
randomgram = []

def create_weights(histogram_list):
    """Using a dictiornary histogram, create our weights"""
    global weighted_rng

    for number in histogram_frequency:
        weighted_rng.append(number/total_words)

def wordcount_list(histogram):
    """seperate into unique words and count them ALL up"""
    global histogram_words, histogram_frequency, total_words

    total_words = len(histogram)

    for i, word in histogram:
        if word not in histogram_words:
            histogram_words.append(word)
            histogram_frequency.append(1)
        else:
            histogram_frequency[i] += 1

def wordcount_nestedlist(parsed_text):
    #global total_words

    total_words = len(parsed_text)
    histogram = [[parsed_text[0],0,0]]

    for word in parsed_text:
        match = False
        for gram in histogram:        
            if word == gram[0]:
                match = True
                gram[1] += 1    
        if match == False:
            item = [word, 1, 0]
            histogram.append(item)

    return histogram

def random_word():
    rng = randint(0,total_words-1)
    index = 0
    total = 0
    for numbers in histogram_frequency:
        total += numbers
        if rng < total:
            break
        index += 1
    print (f' rng:{rng}  total:{total}  index#:{index}')
    print (f'random weighted word: {histogram_words[index]} freq is {histogram_frequency[index]}')
    return histogram_words[index]
    #choice(histogram_words, p=weighted_rng)

def random_word_from_lists(histogram):
    total_words = 0
    for num in histogram:
        total_words += num[1]

    rng = randint(0,total_words-1)
    word = ""
    freq = 0
    total = 0
    for gram in histogram:
        total += gram[1]
        if rng < total:
            word = gram[0]
            freq = gram[1]
            break

    #print (f' |{word}| freq: {freq} {rng}:{total_words} ')
    return [word, freq]
    #return word
    #choice(histogram_words, p=weighted_rng)

def random_starter_words(starter_words):
    total_words = 0
    for key in starter_words.keys():
        #print(f"checking starter word: {key} and value: {starter_words[key]}")
        total_words += starter_words[key][1]

    rng = randint(0,total_words-1)
    words = ""
    color = ""
    freq = 0
    total = 0
    for key in starter_words.keys():
        total += starter_words[key][1]
        if rng < total:
            words = key
            color = starter_words[key][0]
            freq = starter_words[key][1]
            break

    #print (f' |{word}| freq: {freq} {rng}:{total_words} ')
    return [words, color, freq]

def random_markov_word(current_word, markov_dict):
    try:
        next_word_list = markov_dict[current_word]
    except:
        return ["888", '', 0]

    total_words = 0
    for num in next_word_list:
        total_words += num[2]

    rng = randint(0,total_words-1)
    next_word = ""
    color = ""
    freq = 0
    total = 0
    for word in next_word_list:
        total += word[2]
        if rng < total:
            next_word = word[0]
            color = word[1]
            freq = word[2]
            break
        
    return [next_word, color, freq]

def random_markov_order_two_word(current_phrase, markov_order_two_dict):
    try:
        next_word_list = markov_order_two_dict[current_phrase]
    except:
        return ["888", '', 0]

    #print (next_word_list)
    total_words = 0
    for num in next_word_list:
        total_words += num[2]

    rng = randint(0,total_words-1)
    next_phrase = ""
    color = ""
    freq = 0
    total = 0
    for word in next_word_list:
        total += word[2]
        if rng < total:
            next_phrase = word[0]
            color = word[1]
            freq = word[2]
            break
        
    return [next_phrase, color, freq]

def create_randomgram(word):
    global randomgram

    for gram in randomgram:        
        if word == gram[0]:
            gram[2] += 1

def init():
    """used to initialize our files when called from a flask app"""
    global randomgram
    parsed_text = parseFile('MonsterUnderTheBed')
    histogram = wordcount_nestedlist(parsed_text)
    #create_weights(histogram)
    randomgram = sorted(histogram, key = lambda x:x[0])

    return randomgram

def compare_randogram_to_histogram(histogram):
    for x in range(total_words):
        word = random_word_from_lists(histogram)
        create_randomgram(word)
    for i, gram in enumerate(randomgram):
        print (f'{i} | {gram[0]} |  -random freq: {gram[2]} -word freq: {gram[1]}')
    #print (f'random weighted word = {random_word()}')

if __name__ == "__main__":
    parsed_text = parseFile('MonsterUnderTheBed')
    histogram = wordcount_nestedlist(parsed_text)
    #create_weights(histogram)
    randomgram = sorted(histogram, key = lambda x:x[0])
    
    