# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import url_for
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
        return render_template('index.html', data=constants.get_pokemon_list())
    else:
        form = list(request.form)
        return render_template('results.html', data=form)