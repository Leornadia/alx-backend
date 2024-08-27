#!/usr/bin/env python3
""" 2. Get locale from request object """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """ Configuration class for Flask app. """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app) 
app.url_map.strict_slashes = False


@babel.localeselector
def get_locale():
    """Determine the best match for supported languages from request."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def welcome() -> str:
    """ / page """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
