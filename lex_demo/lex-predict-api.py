import sys
sys.path.insert(0,'..')

import streamlit as st

import time

import pandas as pd

from lex_demo.lex_extractor import Lex_extractor

start_time = time.time()
extractor = Lex_extractor()
ner_df = extractor.parse_text()

print("--- %s seconds ---" % (time.time() - start_time))
text = extractor.get_text()



# st.text(text)
st.text_area('corpus', value=text, height=600, max_chars=None, key=None)

pd.set_option('max_colwidth', -1)

ner_df


# import flask
# from flask import request, jsonify

# app = flask.Flask(__name__)
# app.config["DEBUG"] = True

# from pdf_files.pdf_agent import PDF_agent

# covid_agent = PDF_agent()
# file = 'EBC External 06.10.20 FAQs.pdf'
# covid_agent.read_file(file)
# corpus = covid_agent.get_corpus()


# @app.route('/', methods=['GET'])
# def home():
#     return "<h1>Covid Question Answer</h1><p>This site is a prototype API for QA agent which answers Covid questions.</p>"



# @app.route('/api/v1/covid-agent/answer', methods=['PUT'])
# def answer_question():
#     query_parameters = request.args
#     question = query_parameters['question']
#     print('calling agent to answer')
#     answer = covid_agent.answer(question)
#     print('got answer: {}'.format(answer))
    
#     return jsonify({'answer':answer})

    
# app.run(host='0.0.0.0')


