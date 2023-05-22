from googletrans import Translator

translator = Translator()


def detect(text):
    return translator.detect(text).lang


def translate(text, dest, src):
    if src == 'NaN':
        src = detect(text)
    return translator.translate(text, dest=dest, src=src).text
