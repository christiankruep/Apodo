#Apodo.py
#By Christian Kruep

import flask, random
from flask import request, jsonify

#repository of first names sourced from all over
first_bank = ('Gus', 'Enoch', 'Flo', 'Theoden', 'Pippin', 'Samwise',
              'Loial', 'Gandalf', 'Matrim', 'Perrin', 'Randy', 'Bob',
              'Theoden', 'Andrew', 'Arnie', 'Clunt', 'Kvothe',
              'Rincewind', 'Twoflower', 'Mort', 'Krom', 'Bravd',
              'Deacon', 'Rand', 'Thom', 'Minipat', 'Wile E.')

#repository of last names sourced from all over
last_bank = ('Longfellow', 'De Smet', 'Cauthon', 'Al Thor', 'The Grey',
             'Wizard', 'De Los Altos', 'Bell', 'Anglesmith', 'Del Gato',
             'Underhill', 'Root', 'Bard', 'Barksdale',
             'McNulty', 'Flagstaff', 'Guster', 'Coyote')

#randomly generates up a false name. Puts them into a dictionary
def gin_up_false_name():
    falsename = [
        {'first_name': random.choice(first_bank),
         'last_name': random.choice(last_bank) }
    ]
    return falsename

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<Apodo</h1><p>This site is a prototype API for generating fake names.</p>"

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Resource could not be found</p>", 404

#returns all first and last names that fake names are created from
@app.route('/api/v1/resources/names/all', methods=['GET'])
def api_all():
    names = [{'first_names': first_bank,
             'last_names': last_bank}]
    return jsonify(names)

# A route to return a randomly generated false name
@app.route('/api/v1/resources/rando_name', methods=['GET'])
def api_random_name():
    return jsonify(gin_up_false_name())

app.run()
