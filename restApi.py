from flask import Flask, jsonify, request

from slackBot import *

verification_token = "ZgP4fW50D1N6Dm9Eu81EKHI4"
app = Flask(__name__)


@app.route('/now', methods=['POST'])
def now():
    send_massge_evexry_hour("CUEMLATB8", datetime.datetime.now())

@app.route('/new-content', methods=['POST'])
def now():
    send_massage_by_tweets()