#!/usr/bin/python3
"""
Start a Flask web application
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Start web application

    Returns:
    Hello HBNB!
    """

    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return statement

    Returns:
    HBNB
    """

    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Display a text

    Description:
    This method displays "C " followed by the value of
    the text variable
    """

    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """Display a text

    Description:
    This method displays 'Python ', followed by the value
    of the text variable
    """

    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """Display an integer number

    Description:
    This method displays "n" only if it is an integer
    """
    
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """Display a HTML page

    Description:
    This method displays a HTML page only if n is an integer
    """

    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
