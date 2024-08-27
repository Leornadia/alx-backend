#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

@app.route('/')
def index():
    """Simple index page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

# Babel configuration
@babel.localeselector
def get_locale():
    """Determine the best language for each request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])
