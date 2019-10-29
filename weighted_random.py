from word_frequency import parseFile
#from numpy.random import choice
from random import randint

total_words = 0
histogram_words = []
histogram_frequency = []
weighted_rng = []

def create_weights(histogram_list):
    """Using a dictiornary histogram, create our weights"""
    global weighted_rng

    for number in histogram_frequency:
        weighted_rng.append(number/total_words)

def wordcount_list(histogram):
    """seperate into unique words and count them ALL up"""
    global histogram_words, histogram_frequency, total_words

    total_words = len(histogram)

    for word in histogram:
        if word not in histogram_words:
            histogram_words.append(word)
            histogram_frequency.append(1)
        else:
            i= histogram_words.index(word)
            histogram_frequency[i] += 1

def random_word():
    rng = randint(0,total_words)
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


if __name__ == "__main__":
    histogram = parseFile('MonsterUnderTheBed')
    wordcount_list(histogram)
    create_weights(histogram)
    for x in range(10):
        random_word()
    #print (f'random weighted word = {random_word()}')