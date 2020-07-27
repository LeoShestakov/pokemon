# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask import redirect
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
import datetime

import team
import api

import requests #To access our API


load_dotenv()
# -- Initialization section --
app = Flask(__name__)

## secret key for session (In production, you would set this key via an environment variable)
app.secret_key = b'HO\xf8\xff+\n\x1e\\~/;}'

MONGO_DBNAME = os.getenv("MONGO_DBNAME")
MONGO_DB_USERNAME = os.getenv("MONGO_DB_USERNAME")
MONGO_DB_PASSWORD = os.getenv("MONGO_DB_PASSWORD")

app.config['MONGO_DBNAME'] = MONGO_DBNAME
app.config['MONGO_URI'] = f"mongodb+srv://{MONGO_DB_USERNAME}:{MONGO_DB_PASSWORD}@cluster0.b4bsb.mongodb.net/{MONGO_DBNAME}?retryWrites=true&w=majority"

mongo = PyMongo(app)

# -- Routes section --
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', data=api.get_pokemon_list())
    else:
        form = list(request.form)
        my_team = team.Team()
        my_team.add_pokemon(form)
        session["team"] = my_team.get_names()
        return render_template('results.html', data=my_team)


@app.route('/addTeam', methods=['GET', 'POST'])
def addTeam():
    if request.method == 'GET':
        return redirect(url_for('index'))
    else:
        form = dict(request.form)
        db_team = {
            "name": form['name'],
            "team": session["team"]
        }
        mongo.db.teams.insert(db_team)
        return redirect(url_for('index'))



