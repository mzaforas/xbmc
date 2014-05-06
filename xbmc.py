# -*- coding: utf-8 -*-

# all the imports
import json

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
        payload = get_payload(action)
        print payload
        response = requests.get('http://192.168.1.11:8080/jsonrpc', params=payload)
        if response.status_code != requests.codes.ok:
            flash('Error sending XBMC command')

    return redirect(url_for('index'))


def get_payload(action):
    XBMC_RPC_API = {
        'up':  {'method': 'Input.Up'},
        'down': {'method': 'Input.Down'},
        'left':  {'method': 'Input.Left'},
        'right':  {'method': 'Input.Right'},
        'select':  {'method': 'Input.Select'},
        'playpause':  {'method': 'Player.PlayPause', 'params': {'playerid': 1}},
        'stop':  {'method': 'Player.Stop', 'params': {'playerid': 1}},
        'backward':  {'method': 'Player.Move', 'params': {'playerid': 1, 'direction': 'left'}},
        'forward':  {'method': 'Player.Move', 'params': {'playerid': 1, 'direction': 'right'}},
        'home':  {'method': 'Input.Home'},
        'party': {'method': 'Player.Open', 'params': {'item': {'partymode': 'music'}}, 'id': 1},
        'scan-video':  {'method': 'VideoLibrary.Scan'},
        'scan-music':  {'method': 'AudioLibrary.Scan'},
    }

    method = XBMC_RPC_API.get(action, {}).get('method')
    params = XBMC_RPC_API.get(action, {}).get('params', [])
    return {'request': json.dumps({'jsonrpc': '2.0', 'method': method, 'params': params})}


if __name__ == "__main__":
    app.run(host='0.0.0.0')
