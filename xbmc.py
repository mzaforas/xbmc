# -*- coding: utf-8 -*-

# all the imports

import os
import os.path
import datetime
import time
import arrow
import requests

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash


# app instance
app = Flask(__name__)

# configuration
DEBUG = True
SECRET_KEY = 'development key'
app.config.from_object(__name__)


# controllers
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/execute")
def execute():
    action = request.args.get('action')
    if action:
        payload = {'request': '{ "jsonrpc": "2.0", "method": "Player.Open", "params": { "item": { "partymode": "music" } }, "id": 1 }'}
        response = requests.get('http://192.168.1.11:8080/jsonrpc', params=payload)
        if response.status_code != requests.codes.ok:
            flash('Error sending XBMC command')

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
