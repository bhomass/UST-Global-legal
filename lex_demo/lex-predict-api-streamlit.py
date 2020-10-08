import sys
sys.path.insert(0,'..')

import streamlit as st

import time

import pandas as pd

from lex_demo.lex_extractor import Lex_extractor

intro_text = """This Demo leverages lexpredict which is an open source lib for working with real, unstructured legal text, including contracts, plans, policies, procedures, and other material.

LexNLP provides functionality such as:

Segmentation and tokenization, such as A sentence parser that is aware of common legal abbreviations like LLC. or F.3d. Pre-trained segmentation models for legal concepts such as pages or sections.
Pre-trained word embedding and topic models, broadly and for specific practice areas
Pre-trained classifiers for document type and clause type
Broad range of fact extraction, such as: Monetary amounts, non-monetary amounts, percentages, ratios Conditional statements and constraints, like "less than" or "later than" Dates, recurring dates, and durations Courts, regulations, and citations
Tools for building new clustering and classification methods
Hundreds of unit tests from real legal documents
The demo takes an open source credit agreeement from Edgar database http://edgar.secdatabase.com/399/95013798000790/filing-main.htm

and extracts the following type of legal entities: money, copyright, percent, regulation, trademark, laws, act, court"""

st.text(intro_text)

start_time = time.time()
extractor = Lex_extractor()
ner_df = extractor.parse_text()

print("--- %s seconds ---" % (time.time() - start_time))
text = extractor.get_text()

# st.text(text)
st.text_area('corpus', value=text, height=600, max_chars=None, key=None)

pd.set_option('max_colwidth', -1)

ner_df

