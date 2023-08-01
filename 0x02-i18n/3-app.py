#!/usr/bin/env python3
"""This module contains a basic babel setup"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Class definition"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """Gets best matched language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def get_root():
    """This function renders the home page"""
    return render_template('3-index.html', home_title=_(
        'home_title'), home_header=_('home_header'))


if __name__ == '__main__':
    app.run(host='127.0.0.1')
