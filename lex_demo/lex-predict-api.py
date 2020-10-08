import sys
sys.path.insert(0,'..')

import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

import pandas as pd
from lex_demo.lex_extractor import Lex_extractor

extractor = Lex_extractor()

ner_df = extractor.parse_text()


@app.route('/', methods=['GET'])
def home():
    return "<h1>Lex Predict</h1><p>This site is a prototype API for applying NER to Legal Documents.</p>"



@app.route('/api/v1/lex-predict/get_text', methods=['GET'])
def get_text():
    text = extractor.get_text()
    
    return jsonify({'text':text})

@app.route('/api/v1/lex-predict/parse_text', methods=['GET'])
def parse_text():    
    return ner_df.to_json()

app.run(host='0.0.0.0', port=9000)


