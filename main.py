import googletrans
from googletrans import Translator

# this will list out all the different languages and codes
print(googletrans.LANGUAGES)

translator = Translator()

result = translator.translate('what is up', src='en', dest='de')

print(result.text)