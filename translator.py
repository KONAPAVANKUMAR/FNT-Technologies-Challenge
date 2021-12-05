from deep_translator import GoogleTranslator

def englishToFrench(to_translate):
    return GoogleTranslator(source='en', target='fr').translate(to_translate)