import os
import sys
import subprocess
import requests
import ssl
import random
import string
import json

from flask import jsonify
from flask import Flask
from flask import request
from flask import send_file
import traceback

import torch



try:  # Python 3.5+
    from http import HTTPStatus
except ImportError:
    try:  # Python 3
        from http import client as HTTPStatus
    except ImportError:  # Python 2
        import httplib as HTTPStatus


app = Flask(__name__)



@app.route("/process", methods=["POST", "GET"])
def process():

    try:
        text = request.json["text"]
        top_k = request.json["top_k"]

        if "<mask>" not in text:
            text = text + ' <mask>' 

        callback = json.dumps(camembert.fill_mask(text, topk=int(top_k)))

        return callback, 200

    except:
        traceback.print_exc()
        return {'message': 'input error'}, 400


if __name__ == '__main__':
    global camembert

    camembert = torch.hub.load('pytorch/fairseq', 'camembert.v0')

    port = 5000
    host = '0.0.0.0'

    app.run(host=host, port=port, threaded=False)

