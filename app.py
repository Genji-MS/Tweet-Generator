# app.py
import os
from flask import Flask, render_template, request, redirect, url_for
from weighted_random import random_word_from_lists, wordcount_nestedlist, init
from word_frequency import parseFile


app = Flask(__name__)
randomgram = init()

@app.route('/')
def index():
    """Return homepage"""
    #note to self, instead of global, run the function as above
    #global randomgram
    #if randomgram == None:
    #    print ('running init')
    #    randomgram = init()

    wordlist = []
    words = request.args.get('num')
    num_words = 1 if (words != None and int(words)>1) else int(words)

    for x in range(num_words):
        rng_word = random_word_from_lists(randomgram)
        wordlist.append(rng_word)

    return render_template('index.html', wordlist = wordlist )

if app.name == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
    