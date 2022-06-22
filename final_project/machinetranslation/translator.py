import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

def englishToFrench(englishText):
    text = englishText
    language = 'en-fr'

    auth = IAMAuthenticator(apikey)
    language_translator_obj = LanguageTranslatorV3(
        authenticator=auth,
        version='2018-05-01'
    )
    language_translator_obj.set_service_url(url)

    result = language_translator_obj.translate(
        text = text,
        model_id = language
    ).get_result()['translations'][0]['translation']
    return result
def frenchToEnglish(frenchText):
    text = frenchText
    language = 'fr-en'

    auth = IAMAuthenticator(apikey)
    language_translator_obj = LanguageTranslatorV3(
        authenticator=auth,
        version='2018-05-01'
    )
    language_translator_obj.set_service_url(url)

    result = language_translator_obj.translate(
        text = text,
        model_id = language
    ).get_result()['translations'][0]['translation']
    return result
