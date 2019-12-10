# app.py
import os, math
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from word_frequency import markov_dictionary, parseFile, markov_max_freq, wordcount_max_freq, markov_order_two_with_tokens
from weighted_random import random_word_from_lists, random_markov_word, random_markov_order_two_word, random_markov_two_with_STOP #wordcount_nestedlist

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/itemlist')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
favorites = db.favorites

app = Flask(__name__)

#PARSE INDIVIDUAL SCRIPTS AND COLOR CODE THEM FOR OUR OUTPUT

#parsed_text = parseFile('MonsterUnderTheBed')
#histogram = wordcount_nestedlist(parsed_text)
parsed_text = parseFile('Script_Labyrinth_clean') #blue
# 1storder markov_dict = markov_dictionary(parsed_text, 'blue')
markov_2nd = markov_order_two_with_tokens(parsed_text, 'blue')

parsed_text = parseFile('Script_LastUnicorn_clean') #pink/light purple
# 1storder markov_dict = markov_dictionary(parsed_text, 'pink', markov_dict)
markov_2nd = markov_order_two_with_tokens(parsed_text, 'pink', markov_2nd)

parsed_text = parseFile('Script_Legend_clean') #red
# 1storder markov_dict = markov_dictionary(parsed_text, 'red', markov_dict)
markov_2nd = markov_order_two_with_tokens(parsed_text, 'red', markov_2nd)

parsed_text = None
# 1storder max_freq_word = wordcount_max_freq(histogram)
# 1storder max_freq_markov = markov_max_freq(markov_dict)
#max_freq_markov = markov_max_freq(markov_2nd)

@app.route('/')
def index():
    """Return homepage"""
    #note to self, instead of global, run the function as above
    #global randomgram
    #if randomgram == None:
    #    print ('running init')
    #    randomgram = init()

    #style = ['a','b','c','d','e','f']
    wordlist = []
    colored_wordlist = []
    words = request.args.get('num')
    num_words = int(words) if (words != None and words != "" and int(words)>8) else 8
    used_words = 0
    look_for_STOP = False
    end = False

    data = None #instantiated here for visibility outside of the ifs:
    phrase = ""
    color = ""
    #for x in range(num_words):
    while end is False:
        if used_words == num_words:
            look_for_STOP = True
        #print (f' x: {x} word:{word}')
        #Generate word based on starting position
        if used_words == 0:
            data = random_markov_order_two_word("START START", markov_2nd)
            # 1storder word = random_word_from_lists(histogram)
            #tag = math.floor( (word[1]/max_freq_markov) * 5)
            #phrase = word = data[0]
            word = data[0] #grab both words
            color = data[1]
            used_words += 1 #add one ADDITIONAL here, as we add one each cycle 
        else:
            data = random_markov_two_with_STOP(phrase, markov_2nd, look_for_STOP)
            #tag = math.floor( (word[1]/max_freq_markov) * 5)
            #phrase = data[0]
            word = data[0].split(" ")[1]
            color = data[1]
        
        phrase = data[0] #store our phrase to be used in the next loop
        used_words += 1

        if color == 'red':
            color = "text-danger"
        elif color == 'blue':
            color = "text-primary"
        elif color == 'pink':
            color = "text-info"
        else:
            color = ""
        
        if word == '888' or word == 'STOP':
            end = True
            break #if random word doesn't return another connection, 888 is returned to end the chain prematurely
        else:
            wordlist.append(word)
            #f_wordlist.append( [word[0],style[tag]] )
            colored_wordlist.append( [word, color])

        #print (f'\nwordlist length = {used_words} looking for stop = {look_for_STOP} end = {end}')
        #print (f' phrase = {phrase}, \n "{wordlist}"')

    return render_template('index.html', f_wordlist = colored_wordlist, wordlist = wordlist, favorites = favorites.find() )

@app.route('/favorite/<wordlist>', methods=['GET'])
def add_favorite(wordlist):
    """Add item to favorites and return to index page"""

    unwanted_punctuation_table = dict.fromkeys(map(ord, "'[],:1234567890"), None)    
    wordlist = wordlist.translate(str.maketrans(unwanted_punctuation_table))
    
    new_fav = {
        'text': wordlist
    }
    #print (f'parsing stuff: {new_fav} wordlist:{wordlist} word:{wordlist[0]}')
    favorites.insert_one(new_fav)
    return redirect(url_for('index'))

@app.route('/<fav_id>/delete', methods=['POST'])
def delete_favorite(fav_id):
    """Delete specified item from cart"""
    favorites.delete_one({'_id':ObjectId(fav_id)})
    return redirect(url_for('index'))

if app.name == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
    