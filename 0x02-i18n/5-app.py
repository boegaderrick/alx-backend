#!/usr/bin/env python3
"""This module contains a basic babel setup"""
from flask import Flask, g, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Class definition"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """Returns user identified by 'ID' in 'users' dict"""
    try:
        return users.get(int(user_id))
    except Exception:
        return None


@app.before_request
def before_request():
    """Assign user specified in query string to 'g.user'"""
    g.user = get_user(request.args.get('login_as'))


@babel.localeselector
def get_locale():
    """Gets best matched language"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def get_root():
    """This function renders the home page"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
