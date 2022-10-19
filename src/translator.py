    
from google.cloud import translate_v2 as translate
import os, six 
from typing import Union, Sequence, List
class GoogleTranslator:
    '''A wrapper for the Google Translation API'''
    base_url = 'https://translation.googleapis.com/language/translate/v2'

    def __init__(self):
        self.api_key =  os.getenv('GOOGLE_TRANSLATION_API_PATH')
        
    def __call__(self, text:Union[str, List[str]], lang: str ='en'):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = self.api_key
        translator = translate.Client()
        if type(text) == str:
            if isinstance(text, six.binary_type):
                text = text.decode("utf-8")
        # Text can also be a sequence of strings, in which case this method
        # will return a sequence of results for each text.
            result = translator.translate(text, target_language=lang)
            return  result["translatedText"]
        elif type(text) == list: 
            text_list = []
            for each_text in text:
                if isinstance(each_text, six.binary_type):
                    each_text = each_text.decode("utf-8")
                result = translator.translate(each_text, target_language=lang)
                text_list.append(result['translatedText'])
            return text_list
