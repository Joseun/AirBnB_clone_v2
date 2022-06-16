#!/usr/bin/python3
""" Starts a Flask web application """


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """ List all cities in a specific state if id is present    """
    states = storage.all('State')
    if id:
        key = '{}.{}'.format('State', id)
        if key in states:
            states = states[key]
        else:
            states = None
    return render_template('9-states.html', states=states, id=id)

@app.teardown_appcontext
def close_session(response_or_exc):
    """close sqlalchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
