#!/usr/bin/env python3
"""This module contains a simple flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def get_root():
    """This function renders the home page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1')
