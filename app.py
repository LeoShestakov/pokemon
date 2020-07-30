# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask import redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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
@app.route('/index')
def index():
    return render_template('index3.html', data=api.get_pokemon_list())

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'GET':
        return redirect(url_for('index'))
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
        if db_team["name"] != "":
            mongo.db.teams.insert(db_team)
        return redirect(url_for('index'))

@app.route('/viewTeams')
def viewTeam():
    data = list(mongo.db.teams.find({}))
    return render_template('viewTeam.html', data=data)

@app.route('/teamDetails/<id>')
def teamDetails(id):
    data = mongo.db.teams.find_one({'_id':ObjectId(id)})
    my_team = team.Team()
    my_team.add_pokemon(data['team'])
    data = my_team
    return render_template('teamDetails.html', data=my_team)

# Experimental Routes
@app.route('/teamSelect')
def teamSelect():
    data = list(mongo.db.teams.find({}))
    print(data)
    return render_template('teamSelect.html', data=data)

@app.route('/game',methods=['GET', 'POST'])
def game():
    if request.method == 'GET':
        return redirect('teamSelect')
    else:
        data = dict(request.form)
        t1 = mongo.db.teams.find_one({'_id': ObjectId(data['team1'])})['team']
        t2 = mongo.db.teams.find_one({'_id': ObjectId(data['team2'])})['team']
        team1 = team.Team()
        team2 = team.Team()
        team1.add_pokemon(t1)
        team2.add_pokemon(t2)
        teams = {'team1': team1.get_team(), 'team2': team2.get_team(), 'typing': team1.get_array()}
        return render_template('game.html', data=teams)