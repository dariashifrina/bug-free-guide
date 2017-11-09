from flask import Flask, session, url_for, redirect, render_template, request

import os
import urllib2
import json

#App instantiation
app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def main():
    uResp = urllib2.urlopen('https://api.nasa.gov/planetary/apod?api_key=G9uli2REXs972OE7lle8lTSoH6idWHXw6pDcCFcH')
    blah = uResp.read()
    dict1 = json.loads(blah)
    return render_template('index.html', dictionary = dict1['url'], d2 = dict1['hdurl'])

if __name__ == "__main__":
    app.debug = True
app.run()