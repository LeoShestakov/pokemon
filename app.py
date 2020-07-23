# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import session

import requests #To access our API

# -- Initialization section --
app = Flask(__name__)

## secret key for session (In production, you would set this key via an environment variable)
app.secret_key = b'HO\xf8\xff+\n\x1e\\~/;}'

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    link = 'https://pokeapi.co/api/v2'
    poke_link = link + "/pokemon?limit=964"
    response = requests.get(poke_link).json()
    # need to filter out starting part of json (count, etc)
    print(response)
    return render_template('index.html', data = response)
