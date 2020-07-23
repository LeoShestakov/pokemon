# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import session
import constants

import requests #To access our API

# -- Initialization section --
app = Flask(__name__)

## secret key for session (In production, you would set this key via an environment variable)
app.secret_key = b'HO\xf8\xff+\n\x1e\\~/;}'

# -- Routes section --
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        print("GET")
    else:
        form = list(request.form)
        print(form)
    return render_template('index.html', data=constants.get_pokemon_list())
