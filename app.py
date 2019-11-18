# app.py
import os, math
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from word_frequency import markov_dictionary, parseFile, markov_max_freq, wordcount_max_freq
from weighted_random import random_word_from_lists, random_markov_word, wordcount_nestedlist

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/itemlist')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
favorites = db.favorites

app = Flask(__name__)

#parsed_text = parseFile('MonsterUnderTheBed')
parsed_text = parseFile('Script_Labyrinth_clean') #blue
histogram = wordcount_nestedlist(parsed_text)
markov_dict = markov_dictionary(parsed_text, 'blue')
max_freq_markov = markov_max_freq(markov_dict)

parsed_text = parseFile('Script_LastUnicorn_clean') #pink/light purple
markov_dict = markov_dictionary(parsed_text, 'pink', markov_dict)
max_freq_markov = markov_max_freq(markov_dict)

parsed_text = parseFile('Script_Legend_clean') #red
markov_dict = markov_dictionary(parsed_text, 'red', markov_dict)

parsed_text = None
max_freq_word = wordcount_max_freq(histogram)
max_freq_markov = markov_max_freq(markov_dict)

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
    num_words = int(words) if (words != None and words != "" and int(words)>1) else 1
    
    word = ""
    color = ""
    for x in range(num_words):
        #print (f' x: {x} word:{word}')
        if x == 0:
            word = random_word_from_lists(histogram)
            #tag = math.floor( (word[1]/max_freq_markov) * 5)
            color = None
        else:
            word = random_markov_word(word, markov_dict)
            #tag = math.floor( (word[1]/max_freq_markov) * 5)
            color = word[1]
        if color == 'red':
            color = "text-danger"
        #elif color == 'blue':
        #    color = "text-primary"
        elif color == 'pink':
            color = "text-info"
        else:
            #labyrinth blue
            color = "text-primary"
        if word[0] == '888': break #if random word doesn't return another connection, 888 is returned to end the chain prematurely
        wordlist.append(word[0])
        #f_wordlist.append( [word[0],style[tag]] )
        colored_wordlist.append( [word[0], color])
        word = word[0]

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
    