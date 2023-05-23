from googletrans import Translator

translator = Translator()


def detect(text):
    return translator.detect(text).lang


def translate(input_text, language_from, language_to):
    if language_from == 'NaN':
        language_from = detect(input_text)
    return translator.translate(input_text, dest=language_to, src=language_from).text
