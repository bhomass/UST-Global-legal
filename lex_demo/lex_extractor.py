import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from lexnlp.extract.common.annotation_type import AnnotationType
from lexnlp.extract.common.fact_extracting import FactExtractor, ExtractorResultFormat
from lexnlp.extract.en.geoentities import load_entities_dict_by_path

import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('punkt')

class Lex_extractor:
    
    def __init__(self):
        filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'data', '1000453_1997-11-14_CREDIT AGREEMENT.txt')
        
        with open(filepath, 'r') as doc_file:
            self.text = doc_file.read()

        FactExtractor.initialize()
        
    def parse_text(self):
        facts = FactExtractor.parse_text(self.text,
                                         FactExtractor.LANGUAGE_EN,
                                         ExtractorResultFormat.fmt_class,
        #                                  extract_all=True,
                                         exclude_types={AnnotationType.geoentity},
        #                                  include_types={AnnotationType.act, AnnotationType.court})  
                                         include_types={AnnotationType.money, AnnotationType.copyright, AnnotationType.percent,\
                                                        AnnotationType.regulation, AnnotationType.trademark, \
                                                        AnnotationType.laws, AnnotationType.act, AnnotationType.court
                                                        }
                                 )        
        
        return facts
    
    
    