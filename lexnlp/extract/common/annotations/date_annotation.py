from datetime import date as _date
from typing import Tuple, List
from lexnlp.extract.common.annotations.text_annotation import TextAnnotation

__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2020, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-lexnlp/blob/master/LICENSE"
__version__ = "1.6.0"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"


class DateAnnotation(TextAnnotation):
    record_type = 'date'
    """
    create an object of ActAnnotation like
    cp = ActAnnotation(name='name', coords=(0, 100), text='text text')
    """
    def __init__(self,
                 coords: Tuple[int, int],
                 locale: str = 'en',
                 text: str = None,
                 date: _date = None,
                 score: float = None):
        super().__init__(
            name='',
            locale=locale,
            coords=coords,
            text=text)
        self.date = date
        self.score = score

    def get_cite_value_parts(self) -> List[str]:
        return [str(self.date or '')]

    def get_dictionary_values(self) -> dict:
        df = {
            "tags": {
                'Extracted Entity Date': str(self.date or ''),
                'Extracted Entity Text': self.text
            }
        }
        return df
