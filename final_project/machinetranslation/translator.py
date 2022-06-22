"Provides translation functions to translate English to French and vice versa."
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

def englishToFrench(englishText):
    "Translates englishText to French using IBM Watson translator"
    if englishText != '':
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
    else:
        result = ''
    return result
def frenchToEnglish(frenchText):
    "Translates frenchText to English using IBM Watson translator"
    if frenchText != '':
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
    else:
        result = ''
    return result
