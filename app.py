from flask import Flask, redirect, url_for, render_template, request, session
from flask import jsonify

import json
import sys
import os
from os import listdir

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.secret_key = os.urandom(12)  # Random key for dev purposes
    app.run()
