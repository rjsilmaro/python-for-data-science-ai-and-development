# import speech to text from ibm_watson
from ibm_watson import SpeechToTextV1
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pandas import json_normalize
# import language translator from ibm_watson
from ibm_watson import LanguageTranslatorV3

# speech to text
url_s2t = "https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/786e4d64-6ab0-423f-8af0-6f1fdfd81d8e"
iam_apikey_s2t = "HpZISADzD8pIhoIcRw8-YzR8gnDrYhU5axlsooqRGbAk"

# create speech to text object
authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
s2t

# mp3 file
filename='PolynomialRegressionandPipelines.mp3'

# create the file object wav
# mode "rb" means read mode but ensures the file is in binary mode
# recognize method return the recognized text
# The parameter audio is the file object wav, the parameter content_type is the format of the audio file
with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')

# normalized the json result
json_normalize(response.result['results'],"alternatives")

# obtain the recognized text and assign it to the variable recognized text
recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]

# language translator
url_lt='https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/d92b9b3d-35ea-4126-9f59-1249e5e69252'
apikey_lt='g_xhnBmF5Pj7SNCwQw58jstpngRWUoJ4Je9UeZYx73tL'

# API requests require a version parameter that takes a date in the format version=YYYY-MM-DD.
# describes the current version of Language Translator, 2018-05-01
version_lt='2018-05-01'


# create language translator object
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
language_translator

# normalized the json result
json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")

# translate the text
# model_id is the type of language model 'en-es' means english to spanish
translation_response = language_translator.translate(\
    text=recognized_text, model_id='en-es')
translation_response

#the result is a dictionary
translation=translation_response.get_result()
translation

# get first actual translation string
spanish_translation =translation['translations'][0]['translation']
spanish_translation

# we can translate back to english
translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()
# obtain the first actual translation string
translation_eng=translation_new['translations'][0]['translation']
translation_eng

# translate to french
#French_translation=language_translator.translate(
 #   text=translation_eng , model_id='en-fr').get_result()

#French_translation['translations'][0]['translation']