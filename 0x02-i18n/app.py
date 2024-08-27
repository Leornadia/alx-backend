#!/usr/bin/env python3
"""Display current time on the home page based on the inferred time zone."""
from flask import Flask, render_template, request
from flask_babel import Babel, _
from datetime import datetime
import pytz

app = Flask(__name__)
app.url_map.strict_slashes = False

class Config:
    """Configuration class for Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

babel = Babel(app)

@babel.localeselector
def get_locale():
    """Determine the best match with supported languages."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@babel.timezoneselector
def get_timezone():
    """Select the appropriate timezone."""
    # Here you could extract the timezone from the user or use the default
    return request.args.get('timezone', app.config['BABEL_DEFAULT_TIMEZONE'])

@app.route("/")
def welcome():
    """Renders the home page with the current time."""
    current_time = datetime.now(pytz.timezone(get_timezone())).strftime('%b %d, %Y, %I:%M:%S %p')
    return render_template('index.html', current_time=current_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

