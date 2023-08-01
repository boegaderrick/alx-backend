#!/usr/bin/env python3
"""This module contains a basic babel setup"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Class definition"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'fr'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def get_root():
    """This function renders the home page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1')
