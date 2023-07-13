"translate from en to fr or fr to en"
from deep_translator import MyMemoryTranslator
def englishToFrench (englishText):
    "translate french sentance into English"
    result  =  MyMemoryTranslator(source='en-US', target='fr-FR').translate(englishText)
    return result


def frenchToEnglish(frenchText):
    "translate french sentance into English"
    result  =  MyMemoryTranslator(source='fr-FR', target='en-GB').translate(frenchText)
    return result


