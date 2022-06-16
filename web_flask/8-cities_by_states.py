#!/usr/bin/python3
""" Starts a Flask web application """


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """List all the cities by states in the database"""
    all_states = storage.all('State')
    return render_template("8-cities_by_states.html", states=all_states)


@app.teardown_appcontext
def close_session(response_or_exc):
    """close sqlalchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
