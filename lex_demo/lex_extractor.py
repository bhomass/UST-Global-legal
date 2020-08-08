import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from lexnlp.extract.common.annotation_type import AnnotationType
from lexnlp.extract.common.fact_extracting import FactExtractor, ExtractorResultFormat
from lexnlp.extract.en.geoentities import load_entities_dict_by_path

import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('punkt')

import re
import pandas as pd

class Lex_extractor:
    
    def __init__(self):
        filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'data', '1000453_1997-11-14_CREDIT AGREEMENT.txt')
        
        with open(filepath, 'r') as doc_file:
            text = doc_file.read()
            
#         lines = text.split('\n')
#         curated_lines = []
#         i = 0
#         for line in lines:
#             if len(line) > 0:
#                 curated_lines.append(line)
# #                 i += 1
# #                 if i > 200:
# #                     break

#         self.text = '\n'.join(curated_lines)
        self.text = text
        FactExtractor.initialize()
        
    def parse_text(self):
        facts = FactExtractor.parse_text(self.text,
                                         FactExtractor.LANGUAGE_EN,
                                         ExtractorResultFormat.fmt_class,
                                         extract_all=False,
#                                          exclude_types={AnnotationType.geoentity},
#                                          include_types={AnnotationType.copyright}  
                                         include_types={AnnotationType.money, AnnotationType.percent,\
                                                        AnnotationType.regulation, AnnotationType.trademark, \
                                                        AnnotationType.laws, AnnotationType.act, AnnotationType.court
                                                        }
                                 )        
        
        ner_df = self.derive_df(facts)
#         print('parse_text df shape={}'.format(ner_df.shape))
        return ner_df
    
    def get_text(self):
        return self.text
    
    def derive_df(self, facts):
        rows = []
        for key, fact_value in facts.items():
            print('key:{}'.format(key))
            value_list = fact_value
            print('{} values'.format(len(value_list)))
            for value in value_list:
                print('----------------')
                row_dict = {}
                row_dict['type'] = str(key).replace('AnnotationType.', '')
                extracted_text = value.get_extracted_text(self.text)
                print('extracted text = {}'.format(extracted_text))
                row_dict['extracted'] = extracted_text.replace('\n', ' ')
                value_dict = value.to_dictionary()
                start = int(value_dict['attrs']['start'])
                end = int(value_dict['attrs']['end'])
                print('indices = {},{}'.format(start, end))
                line = find_beginning_end(start, end, self.text)
                row_dict['original'] = line.replace('\n', ' ')
                print('line = {}'.format(line))
                rows.append(row_dict)
                
        ner_df = pd.DataFrame(rows)
#         print('derive_df df shape={}'.format(ner_df.shape))
        return ner_df
              

def find_new_line_backward(start, end, text):
    if end == 0:
        end = start + 1
    start -= 1     # start backing up the document
    partial_str = text[start: end]
#     print('partial_str={}'.format(partial_str))
    start_index = -1
    try:
        start_index = re.search("\n\n", partial_str).start()
    except:
        pass
#     print('start_index= {}'.format(start_index))
    while start_index != 0:
        start -= 1
        partial_str = text[start: end]
#         print('partial_str={}'.format(partial_str))
        try:
            start_index = re.search("\n\n", partial_str).start()
        except:
            pass
#         print('start_index= {}'.format(start_index))
    
#     print('final start_index= {}'.format(start))
    return start

def find_new_line_forward(start, end, text):
    end += 1     # start backing up the document
    partial_str = text[start: end]
#     print('partial_str={}'.format(partial_str))
    end_index = -1
    try:
        end_index = re.search("\n\n", partial_str).start()
    except:
        pass
#     print('start_index= {}'.format(start_index))
    while end_index == -1:
        end += 1
        partial_str = text[start: end]
#         print('partial_str={}'.format(partial_str))
        try:
            end_index = re.search("\n\n", partial_str).start()
        except:
            pass
#         print('end_index= {}'.format(end_index))
    
#     print('final end_index= {}'.format(start))
    return end

def find_beginning_end(start, end, text):
    line_start = find_new_line_backward(start, end, text)
    line_end = find_new_line_forward(start, end, text)
    line = text[line_start + 2: line_end - 2]
#     print('before sub line={}'.format(line))
    line = re.sub('[*]+', '', line)
    line = line.replace('<TABLE>', '').replace('<S>', '').replace('<C>','').replace('<PAGE>','').strip()
#     print('after sub line={}'.format(line))
    return line

