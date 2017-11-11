from flask import Flask, session, url_for, redirect, render_template, request

import os
import urllib2
import json

#App instantiation
app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def main():
    uResp = urllib2.urlopen('https://na1.api.riotgames.com/lol/static-data/v3/champions?locale=en_US&dataById=false&api_key=RGAPI-15f81515-8c2e-4b9e-9c27-ab28e1b37edf')
    blah = uResp.read()
    #print blah
    dict1 = json.loads(blah)
    print dict1["data"]["Jax"]["name"]
    return render_template('index.html', dictionary = dict1["data"])

if __name__ == "__main__":
    app.debug = True
app.run()
